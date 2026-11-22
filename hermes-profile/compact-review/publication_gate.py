"""Trusted experimental prepublication adapter, never imported by project code.

The MCP scope must check repository, branch and path permissions before calling
this gate. Actor mounts exclude this code, record roots and Docker socket. Tests
run in a separate read-only, network-none container, never in this process.
"""
import json
import os
from pathlib import Path
import uuid
import urllib.request
from review_packet import (ReviewBlocked, encoded, source_digest, apply_changes,
                           build_packet, execution_summaries, admission)
from docker_execution import DockerExecution
from review_transport import request_body, TimedReview, publication_review


def measure_input(endpoint, body):
    """Pinned backend template/tokenizer; no model inference or private inputs."""
    suffix='/v1/chat/completions'
    if not endpoint.endswith(suffix):raise ReviewBlocked('Explicit trusted chat-completions endpoint required')
    base=endpoint[:-len(suffix)]
    def post(path, data=None):
        req=urllib.request.Request(base+path,data=None if data is None else encoded(data),headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=30) as response:return json.load(response)
    props=post('/props')
    if props['model_alias']!=body['model']:raise ReviewBlocked('Reviewer alias differs from selected profile')
    prompt=post('/apply-template',{'messages':body['messages'],'chat_template_kwargs':body['chat_template_kwargs']})['prompt']
    count=len(post('/tokenize',{'content':prompt,'add_special':False,'parse_special':True})['tokens'])
    return {'rendered_tokens':count,'context':props['default_generation_settings']['n_ctx'],'model_alias':props['model_alias']}


def mutation(args, current):
    """Resolve the actual MCP payload; scratch workspace contents are not inputs."""
    result = {}
    files = args.get('files') or [{k:args[k] for k in ('path','content','edits','delete','new_path','from_path') if k in args}]
    for item in files:
        path = item['path']
        if path in result or (item.get('new_path') or item.get('from_path')):
            raise ReviewBlocked('Duplicate paths and implicit renames are unsupported')
        if item.get('delete'):
            content = None
        elif 'content' in item:
            content = item['content']
        elif item.get('edits'):
            content = current.get(path)
            if content is None: raise ReviewBlocked('Cannot edit an absent publication file')
            for edit in item['edits']:
                old = edit['old_string']
                if not old or content.count(old) != 1: raise ReviewBlocked('Ambiguous publication edit')
                content = content.replace(old, edit['new_string'], 1)
        else:
            raise ReviewBlocked('Missing actual publication content')
        result[path] = content
    apply_changes(current, result)  # Includes path and text validation.
    return result


def docs_only_admission(packet, review, *, receipts, key, current_digest, environment_id):
    """Comparison control: actual tests plus external docs check, no code feedback.

    This deliberately is not full-review qualification. A separate report must
    identify the common safety controls and may not call this no-review latency.
    """
    from review_packet import packet_id
    if (len(encoded(packet)) > 32768 or packet_id(packet) != packet['packet_id'] or
            current_digest != packet['candidate_source_digest'] or
            review.get('packet_id') != packet['packet_id'] or packet['coverage'] != {
                'patch_complete':True,'requested_context_complete':True,'omissions':[]}):
        raise ReviewBlocked('Documentation control source/packet/coverage mismatch')
    actual = execution_summaries(receipts, key=key, required_suites=['project'],
                                 candidate_digest=current_digest, environment_id=environment_id)
    if encoded(actual) != encoded(packet['execution']):
        raise ReviewBlocked('Documentation control execution mismatch')
    docs = review.get('checks', {}).get('documentation', {})
    if (docs.get('status') != 'consistent' or not isinstance(docs.get('evidence'), str) or
            not docs['evidence'].strip()):
        raise ReviewBlocked('Documentation check did not confirm consistency: '+str(docs.get('evidence', '')))
    for finding in review.get('findings', []):
        if finding.get('file') in packet['documentation_paths']:
            raise ReviewBlocked('Documentation check requests revision: '+str(finding))
    return True


class PublicationGate:
    def __init__(self, *, base, base_revision, record_root, engine_record_root,
                 image, endpoint, alias, phase_file, documentation_paths,
                 context_paths=(), caller_seconds=240, mode='full', max_attempts=4,
                 execute_factory=DockerExecution, input_measure=measure_input, max_rendered_tokens=10000):
        if mode not in {'full','docs_only_control'}:raise ValueError('Unknown comparison mode')
        self.base=dict(base); source_digest(self.base)
        self.base_revision=base_revision; self.root=Path(record_root); self.root.mkdir(parents=True,exist_ok=True)
        self.engine_root=engine_record_root; self.image=image; self.endpoint=endpoint; self.alias=alias
        self.phase_file=Path(phase_file); self.docs=list(documentation_paths); self.context=list(context_paths)
        self.caller_seconds=caller_seconds; self.mode=mode; self.max_attempts=max_attempts;self.execute_factory=execute_factory;self.input_measure=input_measure;self.max_rendered_tokens=max_rendered_tokens
        self.published={};self.attempts={};self.pending=None;self.active=None
        # Per-controller private key, never public fixture keys or actor-supplied data.
        self.key=os.urandom(32)
        descriptor=os.open(self.root/'receipt-key',os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
        with os.fdopen(descriptor,'wb') as file:file.write(self.key)

    def check(self, name, args):
        if name not in {'create_or_update_file','pull_request_write'}:return
        if self.active and not self.active.done.is_set():raise ReviewBlocked('Previous review capture still active; no duplicate request queued')
        self.pending=None
        phase=json.loads(self.phase_file.read_text())
        if not phase.get('active'):raise ReviewBlocked('Publication lease ended')
        current=apply_changes(self.base,self.published)
        change=mutation(args,current) if name=='create_or_update_file' else {}
        cumulative=dict(self.published);cumulative.update(change)
        proposed=apply_changes(self.base,cumulative)
        count=self.attempts.get(phase['id'],0)
        if count>=self.max_attempts:raise ReviewBlocked('Review allowance exhausted; publication remains blocked')
        self.attempts[phase['id']]=count+1
        attempt=uuid.uuid4().hex;root=self.root/attempt;source=root/'source';source.mkdir(parents=True)
        for path,content in proposed.items():
            target=source/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(content.encode())
        engine_source=self.engine_root+'/'+attempt+'/source'
        executor=self.execute_factory(source,engine_source,self.image)
        digest=source_digest(executor.inventory())
        receipt=executor.run(expected_digest=digest,key=self.key)
        (root/'receipt.json').write_bytes(encoded(receipt))
        try:evidence=execution_summaries([receipt],key=self.key,required_suites=['project'],candidate_digest=digest,environment_id=self.image)
        except ReviewBlocked as error:raise ReviewBlocked(str(error)+'; actual suite output: '+receipt['payload']['output_tail']) from error
        metadata={'operation':name}
        for field in ['owner','repo','branch_name','title','body','message','head','base']:
            if field in args:metadata[field]=args[field]
        packet=build_packet(tasks=phase['tasks_so_far'],base_revision=self.base_revision,
                            base=self.base,changes=cumulative,context_paths=self.context,
                            documentation_paths=self.docs,execution=evidence,publication=metadata)
        (root/'packet.json').write_bytes(encoded(packet))
        body=request_body(packet,self.alias)
        metrics=self.input_measure(self.endpoint,body)
        metrics['packet_bytes']=len(encoded(packet));metrics['output_reserve']=body['max_tokens']
        (root/'input-metrics.json').write_bytes(encoded(metrics))
        if (metrics['rendered_tokens']>self.max_rendered_tokens or
                metrics['rendered_tokens']+body['max_tokens']>=metrics['context']):
            raise ReviewBlocked('Rendered reviewer input exceeds configured bound/reserve')
        timed=TimedReview(self.endpoint,body,root/'http',caller_seconds=self.caller_seconds).start()
        self.active=timed
        caller=timed.caller_result()
        review=publication_review(caller)
        observed=(caller['capture'].get('usage')or{}).get('prompt_tokens')
        if (not isinstance(observed,int) or observed>self.max_rendered_tokens or
                observed+body['max_tokens']>=metrics['context']):
            raise ReviewBlocked('Actual reviewer usage does not verify the input bound/reserve')
        kwargs=dict(receipts=[receipt],key=self.key,current_digest=source_digest(executor.inventory()),environment_id=self.image)
        try:
            if self.mode=='full':admission(packet,review,required_suites=['project'],**kwargs)
            else:docs_only_admission(packet,review,**kwargs)
        except ReviewBlocked as error:
            feedback=review if self.mode=='full' else {'documentation':review.get('checks',{}).get('documentation',{}),'findings':[f for f in review.get('findings',[]) if f.get('file') in self.docs]}
            raise ReviewBlocked(str(error)+'; automatic review feedback: '+json.dumps(feedback)) from error
        (root/'admitted.json').write_bytes(encoded({'mode':self.mode,'operation':name,'phase':phase['id'],'packet_id':packet['packet_id'],'source_digest':digest}))
        self.pending=(name,encoded(args),cumulative)

    def after(self,name,args):
        if name not in {'create_or_update_file','pull_request_write'}:return
        if not self.pending or self.pending[:2] != (name,encoded(args)):
            raise ReviewBlocked('Successful remote mutation lacks matching admitted payload')
        if name=='create_or_update_file':self.published=self.pending[2]
        self.pending=None

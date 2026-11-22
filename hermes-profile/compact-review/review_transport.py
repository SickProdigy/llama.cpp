"""Timed nonstreaming review with durable complete-body capture after caller expiry."""
import hashlib
import http.client
import urllib.error
import json
from pathlib import Path
import threading
import time
import urllib.request
from review_packet import SYSTEM, encoded


def response_schema(packet_id):
    finding = {'type':'object','properties':{k:{'type':'string'} for k in ['file','issue','evidence']},
               'required':['file','issue','evidence'],'additionalProperties':False}
    def check(values):
        return {'type':'object','properties':{'status':{'type':'string','enum':values},'evidence':{'type':'string'}},
                'required':['status','evidence'],'additionalProperties':False}
    return {'type':'object','properties':{'packet_id':{'type':'string','enum':[packet_id]},
        'decision':{'type':'string','enum':['approve','revise','needs_context']},
        'findings':{'type':'array','items':finding},'checks':{'type':'object','properties':{
            'tests':check(['adequate','inadequate','unknown']),
            'documentation':check(['consistent','inconsistent','not_applicable','unknown'])},
            'required':['tests','documentation'],'additionalProperties':False}},
        'required':['packet_id','decision','findings','checks'],'additionalProperties':False}


def request_body(packet, alias, *, structured=True, max_tokens=1024, seed=20261122):
    body = {'model':alias,'messages':[{'role':'system','content':SYSTEM},
            {'role':'user','content':encoded(packet).decode()}],
            'temperature':0.8,'top_p':1.0,'top_k':0,'min_p':0.0,'repeat_penalty':1.0,
            'presence_penalty':0.0,'chat_template_kwargs':{'enable_thinking':False},
            'max_tokens':max_tokens,'seed':seed,'stream':False}
    if structured:
        body['response_format']={'type':'json_schema','json_schema':{
            'name':'compact_review','strict':True,'schema':response_schema(packet['packet_id'])}}
    return body


class TimedReview:
    """Caller expiry never grants approval and never discards a later full body.

    Calibration joins capture before another case. A publication adapter must
    return denial at caller expiry; a late decision cannot turn it into approval.
    Socket timeout bounds stalled reads, not a guaranteed total backend deadline.
    The detached stage controller enforces the final overall guard/restoration.
    """
    def __init__(self, endpoint, body, record_root, *, caller_seconds=240, socket_seconds=600):
        self.endpoint=endpoint;self.body=body;self.root=Path(record_root);self.root.mkdir(parents=True)
        self.caller_seconds=caller_seconds;self.socket_seconds=socket_seconds
        self.started=time.time();self.done=threading.Event();self.record=None
        self.thread=threading.Thread(target=self._capture,daemon=True)

    def _capture(self):
        raw=b'';record={'started_epoch':self.started,'request_sha256':hashlib.sha256(encoded(self.body)).hexdigest()}
        (self.root/'request.json').write_bytes(encoded(self.body))
        try:
            req=urllib.request.Request(self.endpoint,data=encoded(self.body),headers={'Content-Type':'application/json'})
            chunks=[]
            with urllib.request.urlopen(req,timeout=self.socket_seconds) as response:
                expected=response.headers.get('Content-Length')
                try:
                    while True:
                        chunk=response.read1(65536)
                        if not chunk: break
                        chunks.append(chunk)
                except http.client.IncompleteRead as error:
                    chunks.append(error.partial);raise
                finally:
                    raw=b''.join(chunks)
                if expected is not None and len(raw)!=int(expected):
                    raise ValueError('Incomplete response body')
            record['body_complete']=True
            reply=json.loads(raw)
            record['usage']=reply.get('usage');record['timings']=reply.get('timings')
            choice=reply['choices'][0];record['finish_reason']=choice.get('finish_reason')
            content=choice['message'].get('content')
            record['raw_model_content']=content
            try: record['parsed_review']=json.loads(content)
            except (ValueError,TypeError) as error: record['review_parse_error']=type(error).__name__
        except urllib.error.HTTPError as error:
            raw=error.read();record['http_status']=error.code;record['body_complete']=True
            record['error']='HTTPError: '+str(error.code)
        except Exception as error:
            record['error']=type(error).__name__+': '+str(error)
            record.setdefault('body_complete',False)
        finally:
            record['ended_epoch']=time.time();record['backend_http_seconds']=round(record['ended_epoch']-self.started,6)
            record['captured_bytes']=len(raw);record['response_sha256']=hashlib.sha256(raw).hexdigest()
            (self.root/'response.bin').write_bytes(raw)
            (self.root/'capture.json').write_text(json.dumps(record,indent=2)+'\n')
            self.record=record;self.done.set()

    def start(self): self.thread.start();return self

    def caller_result(self):
        completed=self.done.wait(self.caller_seconds)
        result={'caller_completed':completed,'caller_seconds':round(time.time()-self.started,6),
                'caller_limit_seconds':self.caller_seconds,'late_feedback_cannot_authorize':True}
        if completed:
            result['capture']=self.record
        else:
            result['error']='caller_deadline'
        (self.root/'caller.json').write_text(json.dumps(result,indent=2)+'\n')
        return result

    def join_capture(self, seconds=620):
        if not self.done.wait(seconds): raise TimeoutError('Capture still active; inspect same request, do not replay')
        return self.record


def publication_review(caller):
    """Only a complete in-deadline nontruncated response may reach admission."""
    from review_packet import ReviewBlocked
    capture=caller.get('capture') or {}
    if (not caller.get('caller_completed') or not capture.get('body_complete') or
            capture.get('error') or capture.get('review_parse_error') or
            capture.get('finish_reason')!='stop' or not isinstance(capture.get('parsed_review'),dict)):
        raise ReviewBlocked('Reviewer transport did not deliver a complete in-deadline verdict')
    return capture['parsed_review']

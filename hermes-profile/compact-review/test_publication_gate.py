import json
import subprocess
import threading
from pathlib import Path
from unittest.mock import patch
import pytest
from publication_gate import PublicationGate, mutation, docs_only_admission
from review_packet import ReviewBlocked, run_suite, source_digest

class LocalSuite:
    def __init__(self,root,engine_root,image):self.root=Path(root);self.image=image
    def inventory(self):return {str(p.relative_to(self.root)):p.read_bytes().decode() for p in self.root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and '.pytest_cache' not in p.parts}
    def run(self,expected_digest,key):
        return run_suite(suite_id='project',argv=['python','-m','pytest','-q','-p','no:cacheprovider'],expected_digest=expected_digest,inventory=self.inventory,execute=lambda argv:subprocess.run(argv,cwd=self.root,capture_output=True,text=True),key=key,environment_id=self.image)

class Approved:
    calls=0
    def __init__(self,endpoint,body,root,**kw):
        self.packet=json.loads(body['messages'][1]['content']);self.done=threading.Event()
    def start(self):self.done.set();type(self).calls+=1;return self
    def caller_result(self):
        review={'packet_id':self.packet['packet_id'],'decision':'approve','findings':[],'checks':{'tests':{'status':'adequate','evidence':'Fixture tests exercise actual function.'},'documentation':{'status':'consistent','evidence':'README describes current function.'}}}
        return {'caller_completed':True,'capture':{'body_complete':True,'finish_reason':'stop','parsed_review':review,'usage':{'prompt_tokens':123}}}

def gate(tmp_path,mode='full'):
    phase=tmp_path/'phase.json';phase.write_text(json.dumps({'id':'turn0','active':True,'tasks_so_far':['Return the sum; document and test it.']}))
    base={'calc.py':'def add(a,b): return a+b\n','README.md':'Returns the sum.\n','test_calc.py':'from calc import add\ndef test_add(): assert add(2,3)==5\n'}
    return PublicationGate(base=base,base_revision='a'*40,record_root=tmp_path/'records',engine_record_root='/engine/records',image='sha256:test',endpoint='http://unused',alias='fixture',phase_file=phase,documentation_paths=['README.md'],execute_factory=LocalSuite,mode=mode,input_measure=lambda endpoint,body:{'rendered_tokens':123,'context':16384,'model_alias':body['model']})

def test_actual_payload_tests_not_scratch(tmp_path):
    g=gate(tmp_path);Approved.calls=0
    with patch('publication_gate.TimedReview',Approved):
        with pytest.raises(ReviewBlocked,match='actual suite output'):
            g.check('create_or_update_file',{'files':[{'path':'calc.py','content':'def add(a,b): return a-b\n'}]})
    assert Approved.calls==0 and not g.published

def test_success_matches_actual_remote_payload(tmp_path):
    g=gate(tmp_path);args={'files':[{'path':'README.md','content':'Returns the sum of both numbers.\n'}]}
    with patch('publication_gate.TimedReview',Approved):g.check('create_or_update_file',args)
    with pytest.raises(ReviewBlocked):g.after('create_or_update_file',{'files':[]})
    assert not g.published
    g.after('create_or_update_file',args)
    assert g.published['README.md']==args['files'][0]['content']

def test_control_still_rejects_false_docs(tmp_path):
    g=gate(tmp_path,mode='docs_only_control');args={'files':[{'path':'README.md','content':'Returns the sum.\n'}]}
    with patch('publication_gate.TimedReview',Approved):g.check('create_or_update_file',args)
    packet=json.loads(next((tmp_path/'records').glob('*/packet.json')).read_text())
    receipt=json.loads(next((tmp_path/'records').glob('*/receipt.json')).read_text())
    review={'packet_id':packet['packet_id'],'checks':{'documentation':{'status':'inconsistent','evidence':'False docs.'}}}
    for status,evidence in [('inconsistent','False docs.'),('consistent',True),('consistent','')]:
        review['checks']['documentation']={'status':status,'evidence':evidence}
        with pytest.raises(ReviewBlocked,match='Documentation check'):
            docs_only_admission(packet,review,receipts=[receipt],key=g.key,current_digest=packet['candidate_source_digest'],environment_id=g.image)

def test_ambiguous_and_private_paths_rejected():
    with pytest.raises(ReviewBlocked):mutation({'files':[{'path':'calc.py','edits':[{'old_string':'x','new_string':'y'}]}]},{'calc.py':'xx'})
    with pytest.raises(ReviewBlocked):mutation({'files':[{'path':'../auth.json','content':'bad'}]}, {})
    with pytest.raises(ReviewBlocked):mutation({'files':[{'path':'new.py','from_path':'old.py','content':'new'}]}, {'old.py':'old'})

def test_pending_review_never_queues_duplicate(tmp_path):
    g=gate(tmp_path);g.active=type('Active',(),{'done':threading.Event()})()
    with pytest.raises(ReviewBlocked,match='still active'):g.check('pull_request_write',{})
    assert not g.attempts


def test_rendered_bound_blocks_before_reviewer(tmp_path):
    g=gate(tmp_path);g.input_measure=lambda endpoint,body:{'rendered_tokens':10001,'context':16384}
    Approved.calls=0
    with patch('publication_gate.TimedReview',Approved):
        with pytest.raises(ReviewBlocked,match='Rendered reviewer input'):
            g.check('create_or_update_file',{'files':[{'path':'README.md','content':'Returns the sum.\n'}]})
    assert Approved.calls==0 and not g.published

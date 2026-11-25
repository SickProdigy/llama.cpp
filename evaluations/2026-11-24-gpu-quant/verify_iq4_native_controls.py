"""Coherent corruption controls on saved evidence, not additional model trials."""
from pathlib import Path
import hashlib,io,json,subprocess,sys,tarfile,tempfile
archive=Path(sys.argv[1]).resolve();verify=Path(__file__).with_name('verify_iq4_native.py');sha=lambda b:hashlib.sha256(b).hexdigest();run=lambda p:subprocess.run([sys.executable,str(verify),str(p)],capture_output=True,text=True)
positive=run(archive);assert positive.returncode==0,positive.stderr
with tarfile.open(archive)as tar:original={m.name:tar.extractfile(m).read()for m in tar}
results=[]
for case in ['hidden_auxiliary_failure','false_feature_success','wrong_native_resume_handle','false_zero_host_model_memory']:
 files=dict(original);read=lambda p:json.loads(files[p])
 def put(p,x):files[p]=(json.dumps(x,indent=2)+'\n').encode()
 summary=read('summary.json');final=read('audits/adapted-iq4-beets-final-audit.json')
 if case=='hidden_auxiliary_failure':
  p='requests/00047.metrics.json';m=read(p);m['backend_body_complete']=True;m['transport_error_present']=False;put(p,m);context=read('audits/adapted-iq4-beets-context-instruction-audit.json');context['incomplete_HTTP_records']=[r for r in context['incomplete_HTTP_records']if r['metrics_file']!='00047.metrics.json'];context['completed_HTTP_records']+=1;put('audits/adapted-iq4-beets-context-instruction-audit.json',context);summary['measurements']['incomplete_HTTP_records']-=1;summary['measurements']['completed_HTTP_records_without_transport_error']+=1;summary['measurements']['incomplete_backend_seconds']-=m['end_epoch']-m['backend_start_epoch']
 elif case=='false_feature_success':
  p='audits/adapted-iq4-beets-feature-manual-audit.json';a=read(p);a['feature_completed']=a['requested_task_completed']=True;put(p,a);final['feature_completed']=final['overall_workflow_completed_correctly']=True
 elif case=='wrong_native_resume_handle':
  p='phases/2/run.json';r=read(p);r['native_session_fingerprints']['cli_resume_handle']=r['native_session_fingerprints']['effective_sid'];put(p,r);summary['phases'][2]['native_session_fingerprints']=r['native_session_fingerprints'];p='audits/adapted-iq4-beets-context-instruction-audit.json';context=read(p);row=next(r for r in context['phases']if r['phase']==2);row['CLI_resume_handle_SHA256']=row['physical_effective_SID_SHA256'];put(p,context)
 else:
  p='runtime/initial-buffer-placement-breakdown.json';b=read(p)
  for row in b['buffers']:
   if row['backend']=='CUDA_Host'and row['kind']=='model':row['MiB']=0
  b['exact_buffer_lines']=[l.replace('644.14','0.00')for l in b['exact_buffer_lines']];put(p,b)
 mapping={'native-adapted-iq4-beets-cleanup.json':'audits/cleanup.json','iq4-context-semantic-audit.json':'controls/context-semantic-audit.json','iq4-compression-runtime-diagnosis.json':'controls/actual-compression-timeout-diagnosis.json','iq4-buffer-placement-breakdown.json':'runtime/initial-buffer-placement-breakdown.json','iq4-test-helper-accounting-audit.json':'runtime/test-helper-accounting.json','aux-budget-getter-controls.json':'controls/aux-budget-getter-controls.json'}
 for name in final['evidence_SHA256']:
  target=mapping.get(name,('controls/'if '-test-adequacy/'in name else'audits/')+name);final['evidence_SHA256'][name]=sha(files[target])
 put('audits/adapted-iq4-beets-final-audit.json',final);summary['independent_final_audit']=final;put('summary.json',summary);put('manifest.json',{p:sha(raw)for p,raw in files.items()if p!='manifest.json'})
 with tempfile.TemporaryDirectory()as t:
  path=Path(t)/'changed.tar.gz'
  with tarfile.open(path,'w:gz')as tar:
   for name,raw in files.items():m=tarfile.TarInfo(name);m.size=len(raw);tar.addfile(m,io.BytesIO(raw))
  result=run(path);assert result.returncode!=0,(case,result.stdout)
 results.append({'case':case,'summary_audit_bindings_and_manifest_updated':True,'rejected':True})
print(json.dumps({'passed':True,'actual_positive_accepted':True,'not_model_trials':True,'negative_controls':results,'original_archive_unchanged_SHA256':sha(archive.read_bytes())}))

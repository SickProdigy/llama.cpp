"""Artifact consistency controls only; no model inference or private behavior tests."""
from pathlib import Path
import json,hashlib,tarfile,io,tempfile,shutil,subprocess,sys
E=Path(__file__).resolve().parent;sha=lambda b:hashlib.sha256(b).hexdigest();encoded=lambda x:(json.dumps(x,indent=2)+'\n').encode();label='native-q4fresh-spam';archive=E/(label+'-evidence.tar.gz');verifier=E/'verify_q4fresh_native_observed.py'
original_sha=sha(archive.read_bytes());assert original_sha==(E/(label+'-evidence.sha256')).read_text().split()[0]
with tarfile.open(archive)as t:original={m.name:t.extractfile(m).read()for m in t.getmembers()}
def final_audit(files,audit):
 files['audits/q4fresh-spam-final-audit.json']=encoded(audit);summary=json.loads(files['summary.json']);summary['independent_final_audit']=audit;files['summary.json']=encoded(summary)
def wrong_manual_source(files):
 name='audits/q4fresh-spam-initial-manual-audit.json';manual=json.loads(files[name]);manual['source_sha256']['autospamignore/__init__.py']='0'*64;files[name]=encoded(manual);audit=json.loads(files['audits/q4fresh-spam-final-audit.json']);audit['manual_audit_sha256']['q4fresh-spam-initial-manual-audit.json']=sha(files[name]);final_audit(files,audit)
def wrong_adequacy_source(files):
 name='controls/q4fresh-spam_enforcement-phase0-test-adequacy/published/source-sha256.json';mapping=json.loads(files[name]);mapping['autospamignore/__init__.py']='0'*64;files[name]=encoded(mapping)
def wrong_context_source(files):
 name='audits/q4fresh-spam-context-instruction-audit.json';context=json.loads(files[name]);context['phases'][2]['saved_request_JSON_sha256']='0'*64;files[name]=encoded(context);audit=json.loads(files['audits/q4fresh-spam-final-audit.json']);audit['posthoc_control_sha256']['q4fresh-spam-context-instruction-audit.json']=sha(files[name]);final_audit(files,audit)
def negative(name,mutate,target_check,root):
 files=dict(original);mutate(files);manifest=json.loads(files['manifest.json']);manifest['sha256']={n:sha(b)for n,b in files.items()if n!='manifest.json'};files['manifest.json']=encoded(manifest);case=root/name;case.mkdir();target=case/archive.name
 with tarfile.open(target,'w:gz')as t:
  for n,b in sorted(files.items()):
   info=tarfile.TarInfo(n);info.size=len(b);t.addfile(info,io.BytesIO(b))
 (case/(label+'-evidence.sha256')).write_text(sha(target.read_bytes())+'  '+target.name+'\n');(case/(label+'-summary.json')).write_bytes(files['summary.json']);shutil.copyfile(verifier,case/verifier.name);r=subprocess.run([sys.executable,str(case/verifier.name),'q4fresh','spam_enforcement'],capture_output=True,text=True,timeout=60);assert r.returncode!=0 and'AssertionError'in r.stderr and target_check in r.stderr,(name,r.stdout,r.stderr)
 return{'name':name,'rejected':True,'exit_code':r.returncode,'manifest_archive_and_relevant_audit_summary_hashes_recomputed':True,'targeted_binding_check_reached':target_check}
positive=subprocess.run([sys.executable,str(verifier),'q4fresh','spam_enforcement'],capture_output=True,text=True,timeout=60);assert positive.returncode==0,(positive.stdout,positive.stderr)
with tempfile.TemporaryDirectory(prefix='q4fresh-artifact-controls-')as tmp:
 root=Path(tmp);cases=[negative('manual_audit_wrong_source',wrong_manual_source,'snapshot[path]==digest',root),negative('adequacy_control_wrong_candidate_source',wrong_adequacy_source,'candidate==j(',root),negative('context_audit_wrong_saved_request',wrong_context_source,'saved_request_JSON_sha256',root)];legacy=[]
 for key in ['devstral','glm']:
  case=root/('legacy-'+key);case.mkdir();prefix='native-'+key+'-spam';prior=E/(prefix+'-evidence.tar.gz');before=sha(prior.read_bytes())
  for suffix in ['-evidence.tar.gz','-evidence.sha256','-summary.json']:shutil.copyfile(E/(prefix+suffix),case/(prefix+suffix))
  oldverifier=E/'verify_candidate_native_observed.py';shutil.copyfile(oldverifier,case/oldverifier.name);r=subprocess.run([sys.executable,str(case/oldverifier.name),key,'spam_enforcement'],capture_output=True,text=True,timeout=60);assert r.returncode==0,(r.stdout,r.stderr);assert sha(prior.read_bytes())==before;legacy.append({'candidate':key,'accepted_by_unchanged_generic_verifier':True,'archive_unchanged':True,'archive_sha256':before})
result={'passed':True,'kind':'artifact_consistency_controls_not_model_trials','actual_Q4_positive_accepted':True,'negative_cases':cases,'legacy_observed_archives':legacy,'original_Q4_archive_unchanged':sha(archive.read_bytes())==original_sha,'verifier_sha256':sha(verifier.read_bytes()),'control_source_sha256':sha(Path(__file__).read_bytes()),'limits':'These checks validate recorded byte associations only; they do not rerun model inference, private behavior checks or remote publication audits.'};(E/(label+'-verifier-controls.json')).write_bytes(encoded(result));print(json.dumps(result))

"""Coherent artifact mutations test the verifier, not the model."""
from pathlib import Path
import copy,hashlib,io,json,subprocess,sys,tarfile,tempfile
archive=Path(sys.argv[1]).resolve();verifier=Path(__file__).with_name('verify_native.py')
run=lambda p:subprocess.run([sys.executable,str(verifier),str(p)],capture_output=True,text=True)
positive=run(archive);assert positive.returncode==0,positive.stderr
with tarfile.open(archive)as tar:original={m.name:tar.extractfile(m).read()for m in tar}
summary=json.loads(original['summary.json']);key=summary['candidate_key'];results=[]
def write(files,name,value):files[name]=(json.dumps(value,indent=2)+'\n').encode()
def update_audit(files,name,value):
    write(files,'audits/'+name,value)
    final_name='audits/'+key+'-beets-final-audit.json';final=json.loads(files[final_name])
    final['evidence_SHA256'][name]=hashlib.sha256(files['audits/'+name]).hexdigest();write(files,final_name,final)
    s=json.loads(files['summary.json']);s['independent_final_audit']=final;write(files,'summary.json',s)
cases=[('manual_wrong_source','audit[\'source_SHA256\']'),('context_wrong_request','private_saved_request_file_SHA256')]
if 'controls/'+key+'-beets_lifecycle-phase2-test-adequacy/candidate/source-sha256.json'in original:cases.append(('authored_control_wrong_source','candidate/source-sha256.json'))
for case,target in cases:
    files=dict(original)
    if case=='manual_wrong_source':
        name=key+'-beets-initial-manual-audit.json';value=json.loads(files['audits/'+name]);value['source_SHA256']['beetsbridge/__init__.py']='0'*64;update_audit(files,name,value)
    elif case=='context_wrong_request':
        name=key+'-beets-context-instruction-audit.json';value=json.loads(files['audits/'+name]);value['phases'][0]['saved_request_JSON_sha256']='0'*64;update_audit(files,name,value)
    else:
        name='controls/'+key+'-beets_lifecycle-phase2-test-adequacy/candidate/source-sha256.json';value=json.loads(files[name]);value['beetsbridge/__init__.py']='0'*64;write(files,name,value)
    manifest=json.loads(files['manifest.json'])
    for name in manifest:manifest[name]=hashlib.sha256(files[name]).hexdigest()
    write(files,'manifest.json',manifest)
    with tempfile.TemporaryDirectory()as temporary:
        bad=Path(temporary)/(case+'.tar.gz')
        with tarfile.open(bad,'w:gz')as tar:
            for name,raw in files.items():
                info=tarfile.TarInfo(name);info.size=len(raw);tar.addfile(info,io.BytesIO(raw))
        outcome=run(bad);assert outcome.returncode!=0 and target in outcome.stderr,(case,outcome.stderr)
        results.append({'case':case,'coherent_manifest_and_audit_references_updated':True,'rejected':True,'exit_code':outcome.returncode})
print(json.dumps({'passed':True,'kind':'artifact_consistency_controls_not_model_trials','actual_positive_accepted':True,'negative_controls':results,'original_archive_unchanged_SHA256':hashlib.sha256(archive.read_bytes()).hexdigest()}))

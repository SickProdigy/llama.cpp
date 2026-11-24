"""Public artifact-format controls; no inference or private model grading."""
from pathlib import Path
import hashlib,json,tarfile,io,tempfile,shutil,subprocess,sys
E=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def encoded(x):return (json.dumps(x,indent=2)+'\n').encode()
archive=E/'native-glm-spam-evidence.tar.gz'
with tarfile.open(archive)as t:
    original={m.name:t.extractfile(m).read()for m in t.getmembers()}
assert sha(archive.read_bytes())==(E/'native-glm-spam-evidence.sha256').read_text().split()[0]
verifier=E/'verify_candidate_native_observed.py'
def negative(label,mutate,root):
    files=dict(original)
    mutate(files)
    manifest=json.loads(files['manifest.json'])
    manifest['sha256']={n:sha(b)for n,b in files.items()if n!='manifest.json'}
    files['manifest.json']=encoded(manifest)
    case=root/label
    case.mkdir()
    target=case/archive.name
    with tarfile.open(target,'w:gz')as t:
        for n,b in sorted(files.items()):
            info=tarfile.TarInfo(n)
            info.size=len(b)
            t.addfile(info,io.BytesIO(b))
    (case/'native-glm-spam-evidence.sha256').write_text(sha(target.read_bytes())+'  '+target.name+'\n')
    (case/'native-glm-spam-summary.json').write_bytes(files['summary.json'])
    shutil.copyfile(verifier,case/verifier.name)
    r=subprocess.run([sys.executable,str(case/verifier.name),'glm','spam_enforcement'],capture_output=True,text=True,timeout=60)
    assert r.returncode!=0 and 'AssertionError'in r.stderr,(label,r.stdout,r.stderr)
    return {'name':label,'rejected':True,'exit_code':r.returncode,'manifest_and_archive_hashes_recomputed':True}
def set_audit(files,audit):
    files['audits/glm-spam-final-audit.json']=encoded(audit)
    summary=json.loads(files['summary.json'])
    summary['independent_final_audit']=audit
    files['summary.json']=encoded(summary)
def bad_feature_source(files):
    name='controls/glm-spam-feature-supplementary/result.json'
    control=json.loads(files[name])
    control['source_sha256']['autospamignore/__init__.py']='0'*64
    files[name]=encoded(control)
    manual_name='audits/glm-spam-feature-manual-audit.json'
    manual=json.loads(files[manual_name])
    manual['posthoc_feature_result_sha256']=sha(files[name])
    files[manual_name]=encoded(manual)
    audit=json.loads(files['audits/glm-spam-final-audit.json'])
    audit['manual_audit_sha256']['glm-spam-feature-manual-audit.json']=sha(files[manual_name])
    audit['posthoc_control_sha256']['glm-spam-feature-supplementary-control/result.json']=sha(files[name])
    set_audit(files,audit)
def bad_context_source(files):
    name='audits/glm-spam-context-instruction-audit.json'
    context=json.loads(files[name])
    context['phases'][2]['saved_request_JSON_sha256']='0'*64
    files[name]=encoded(context)
    audit=json.loads(files['audits/glm-spam-final-audit.json'])
    audit['posthoc_control_sha256']['glm-spam-context-instruction-audit.json']=sha(files[name])
    set_audit(files,audit)
with tempfile.TemporaryDirectory(prefix='glm-native-artifact-controls-')as tmp:
    root=Path(tmp)
    cases=[negative('feature_control_wrong_source',bad_feature_source,root),negative('context_audit_wrong_request',bad_context_source,root)]
    legacy=root/'legacy'
    legacy.mkdir()
    names=['native-devstral-spam-evidence.tar.gz','native-devstral-spam-evidence.sha256','native-devstral-spam-summary.json']
    for n in names:shutil.copyfile(E/n,legacy/n)
    shutil.copyfile(verifier,legacy/verifier.name)
    r=subprocess.run([sys.executable,str(legacy/verifier.name),'devstral','spam_enforcement'],capture_output=True,text=True,timeout=60)
    assert r.returncode==0,(r.stdout,r.stderr)
result={'passed':True,'kind':'artifact_consistency_controls_not_model_trials','negative_cases':cases,'legacy_Devstral_observed_outcome_still_accepted':True,'GLM_original_archive_unchanged':sha(archive.read_bytes())==(E/'native-glm-spam-evidence.sha256').read_text().split()[0],'verifier_sha256':sha(verifier.read_bytes()),'control_source_sha256':sha(Path(__file__).read_bytes()),'limits':'These checks do not rerun model inference, private behavior tests or independent publication audits.'}
(E/'native-glm-spam-verifier-controls.json').write_bytes(encoded(result))
print(json.dumps(result))


"""Exercise the saved-observation verifier; these are not model trials."""
from pathlib import Path
import hashlib, io, json, subprocess, sys, tarfile, tempfile
archive=Path(sys.argv[1]).resolve()
verifier=Path(__file__).with_name('verify_reasoning_resource.py')
positive=subprocess.run([sys.executable,str(verifier),str(archive)],capture_output=True,text=True)
assert positive.returncode==0,positive.stderr
with tarfile.open(archive) as tar:
    files={m.name:tar.extractfile(m).read() for m in tar.getmembers()}
summary=json.loads(files['summary.json']);summary['peak_gpu_MiB']+=1
files['summary.json']=(json.dumps(summary,indent=2)+'\n').encode()
manifest=json.loads(files['manifest.json'])
manifest['summary.json']=hashlib.sha256(files['summary.json']).hexdigest()
files['manifest.json']=(json.dumps(manifest,indent=2)+'\n').encode()
with tempfile.TemporaryDirectory() as temporary:
    bad=Path(temporary)/'coherent-wrong-GPU-summary.tar.gz'
    with tarfile.open(bad,'w:gz') as tar:
        for name,raw in files.items():
            info=tarfile.TarInfo(name);info.size=len(raw)
            tar.addfile(info,io.BytesIO(raw))
    negative=subprocess.run([sys.executable,str(verifier),str(bad)],capture_output=True,text=True)
    assert negative.returncode!=0 and 'peak_gpu_MiB' in negative.stderr
print(json.dumps({'passed':True,'kind':'artifact_consistency_controls_not_model_trials','actual_positive_accepted':True,'coherent_wrong_GPU_summary_rejected':True,'manifest_hash_updated_in_negative_control':True,'archive_unchanged_SHA256':hashlib.sha256(archive.read_bytes()).hexdigest()}))

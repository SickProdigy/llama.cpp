from pathlib import Path
import copy,hashlib,io,json,subprocess,sys,tarfile,tempfile
archive=Path(sys.argv[1]).resolve();verify=Path(__file__).with_name('verify_iq4_resource.py');run=lambda p:subprocess.run([sys.executable,str(verify),str(p)],capture_output=True,text=True)
positive=run(archive);assert positive.returncode==0,positive.stderr
with tarfile.open(archive)as tar:original={m.name:tar.extractfile(m).read()for m in tar}
results=[]
for case in ['wrong_GPU_summary','hidden_failed_layout','wrong_staging_reserve']:
 files=dict(original);s=json.loads(files['summary.json'])
 if case=='wrong_GPU_summary':s['layouts'][-1]['peak_GPU_MiB']+=1
 elif case=='hidden_failed_layout':s['layouts'][0]['result']['GPU_OOM_log_marker']=False
 else:s['layouts'][-1]['minimum_staging_disk_free_bytes']=100*1024**3
 files['summary.json']=(json.dumps(s,indent=2)+'\n').encode();m=json.loads(files['manifest.json'])
 for name in m:m[name]=hashlib.sha256(files[name]).hexdigest()
 files['manifest.json']=(json.dumps(m,indent=2)+'\n').encode()
 with tempfile.TemporaryDirectory()as t:
  p=Path(t)/'bad.tar.gz'
  with tarfile.open(p,'w:gz')as tar:
   for name,raw in files.items():i=tarfile.TarInfo(name);i.size=len(raw);tar.addfile(i,io.BytesIO(raw))
  r=run(p);assert r.returncode!=0,(case,r.stdout);results.append({'case':case,'coherent_manifest_updated':True,'rejected':True})
print(json.dumps({'passed':True,'actual_positive_accepted':True,'not_model_trials':True,'negative_controls':results,'original_archive_unchanged_SHA256':hashlib.sha256(archive.read_bytes()).hexdigest()}))

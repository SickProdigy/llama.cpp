"""Replay saved interruption evidence, not inference or code quality."""
from pathlib import Path,PurePosixPath
import sys,json,hashlib,tarfile
p=Path(sys.argv[1]);sha=lambda b:hashlib.sha256(b).hexdigest();files={}
with tarfile.open(p)as t:
 for m in t:
  n=PurePosixPath(m.name);assert m.isfile()and not n.is_absolute()and'..'not in n.parts and m.name not in files;files[m.name]=t.extractfile(m).read()
read=lambda n:json.loads(files[n]);manifest=read('manifest.json');assert set(files)==set(manifest)|{'manifest.json'}
for n,h in manifest.items():assert sha(files[n])==h
s=read('summary.json');rows=read('observations/memory.json');metrics=read('observations/request-metrics.json');guards=[r for r in rows if r.get('budget_guard_triggered')]
assert s['quality_verdict']is None and s['completed_coding_turns']==0
assert len(rows)==s['samples']and len(guards)==1 and guards[0]==s['guard'];g=guards[0]
assert g['disk_reserve_guard_triggered']and g['staging_disk_free_bytes']<s['reserve_bytes']<=g['model_disk_free_bytes']
assert all(r['staging_disk_free_bytes']>=s['reserve_bytes']for r in rows if r is not g)
assert max(r['total_cgroup_bytes']for r in rows)==s['peak_aggregate_cgroup_bytes']<=s['host_limit_bytes']
assert max(r['total_process_pss_bytes']for r in rows)==s['peak_PSS_bytes']<=s['host_limit_bytes']
assert max(r['total_cgroup_swap_bytes']for r in rows)==s['peak_study_swap_bytes']==0
assert sum('measurement_error'in r for r in rows)==s['measurement_errors']==0
good=[m for m in metrics if m.get('usage')];bad=[m for m in metrics if not m.get('usage')];assert len(good)==s['usage_completed_requests']==14 and len(bad)==s['failed_requests_after_guard']==5
assert all(m['end_epoch']>=g['epoch']for m in bad)
assert all(m['usage']['total_tokens']<=s['context']for m in good)
assert s['preservation']['passed']and s['owner_preservation']['passed']and s['cleanup']['passed']
assert s['publication']['issue_closed_independently_verified']and s['publication']['actual_personal_fork_parent_verified']and s['publication']['upstream_baseline_blobs_verified']==40
state=read('observations/terminal-state.json');assert state['Status']=='exited'and not state['OOMKilled']
print(json.dumps({'passed':True,'archive_SHA256':sha(p.read_bytes()),'manifest_files':len(manifest),'classification':s['classification'],'quality_verdict':None,'not_a_model_pass_or_fail':True}))

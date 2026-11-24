"""Verify saved posthoc comparison fingerprints, not GUI behavior or reliability."""
from pathlib import Path
import json,tarfile,hashlib
E=Path(__file__).resolve().parent;sha=lambda b:hashlib.sha256(b).hexdigest();x=json.loads((E/'announcer-dispatch-cleanup-comparison.json').read_text());assert x['not_actor_feedback']and x['frozen_grades_unchanged'];out=[]
for row in x['candidates']:
 arc=E/row['evidence_archive'];assert sha(arc.read_bytes())==row['archive_sha256']==(E/(arc.name.replace('.tar.gz','.sha256'))).read_text().split()[0]
 with tarfile.open(arc)as t:
  fingerprints=json.load(t.extractfile('phases/2/'+row['source_kind']+'/source-sha256.json'))
  if row['candidate']=='devstral':assert sha(t.extractfile('source/announcer_dispatch_cleanup_control.py').read())==x['same_control_source_sha256']
 assert fingerprints['announcer/__init__.py']==row['source_sha256'];assert row['control_sha256']==x['same_control_source_sha256'];pins={p['commit']:p for p in x['upstream_pins']if 'commit'in p}
 for result in row['results']:
  pin=pins[result['commit']];assert result['upstream_source_sha256']==pin['sha256']and result['upstream_url']==pin['url']
  out.append({'candidate':row['candidate'],'upstream_ref':result['requested_ref'],'argument_accepted':result['selective_with_surviving_target']['actual_upstream_dispatch_accepted_room_argument'],'orphaned_reply_entries':result['cancelling_last_target_of_job']['reply_entries_after_cancelling_only_target']})
r={'passed':True,'source_fingerprints_checked':True,'dispatch_not_reexecuted':True,'scope':'Recorded comparison consistency, not model quality or full GUI/network integration.','observations':out};(E/'announcer-dispatch-cleanup-validation.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))

"""Normalize delivered results without upgrading checks into behavior verdicts.

This reads completed public reports only; it neither reads nor modifies a live
actor. All included cells are independently audited; the Q3_K_M delivery is finalized with this update.
"""
from pathlib import Path
import hashlib,json,math,time,datetime
E=Path(__file__).resolve().parent
R=E.parent.parent
candidates=['adapted-q4-current','adapted-iq4-current-r2','adapted-iq3-current','adapted-q3km-current','fable-q4-current-thinking','fable-q5-current-thinking','fable-q6-current-thinking','fable-q8-thinking','vibe-q4-thinking','vibe-q6-thinking']
rows=[]
for candidate in candidates:
 p=E/('native-'+candidate+'-cold-beets-summary.json')
 x=json.loads(p.read_text());phases=x['phases'];assert len(phases)==3
 assert isinstance(x['whole_workflow_pass'],bool)
 assert math.isclose(sum(t['coding_seconds']for t in phases)/60,x['coding_minutes'],abs_tol=1e-8)
 resource=x['resource'];audit=x['runtime_audit']
 publication=x.get('publication');forge=x.get('forge')
 if publication is not None:
  if candidate=='adapted-q4-current':
   actions={k:publication[k]for k in ['actual_issue_created','actual_personal_fork_parent_verified','actual_PR_created_updated','issue_closed_after_test','PR_preserved_unmerged']}
  else:
   actions={'upstream_issue_observed':bool(publication['upstream_issue']),'personal_fork_parent_verified':publication['personal_fork_parent_verified'],'PR_observed':bool(publication['PR']),'PR_open_unmerged':publication['PR_open_unmerged'],'issue_closed_single_GET_verified':publication['issue_closed_single_get_verified']}
 else:
  actions={'actor_fork_GET_status':forge['actor_fork_GET_status'],'observed_issues_count':len(forge['issues']),'observed_PR_count':len(forge['pull_requests']),'empty_issue_list_is_not_closure_proof':True}
 rows.append({
  'candidate':candidate,'source':str(p.relative_to(R)),'source_SHA256':hashlib.sha256(p.read_bytes()).hexdigest(),
  'whole_workflow_pass':x['whole_workflow_pass'],
  'model':x['model'],
  'model_repository':x.get('model_repository'),
  'model_revision':x.get('model_revision'),
  'runtime_images':x.get('runtime_images'),
  'preservation':x.get('preservation'),
  'intervention':x.get('intervention'),
  'turn_minutes':[t['coding_seconds']/60 for t in phases],
  'total_coding_minutes':x['coding_minutes'],
  'supervisor_wall_minutes':x.get('supervisor_wall_minutes',x.get('supervisor_total_wall_minutes')),
  'turn_checks':[{'phase':t['phase'],'project_exit':t['project_exit'],'original_exit':t.get('original_exit',t.get('preservation_exit')),'registered_independent_exit':t['independent_exit'],'source_authority':t.get('source_authority','not stated in this summary'),'not_a_manual_behavior_verdict':True}for t in phases],
  'resource':{k:resource.get(k)for k in ['samples','peak_GPU_MiB','peak_aggregate_cgroup_bytes','peak_process_PSS_bytes','peak_study_swap_bytes','guards','measurement_errors','minimum_disk_free_bytes','minimum_staging_free_bytes']},
  'actual_buffer_placement_lines':resource['placement_lines'],
  'backend':{'completed_requests':audit.get('usage_completed_requests',audit.get('completed_requests')),'requested_calls':audit.get('requested_calls'),'failed_requests':audit.get('failed_backend_requests'),'largest_completed_prompt':audit['largest_completed_prompt'],'any_length_finish':audit['any_length_finish']},
  'publication':actions,
  'quant_or_runtime_qualification':x.get('qualification',x.get('comparability',x.get('restoration_qualification'))),
  'source_report_for_manual_findings':str(p.with_suffix('').with_name(p.name.replace('-summary.json','.md')).relative_to(R)),
 })
timing_source=E/'completed-current-quant-terminal-timings.json'
timing_data=json.loads(timing_source.read_text())
for observed in timing_data['observations']:
 state=observed['terminal_state'];dt=lambda x:datetime.datetime.fromisoformat(x.replace('Z','+00:00'))
 minutes=(dt(state['FinishedAt'])-dt(state['StartedAt'])).total_seconds()/60
 assert state['Status']=='exited'and not state['Running']and not state['OOMKilled']and state['ExitCode']==0
 assert math.isclose(minutes,observed['supervisor_wall_minutes'],abs_tol=1e-9)
 assert observed['matching_recorded_launch_receipts']and all(r['id']==observed['container_id']for r in observed['matching_recorded_launch_receipts'])
 row=next(r for r in rows if r['candidate']==observed['candidate']);assert minutes>row['total_coding_minutes']
 assert math.isclose(observed['coding_minutes'],row['total_coding_minutes'],abs_tol=1e-9)
 if row['supervisor_wall_minutes']is not None:assert math.isclose(minutes,row['supervisor_wall_minutes'],abs_tol=1e-9)
 row['supervisor_wall_minutes']=minutes
 row['wall_observation_source']=str(timing_source.relative_to(R))
 row['wall_observation_source_SHA256']=hashlib.sha256(timing_source.read_bytes()).hexdigest()
out={'scope':'Only already delivered completed current-runtime Beets workflows; IQ3, Q5 and Q3_K_M included after independent source/behavior/publication audits. Three dependent turns constitute one workflow per cell, not three independent trials.','rows':rows,'paired_comparison_qualifications':{
 'Fable Q4/Q5/Q6/Q8':'Same current evaluator/backend/transparent recorder, reasoning sampler and context; none of these four full workflows passes. Single observations, not precision-only causality or reliability.',
 'Vibe Q4/Q6':'Both use the earlier recorder; Q6 final context400 was masked as502. Earlier independent code failures remain; final feature score is confounded.',
 'Adapted IQ3/Q3_K_M/Q4/IQ4':'Same current evaluator/backend/transparent recorder and nonthinking sampler/caps. Q3_K_M actual initial33schemas/seed/caps match IQ3/IQ4; its published worker is unchanged and rejected proposals also fail preserved normal-import behavior. Quant production/calibration, measured layer placement/host spillover and ubatch differ. IQ4 full Codex-state check failed on a start timestamp change of unknown cause; its qualified restoration is retained.',
 },'missing_values':'null means not present in the supplied public summary, never an assumed zero or successful check.','interpretation':'No runtime, test, publication or capacity check alone is a correctness verdict. Manual source/behavior/docs/claims findings remain in each linked delivered report. No GPT5 equivalence or autonomous reliability claim.','source_code_SHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(E/'completed-current-quant-comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'completed_cells_normalized':len(rows),'turn_sums_verified':True,'pending_cells_not_scored':True,'results':[{'candidate':r['candidate'],'workflow_pass':r['whole_workflow_pass'],'turn_minutes':[round(n,2)for n in r['turn_minutes']],'coding_minutes':round(r['total_coding_minutes'],2)}for r in rows]}))

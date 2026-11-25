"""Trusted local known-value scan. No credential values or native profiles exported."""
from pathlib import Path
import json,sys,re,base64,urllib.parse,tarfile,hashlib
from ruamel.yaml import YAML
values=set(json.load(sys.stdin))
def candidate(key,value):
 if re.search(r'(?:^|_)(?:TOKEN|PASSWORD|SECRET|API_KEY|ACCESS_KEY)$',key.upper()) and isinstance(value,str) and len(value)>=8:values.add(value)
def visit(obj):
 if isinstance(obj,dict):
  for key,value in obj.items():candidate(str(key),value);visit(value)
 elif isinstance(obj,list):
  for v in obj:visit(v)
for line in Path('/opt/data/.env').read_text().splitlines():
 if '=' in line and not line.lstrip().startswith('#'):
  k,v=line.split('=',1);candidate(k.strip(),v.strip().strip('\"\''))
visit(YAML(typ='safe').load(Path('/opt/data/config.yaml').read_text()))
auth=Path('/opt/data/auth.json')
if auth.exists():visit(json.loads(auth.read_text()))
patterns=set()
for value in values:
 for text in [value,urllib.parse.quote(value,safe=''),urllib.parse.quote_plus(value),json.dumps(value)[1:-1],base64.b64encode(value.encode()).decode()]:patterns.add(text.encode())
stage=sys.argv[1];assert stage in ['resource-fable-q4-thinking','resource-fable-q6-thinking','resource-vibe-q4-thinking','resource-vibe-q6-thinking']
keys=list(Path('/state').rglob('receipt-key'))
for path in keys:
 value=path.read_bytes();patterns.update([value,value.hex().encode(),base64.b64encode(value)])
matches=[];checked=0
def scan(payload,name):
 global checked
 checked+=1
 if any(v in payload for v in patterns):matches.append(name)
archive=Path('/public')/(stage+'-evidence.tar.gz')
archives=list(sorted(Path('/public').glob('*-evidence.tar.gz')))
assert archive in archives
for source_archive in archives:
 with tarfile.open(source_archive) as t:
  for entry in t:
   assert entry.isfile();scan(t.extractfile(entry).read(),'archive:'+source_archive.name+':'+entry.name)
for root in [Path('/public'),Path('/code')]:
 for f in root.rglob('*'):
  if f.is_file() and f.suffix in {'.py','.md','.json','.csv','.sha256','.log'}:scan(f.read_bytes(),str(f))
scan(Path('/root-readme').read_bytes(),'README.md')
scan(Path('/model-options').read_bytes(),'MODEL-OPTIONS.md')
result={'passed':not matches,'known_credential_values_checked':len(values),'private_receipt_keys_checked':len(keys),'patterns_checked':len(patterns),'payloads_checked':checked,'matching_paths':matches,'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'archives_checked':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in archives},'scanner_worker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Known credential values plus actual private signing keys and common encodings; not general secret detection. No values persisted or printed.'}
(Path('/state')/(stage+'-public-scan.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));assert not matches

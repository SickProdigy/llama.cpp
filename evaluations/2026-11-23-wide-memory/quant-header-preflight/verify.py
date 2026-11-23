"""Compare pinned public quant headers, not dequantized weight identity or quality."""
from pathlib import Path
import struct,hashlib,json
import argparse, urllib.request
A=Path(__file__).resolve().parent
for name,digest in json.loads((A/'sha256.json').read_text()).items():
 assert hashlib.sha256((A/name).read_bytes()).hexdigest()==digest,name
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--prefix-root',type=Path,default=A)
parser.add_argument('--fetch',action='store_true',help='Fetch only two bounded public16MiB prefixes, never full weights')
args=parser.parse_args();D=args.prefix_root
if args.fetch:
 repo='netprojects/Qwen3.8-27B-hermes-adapted-GGUF';revision='10fdf357f14825c61ad7eb42a932e1f1e4390e8f'
 for key,name,size in [('q3','Qwen3.8-27B-hermes-Q3_K_M.gguf',13752764064),('q4','Qwen3.8-27B-hermes-Q4_K_M.gguf',16810714560)]:
  out=D/(key+'-header')/'prefix.bin';out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():continue
  request=urllib.request.Request('https://huggingface.co/'+repo+'/resolve/'+revision+'/'+name,headers={'Range':'bytes=0-16777215'})
  with urllib.request.urlopen(request,timeout=60)as response:
   assert response.status==206 and response.headers.get('Content-Range')=='bytes 0-16777215/'+str(size)
   raw=response.read(16777217);assert len(raw)==16777216
  expected=json.loads((A/'expected.json').read_text())['headers'][key]['prefix_sha256'];assert hashlib.sha256(raw).hexdigest()==expected
  out.write_bytes(raw)

results={};descriptors={};fingerprints={};calibration={}
for key in ['q3','q4']:
 raw=(D/(key+'-header')/'prefix.bin').read_bytes();offset=4
 def take(fmt):
  global offset
  value=struct.unpack_from('<'+fmt,raw,offset)[0];offset+=struct.calcsize('<'+fmt);return value
 def string():
  global offset
  n=take('Q');v=raw[offset:offset+n].decode();offset+=n;assert offset<=len(raw);return v
 def skip(t):
  global offset
  sizes={0:1,1:1,2:2,3:2,4:4,5:4,6:4,7:1,10:8,11:8,12:8}
  if t==8:string()
  elif t==9:
   subtype=take('I');n=take('Q')
   if subtype in sizes:offset+=n*sizes[subtype]
   else:
    for _ in range(n):skip(subtype)
  else:offset+=sizes[t]
  assert offset<=len(raw)
 version=take('I');nt=take('Q');nm=take('Q');fields={};calibration[key]={}
 for _ in range(nm):
  name=string();start=offset;ty=take('I')
  if name.startswith('quantize.imatrix.'):
   calibration[key][name]=string()if ty==8 else take({4:'I',5:'i',10:'Q',11:'q'}[ty])
  else:skip(ty)
  fields[name]=hashlib.sha256(raw[start:offset]).hexdigest()
 tensors=[]
 for _ in range(nt):
  name=string();dims=[take('Q')for _ in range(take('I'))];ty=take('I');position=take('Q');tensors.append({'name':name,'dimensions':dims})
 descriptors[key]=tensors;fingerprints[key]=fields
 results[key]={'prefix_sha256':hashlib.sha256(raw).hexdigest(),'metadata_count':nm,'tensor_count':nt,'tensor_table_end':offset,'metadata_value_sha256':fields,'tensor_names_and_shapes_sha256':hashlib.sha256(json.dumps(tensors,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
a=fingerprints['q3'];b=fingerprints['q4'];different=[k for k in sorted(set(a)|set(b))if a.get(k)!=b.get(k)]
comparison={'q3_vs_q4_metadata_fields_differing':different,'non_file_type_metadata_bytes_identical':all(a.get(k)==b.get(k)for k in set(a)|set(b)if k!='general.file_type'),'tensor_names_and_shapes_identical':descriptors['q3']==descriptors['q4'],'tokenizer_metadata_bytes_including_token_arrays_identical':all(a.get(k)==b.get(k)for k in set(a)|set(b)if k.startswith('tokenizer.')),'core_non_quantization_metadata_bytes_identical':all(a.get(k)==b.get(k)for k in set(a)|set(b)if k!='general.file_type'and not k.startswith('quantize.imatrix.')),'calibration_metadata':calibration,'quantization_calibration_confounds_precision_only_attribution':True,'not_dequantized_weight_identity_proof':True,'not_load_fit_or_quality_proof':True,'Q3_full_model_not_downloaded_or_hashed':True}
assert json.loads((A/'expected.json').read_text())=={'comparison':comparison,'headers':results},'Header evidence differs from frozen expectations'
print(json.dumps(comparison,indent=2))

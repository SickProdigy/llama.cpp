"""Compare pinned public quant headers, not dequantized weight identity or quality."""
from pathlib import Path
import struct,hashlib,json,sys
assert len(sys.argv)==4, 'Supply Q3_K_M, Q4_K_M and IQ4_XS 16MiB prefixes in that order'
paths=dict(zip(['q3','q4','iq4'],map(Path,sys.argv[1:])))
results={};descriptors={};fingerprints={};calibration={}
for key in ['q3','q4','iq4']:
 raw=paths[key].read_bytes();assert raw[:4]==b'GGUF'and len(raw)==16*1024**2;offset=4
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
 tensors=[];tensor_types={};embedding_output=[]
 for _ in range(nt):
  name=string();dims=[take('Q')for _ in range(take('I'))];ty=take('I');position=take('Q');tensors.append({'name':name,'dimensions':dims});tensor_types[str(ty)]=tensor_types.get(str(ty),0)+1
  if name in ['token_embd.weight','output.weight']:embedding_output.append({'name':name,'dimensions':dims,'type':ty})
 descriptors[key]=tensors;fingerprints[key]=fields
 results[key]={'prefix_sha256':hashlib.sha256(raw).hexdigest(),'metadata_count':nm,'tensor_count':nt,'tensor_table_end':offset,'tensor_type_counts':tensor_types,'embedding_and_output':embedding_output,'metadata_value_sha256':fields,'tensor_names_and_shapes_sha256':hashlib.sha256(json.dumps(tensors,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
pairs={}
for left,right in [('q3','q4'),('q3','iq4'),('q4','iq4')]:
 a,b=fingerprints[left],fingerprints[right];keys=set(a)|set(b)
 pairs[left+'_vs_'+right]={'metadata_fields_differing':[k for k in sorted(keys)if a.get(k)!=b.get(k)],'tensor_names_and_shapes_identical':descriptors[left]==descriptors[right],'tokenizer_metadata_bytes_including_arrays_identical':all(a.get(k)==b.get(k)for k in keys if k.startswith('tokenizer.')),'core_non_quantization_metadata_bytes_identical':all(a.get(k)==b.get(k)for k in keys if k!='general.file_type'and not k.startswith('quantize.imatrix.'))}
print(json.dumps({'headers':results,'comparisons':pairs,'calibration_metadata':calibration,'limits':['Header fingerprints and shapes do not prove identical unquantized source weights.','Public calibration filenames/counts are metadata, not recovered calibration contents or audited production commands.','Different calibration, tensor mixes, runtime placement, contexts and tasks prevent precision-only attribution.','This standalone reader does not verify full model hashes, runtime fit or behavior.']},indent=2))

"""Bounded retained-file header audit, not full-file hash or fit proof."""
from pathlib import Path
import json,struct,hashlib,time,sys
D=Path(sys.argv[1]).resolve().parent;P={'adapted-iq4':{'file':'adapted-iq4-prefix.gguf','repo':'netprojects/Qwen3.8-27B-hermes-adapted-GGUF','revision':'10fdf357f14825c61ad7eb42a932e1f1e4390e8f'}};out={}
for key in ['adapted-iq4']:
 model=P[key];p=Path(sys.argv[1]).resolve()
 with p.open('rb')as f:raw=f.read(16*1024**2)
 offset=4;assert raw[:4]==b'GGUF';sizes={0:('B',1),1:('b',1),2:('H',2),3:('h',2),4:('I',4),5:('i',4),6:('f',4),7:('?',1),10:('Q',8),11:('q',8),12:('d',8)}
 def take(fmt):
  global offset
  n=struct.calcsize('<'+fmt);assert offset+n<=len(raw);v=struct.unpack_from('<'+fmt,raw,offset)[0];offset+=n;return v
 def string(keep=True):
  global offset
  n=take('Q');assert offset+n<=len(raw);v=raw[offset:offset+n].decode()if keep else None;offset+=n;return v
 def value(ty,keep=True):
  global offset
  if ty==8:return string(keep)
  if ty==9:
   begin=offset;subtype=take('I');n=take('Q');assert n<2000000
   if subtype in sizes:offset+=n*sizes[subtype][1];assert offset<=len(raw)
   else:
    for _ in range(n):value(subtype,False)
   return {'items':n,'type':subtype,'encoded_SHA256':hashlib.sha256(raw[begin:offset]).hexdigest()}
  assert ty in sizes;return take(sizes[ty][0])
 version=take('I');tensors=take('Q');count=take('Q');meta={}
 for _ in range(count):
  k=string();ty=take('I');v=value(ty)
  if k=='tokenizer.chat_template':v={'SHA256':hashlib.sha256(v.encode()).hexdigest(),'bytes':len(v.encode())}
  meta[k]=v
 descriptors=[];types={}
 for _ in range(tensors):
  name=string();nd=take('I');dims=[take('Q')for _ in range(nd)];ty=take('I');where=take('Q');descriptors.append({'name':name,'dimensions':dims,'type':ty});types[str(ty)]=types.get(str(ty),0)+1
 out[key]={'file':model['file'],'repo':model['repo'],'revision':model['revision'],'file_bytes':15321491104,'prefix_local_file_bytes':p.stat().st_size,'output_and_embedding_tensors':[r for r in descriptors if r['name'] in ['output.weight','token_embd.weight']],'prefix_bytes':len(raw),'prefix_SHA256':hashlib.sha256(raw).hexdigest(),'full_file_SHA_not_checked_by_this_header_reader':True,'GGUF_version':version,'tensor_count':tensors,'metadata':meta,'descriptor_end':offset,'tensor_type_counts':types,'tensor_names_and_dimensions_SHA256':hashlib.sha256(json.dumps([{k:v for k,v in row.items()if k!='type'}for row in descriptors],sort_keys=True).encode()).hexdigest()}
print(json.dumps({'models':out,'not_quality_or_fit_proof':True},indent=2))

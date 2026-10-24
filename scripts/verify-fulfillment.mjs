#!/usr/bin/env node
// Run only against a fresh BrowserFixture and its optional runtime on loopback port 8097.
import assert from 'node:assert/strict'
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs'
const port=Number(readFileSync(process.argv[2]??'/tmp/srotax-same-set-port','utf8').trim())
assert.ok(Number.isInteger(port)&&port>0&&port<65536)
const base=`http://127.0.0.1:${port}`;const cookies=new Map();let csrf,root,changeSet
async function request(path,method='GET',body,expected=200){
 const headers={Cookie:[...cookies].map(([k,v])=>`${k}=${v}`).join('; ')}
 if(csrf)headers[csrf.headerName]=csrf.token
 if(changeSet)headers['X-Srotax-Change-Set']=changeSet
 if(body!==undefined)headers['Content-Type']='application/json'
 const r=await fetch(base+path,{method,headers,body:body===undefined?undefined:JSON.stringify(body),redirect:'manual',signal:AbortSignal.timeout(20000)})
 for(const value of r.headers.getSetCookie()){const pair=value.split(';')[0],i=pair.indexOf('=');cookies.set(pair.slice(0,i),pair.slice(i+1))}
 const text=await r.text();assert.equal(r.status,expected,`${method} ${path}: ${text}`)
 return expected===302?r.headers.get('location'):text?JSON.parse(text):undefined
}
const api=(p,m='GET',b,e=200)=>request(root+p,m,b,e)
const redirect=await request('/auth/login?provider=google','GET',undefined,302);await request(redirect,'GET',undefined,302);csrf=await request('/api/session/csrf')
let session=await request('/api/session');if(!session.workspaces.length)session=await request('/api/session/onboarding','POST',{})
const ws=session.workspaces[0];root=`/api/organisations/${ws.organisationId}/workspaces/${ws.workspaceId}`
assert.equal((await api('/main')).revision,0,'Use a fresh disposable fixture')

const source=JSON.parse(readFileSync(process.argv[3]||'examples/fulfillment/assets.json','utf8'));
changeSet=(await api('/change-sets','POST',{name:'Regional handling data'},201)).id;
const dataset=await api('/reference-data','POST',{name:'Regional handling fees'});const datasetId=dataset.draft.id;
await api(`/reference-data/${datasetId}/draft/import`,'POST',{expectedRevision:0,table:{key:'country',columns:[{name:'country',type:'string'},{name:'handlingFee',type:'number'}],rows:[['CA',2],['US',4]]}});
let comparison=await api(`/change-sets/${changeSet}/changes`);await api(`/change-sets/${changeSet}/merge`,'POST',{expectedRevision:comparison.changeSet.revision});
changeSet=(await api('/change-sets','POST',{name:'Order fulfillment tutorial'},201)).id;
const ids=new Map();const created=[];
for(const a of source){const d=await api('/decisions','POST',{name:a.name,type:a.type},201);ids.set(a.id,d.id);created.push(d)}
const drafts=[];
for(let i=0;i<source.length;i++){
 const a=structuredClone(source[i]);
 for(const n of a.definition.nodes||[]){const s=n.data.step;
  for(const k of ['decisionTable','decisionTree','callFlow'])if(s[k]){s[k].decisionId=ids.get(s[k].decisionId);s[k].source='draft';s[k].version=0}
  if(s.lookupReference){s.lookupReference.datasetId=datasetId;s.lookupReference.version=1}
 }
 const draft=await api(`/decisions/${created[i].id}/draft`,'PUT',{draft:{...created[i],contract:a.contract,definition:a.definition},expectedRevision:0});drafts.push(draft)
}
const main=drafts.find(x=>x.name==='Order Fulfillment Flow');
const input={orderId:'DOC-1001',country:'CA',items:[{sku:'A',quantity:2,unitPrice:50,active:true,restricted:false},{sku:'B',quantity:1,unitPrice:40,active:true,restricted:false},{sku:'C',quantity:1,unitPrice:20,active:true,restricted:false},{sku:'D',quantity:1,unitPrice:10,active:true,restricted:false},{sku:'INACTIVE',quantity:1,unitPrice:999,active:false,restricted:false}]};
const preview=await api(`/decisions/${main.id}/preview`,'POST',{draft:main,inputs:input});
mkdirSync('target',{recursive:true});writeFileSync('target/fulfillment-preview.json',JSON.stringify(preview,null,2));assert.equal(preview.success,true,JSON.stringify(preview));
console.log('Output',JSON.stringify(preview.data));
writeFileSync('target/fulfillment-context.json',JSON.stringify({organisation:ws.organisationId,workspace:ws.workspaceId,changeSet,datasetId,assets:drafts.map(x=>({id:x.id,name:x.name,type:x.type})),input},null,2));
const cases=[['approved',input,172,'Approved'],['paid shipping',{...input,items:[{...input.items[0],quantity:1,unitPrice:20}]},31,'Approved'],['restricted',{...input,items:[{...input.items[0],quantity:1,unitPrice:20,restricted:true}]},31,'Review required'],['high value',{...input,items:[{...input.items[0],quantity:1,unitPrice:600}]},602,'Review required']];
for(const [name,inputs,total,status] of cases){const p=await api(`/decisions/${main.id}/preview`,'POST',{draft:main,inputs});assert.equal(p.success,true,JSON.stringify(p));assert.equal(p.data.total,total);assert.equal(p.data.status,status)}
assert.equal(preview.data.priorityValue,160);assert.ok(preview.trace.find(t=>t.nodeId==='call-order-charges').children.length>0);
for(const inputs of [{...input,country:'ZZ'},{...input,orderId:''}]){const p=await api(`/decisions/${main.id}/preview`,'POST',{draft:main,inputs});assert.equal(p.success,false)}
let releaseCheck='not run';
try {
 const diff=await api(`/change-sets/${changeSet}/changes`);
 const merge=await api(`/change-sets/${changeSet}/merge`,'POST',{expectedRevision:diff.changeSet.revision});changeSet=undefined;
 const release=await api('/releases','POST',{expectedMainRevision:merge.changeSet.mergedMainRevision},201);assert.equal(release.assets.length,4);
 const published=await api(`/decisions/${main.id}/versions/1/preview`,'POST',{inputs:input});assert.equal(published.success,true);assert.deepEqual(published.data,preview.data);releaseCheck='passed';
} catch(error) { releaseCheck='blocked: '+error.message.split('\n')[0]; }
mkdirSync('verification',{recursive:true});writeFileSync('verification/fulfillment.json',JSON.stringify({verifiedAt:new Date().toISOString(),environment:'Disposable BrowserFixture',checks:['four successful draft cases','unknown country rejected','blank order ID rejected','nested subflow trace present','priority sum differs from full subtotal'],releaseCheck,expected:preview.data},null,2)+'\n');
console.log('PASS: draft cases and nested trace. Release check: '+releaseCheck);
if(releaseCheck!=='passed')process.exitCode=1;

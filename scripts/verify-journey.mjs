#!/usr/bin/env node
// Run only against a fresh BrowserFixture and its optional runtime on loopback port 8097.
import assert from 'node:assert/strict'
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs'
import {spawnSync} from 'node:child_process'
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

const authoring=JSON.parse(readFileSync('examples/shipping/authoring.json','utf8'));
const cases=JSON.parse(readFileSync('examples/shipping/cases.json','utf8'));
changeSet=(await api('/change-sets','POST',{name:'Documentation shipping walkthrough'},201)).id;
let draft=await api('/decisions','POST',{name:'Shipping quickstart',type:'table'},201);
draft={...draft,...authoring};
draft=await api(`/decisions/${draft.id}/draft`,'PUT',{draft,expectedRevision:0});
assert.equal((await api(`/decisions/${draft.id}/validate`,'POST',{draft})).valid,true);
for(const c of cases){const p=await api(`/decisions/${draft.id}/preview`,'POST',{draft,inputs:c.input});assert.equal(p.success,true,JSON.stringify(p));assert.deepEqual(p.data,c.expected)}
const invalid=await api(`/decisions/${draft.id}/preview`,'POST',{draft,inputs:{subtotal:'wrong'}});assert.equal(invalid.success,false);
const comparison=await api(`/change-sets/${changeSet}/changes`);
const merged=await api(`/change-sets/${changeSet}/merge`,'POST',{expectedRevision:comparison.changeSet.revision});
assert.equal(merged.changeSet.status,'Merged');changeSet=undefined;
const version=await api(`/decisions/${draft.id}/versions/1`);assert.ok(version.artifact);
const release=await api('/releases','POST',{expectedMainRevision:merged.changeSet.mergedMainRevision},201);
const key=await api('/keys','POST',{name:'Disposable documentation client',environment:'dev'});
const runtime=`http://127.0.0.1:8097/api/runtime/decisions/${draft.id}/execute`;
async function run(input,secret=key.secret){const r=await fetch(runtime,{method:'POST',headers:{Authorization:`Bearer ${secret}`,'Content-Type':'application/json'},body:JSON.stringify(input),signal:AbortSignal.timeout(20000)});return {status:r.status,body:await r.json()}}
assert.equal((await run({subtotal:75})).status,404);
await api('/environments/dev/activation','PUT',{releaseId:release.id,expectedRevision:0});
for(const c of cases){const r=await run(c.input);assert.equal(r.status,200);assert.equal(r.body.success,true);assert.deepEqual(r.body.data,c.expected);const h=await api(`/executions/${r.body.runId}`);assert.equal(h.releaseId,release.id)}
assert.equal((await run({subtotal:75},'sx_'+'z'.repeat(43))).status,401);
assert.equal((await run({subtotal:'wrong'})).body.success,false);
const java=spawnSync(`${process.env.JAVA_HOME}/bin/java`,['examples/java/ShippingClient.java'],{encoding:'utf8',env:{...process.env,SROTAX_RUNTIME_URL:'http://127.0.0.1:8097',SROTAX_DECISION_ID:draft.id,SROTAX_API_KEY:key.secret}});
assert.equal(java.status,0,java.stderr);assert.deepEqual(JSON.parse(java.stdout).data,{fee:9,method:'Standard'});
mkdirSync('verification',{recursive:true});
writeFileSync('verification/journey.json',JSON.stringify({verifiedAt:new Date().toISOString(),environment:'Disposable PostgreSQL; fixture identity; real management/compiler/runtime HTTP',checks:['create change set','create and save nested-schema table','validate','five preview boundary cases','invalid preview input','merge creates version 1','release complete Main snapshot','execution unavailable before activation','activate Development','five runtime boundary cases','release-linked execution history','invalid key denied','invalid runtime input rejected','Java HTTP example executed'],cases:cases.length,java:'passed'},null,2)+'\n');
console.log('PASS: shipping create → contract → test → merge → release → activate → Java runtime client');

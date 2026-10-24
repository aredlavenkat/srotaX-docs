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

assert.equal((await api('/main')).revision,1,'Run shipping journey first in a fresh fixture');
const sets=await api('/change-sets'); changeSet=(sets.items.find(s=>s.name==='Explore Studio') ?? await api('/change-sets','POST',{name:'Explore Studio'},201)).id;
const folders=await api('/asset-folders');
const orders=folders.find(f=>f.name==='Orders') ?? await api('/asset-folders','POST',{name:'Orders'},201);
const shipping=folders.find(f=>f.name==='Shipping') ?? await api('/asset-folders','POST',{name:'Shipping',parentFolderId:orders.id},201);
const models=await api('/models');
const model=models.find(m=>m.name==='Address') ?? await api('/models','POST',{name:'Address',description:'Delivery address shared by order decisions',schema:{type:'object',properties:{street:{type:'string',example:'123 King Street'},city:{type:'string',example:'Toronto'},postalCode:{type:'string',example:'M5V 1A1'},country:{type:'string',example:'CA'}},required:['street','city','postalCode','country']},expectedRevision:0},200);
const contract=JSON.parse(readFileSync('examples/shipping/authoring.json','utf8')).contract;
async function author(name,type,contract,definition){let d=await api('/decisions','POST',{name,type,folderId:shipping.id},201);d={...d,contract,definition};return api(`/decisions/${d.id}/draft`,'PUT',{draft:d,expectedRevision:0})}
const group={id:'threshold-group',type:'group',op:'and',children:[{id:'subtotal-threshold',type:'condition',path:'subtotal',operator:'$gte',value:'100'}]};
const tree=await author('Shipping eligibility','tree',contract,{tiles:[{id:'start',kind:'start',title:'Start',assignments:[],yes:'threshold'},{id:'threshold',kind:'condition',title:'Free shipping eligible?',condition:{group},assignments:[],yes:'free',no:'paid'},...['free','paid'].map(id=>({id,kind:'result',title:id==='free'?'Free shipping':'Standard shipping',assignments:[{id:id+'-fee',path:'fee',value:id==='free'?'0':'9'},{id:id+'-method',path:'method',value:'Standard'}]}))]});
const simple={inputs:{type:'object',properties:{subtotal:{type:'number',example:75}},required:['subtotal']},outputs:{type:'object',properties:{total:{type:'number',example:84}},required:['total']},variables:{type:'object',properties:{},required:[]}};
const steps=[{id:'start',kind:'request',title:'Start'},{id:'total',kind:'transform',title:'Add shipping fee',set:{assignments:[{targetPath:'output.total',expression:{kind:'call',operator:'$add',args:[{kind:'field',path:'input.subtotal'},{kind:'literal',type:'number',value:'9'}]}}]}},{id:'response',kind:'response',title:'Return total'}];
const flow=await author('Order total','flow',simple,{nodes:steps.map((step,i)=>({id:step.id,type:'flowStep',position:{x:i*310,y:80},data:{step}})),edges:[{id:'e1',source:'start',target:'total'},{id:'e2',source:'total',target:'response'}]});
for(const [draft,expected] of [[tree,{fee:9,method:'Standard'}],[flow,{total:84}]]){const p=await api(`/decisions/${draft.id}/preview`,'POST',{draft,inputs:{subtotal:75}});assert.equal(p.success,true,JSON.stringify(p));assert.deepEqual(p.data,expected)}
const addressContract={...contract,inputs:{type:'object',properties:{subtotal:{type:'number',example:75},deliveryAddress:{$ref:'#/components/schemas/'+model.id}},required:['subtotal']}};
const table=await author('Shipping with address','table',addressContract,JSON.parse(readFileSync('examples/shipping/authoring.json','utf8')).definition);
mkdirSync('target',{recursive:true});writeFileSync('target/visual-guide-context.json',JSON.stringify({organisation:ws.organisationId,workspace:ws.workspaceId,changeSet,tree:tree.id,flow:flow.id,table:table.id,model:model.id},null,2));
console.log('PASS: disposable Model, folder, Tree and Flow examples prepared; Tree and Flow return expected results');

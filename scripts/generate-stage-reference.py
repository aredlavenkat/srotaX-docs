"""Generate stage reference pages from reviewed prose and executed examples."""
import argparse,json,collections,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--without-mongo',action='store_true');args=p.parse_args()
catalog=json.loads((root/'reference/stage-catalog.json').read_text())
report=json.loads((root/'verification/stage-behavior.json').read_text())
def code(v):return ['```json',json.dumps(v,indent=2),'```']
def cell(v):return str(v).replace('|','&#124;').replace('<','&lt;').replace('>','&gt;').replace('\n',' ')
def result(c):return 'Error: '+c['error']+' — '+c['message'] if 'error' in c else json.dumps(c['result'],separators=(',',':'))
index=['# Aggregation stages','','Stages transform a **list of documents**. Expression operators calculate a value inside a document. The same name can have different syntax in these contexts.','','These pages describe the 21 registered Core stages. They are not a list of Studio palette steps. For the authoring UI, use the [Flow step reference](steps.md). SrotaX normally processes one request document; use array expressions such as `$map` and `$sortArray` to transform its lists.','','Each page includes a runnable pipeline, actual Core output, and implementation limits. The stage examples are separate from the 6,495-case expression parity suite.','','| Stage | Purpose |','| --- | --- |']
for d in catalog:
 name=d['name'];slug=name[1:];cases=[c for c in report if c['stage']==name];example=next(c for c in cases if c['kind']=='example')
 assert 'error' not in example,name
 index.append(f"| [{name}](stages/{slug}.md) | {d['definition']} |")
 lines=[f'# {name}', '', '## Definition', '', d['definition'], '', '**Core aggregation stage** · '+d['category']+'. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.', '', '## Syntax', '', 'Basic form, with concrete values:',*code(d['syntax']),'','## Parameters','','| Parameter | Required | Description |','| --- | --- | --- |']
 for a in d['parameters']:lines.append(f"| `{a['name']}` | {a['required']} | {a['description']} |")
 lines+=['','## Behavior','']+['- '+b for b in d['behavior']]
 lines+=['','### Empty input and invalid specification','','These cases use the basic form above unless the specification is explicitly replaced.','','| Case | Observed result |','| --- | --- |']
 for c in cases:
  if c['kind'] in ['empty input','invalid specification']:lines.append('| '+c['kind']+(' (`null`)' if c['kind']=='invalid specification' else '')+' | '+cell(result(c))+' |')
 lines+=['','## Examples','','### Basic pipeline','','Input documents:',*code(example['input']),'','Pipeline:',*code(example['pipeline']),'','Result:',*code(example['result'])]
 extras=[c for c in cases if c['kind'] not in ['example','empty input','invalid specification']]
 for c in extras:
  lines+=['','### '+c['kind'].capitalize(),'','Input documents:',*code(c['input']),'','Pipeline:',*code(c['pipeline']),'']
  lines+=['**Observed error:** '+cell(c['message'])] if 'error' in c else ['Result:',*code(c['result'])]
 lines+=['','## Verification','',f'The {len(cases)} examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.', '', f'[Download the executable cases and recorded results](../../downloads/stage-behavior/{slug}.json).']
 if not args.without_mongo:
  lines+=['','<!-- BEGIN MONGO PARITY -->','## MongoDB differences','','Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.']
  lines+=['']+['- '+x for x in d['limitations']]
  if name!='$subPipeline':lines+=['',f'[MongoDB {name} reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/{slug}/). Read the Core behavior above before reusing MongoDB examples.']
  lines+=['','<!-- END MONGO PARITY -->']
 path=root/'docs/reference/stages'/f'{slug}.md';path.parent.mkdir(parents=True,exist_ok=True);path.write_text('\n'.join(lines)+'\n')
 path=root/'docs/downloads/stage-behavior'/f'{slug}.json';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(cases,indent=2)+'\n')
(root/'docs/reference/stages.md').write_text('\n'.join(index)+'\n')
print('Generated',len(catalog),'stage pages')

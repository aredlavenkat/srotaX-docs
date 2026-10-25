"""Generate engineer-facing operator pages from executed cases. Mongo sections are removable."""
import argparse,json,collections,html
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--report',type=Path,required=True);p.add_argument('--without-mongo',action='store_true');a=p.parse_args()
report=json.loads(a.report.read_text());catalog=json.loads((root/'reference/operator-catalog.json').read_text())
visual={x['value'] for x in catalog['expressions']};by=collections.defaultdict(list)
for c in report['cases']:by[c['operator']].append(c)
def compact(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def cell(x):return str(x).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n',' ')
def plain(v):
 if isinstance(v,list):return [plain(x) for x in v]
 if isinstance(v,dict):
  if len(v)==1:
   tag=next(iter(v))
   if tag in ['$numberInt','$numberLong']:return int(v[tag])
   if tag == '$numberDecimal':return v
   if tag == '$numberDouble':
    try:return float(v[tag])
    except ValueError:return v[tag]
  return {k:plain(x) for k,x in v.items()}
 return v
def describe(v):
 if 'error' in v:return 'Error: '+v['error']+' — '+v.get('message','')[:180]
 if not v.get('present'):return 'Missing (field omitted)'
 raw=json.loads(v['bson'])['v']
 if isinstance(raw,dict) and len(raw)==1:
  tag=next(iter(raw));types={'$numberInt':'int32','$numberLong':'int64','$numberDouble':'double','$numberDecimal':'decimal128','$date':'date','$timestamp':'timestamp','$oid':'ObjectId','$undefined':'undefined'}
  if tag in types:return str(raw[tag])+' ('+types[tag]+')'
 return compact(plain(raw))
def code(value):return ['```json',json.dumps(value,indent=2,ensure_ascii=False),'```']
def result(v):return cell(describe(v))
index=['# Operator behavior reference','',f"**{len(by)} registered expression operators**, documented from {report['caseCount']:,} executed cases.",'','[Read the coverage and testing methodology](operator-parity.md).', '', 'Each page separates SrotaX behavior from an optional MongoDB comparison section. The input tables are concrete regression cases, not a claim that every possible combination has been tested.','', '| Operator | Purpose | Cases |','| --- | --- | --- |']
for d in catalog['engineOperators']:
 op=d['name'];slug=op[1:];cases=by[op];baseline=next(c for c in cases if c['kind']=='baseline')
 index.append(f"| [{op}](operators/{slug}.md) | {cell(d['description'])} | {len(cases)} |")
 lines=[f'# {op}','',d['description'].replace('Mongo 6 numeric format tokens','supported numeric format tokens').replace('Mongo-style','JSON-style'),'',f"**Category:** {d['category']}. **Studio Visual entry:** {'Available' if op in visual else 'Not exposed'}. This page describes Core expression execution; Studio also checks field types and authoring permissions.",'','## Syntax and arguments','']
 syntax=d['argumentSyntax']
 lines += [{'SINGLE':'Supply one expression as the operator value.','POSITIONAL':'Supply an ordered array of arguments.','NAMED':'Supply an object with the named arguments below.'}[syntax],'']
 lines+=['| Argument | Metadata input types | Required | Evaluation |','| --- | --- | --- | --- |']
 for arg in d['operands']:lines.append(f"| `{arg['name']}` | {', '.join(arg['acceptedTypes'])} | {'Yes' if arg['required'] else 'No'} | {'Literal configuration' if arg.get('evaluation')=='LITERAL' else 'Expression evaluated against the input'} |")
 lines+=['',f"Argument count: minimum {d['minArguments']}; maximum {d['maxArguments'] if d['maxArguments']>=0 else 'variadic'}.",'',f"Declared result types: **{', '.join(d['resultTypes'])}**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation."]
 if op in ['$sum','$avg','$min','$max']:
  lines+=['','A single array-valued expression is also supported, for example `{"'+op+'": "$items"}`. With multiple operands, array arguments are not recursively flattened.']
 if op=='$range':
  lines+=['','**Resource limit:** very large ranges can exhaust engine memory. Bound range sizes before execution; an extreme-endpoint probe exhausted the test JVM and is excluded from the bounded tables below.']
 if op=='$convert':
  lines+=['','Supported `to` target names: `array`, `object`, `bool`, `double`, `string`, `date`, `int`, `long`, `decimal`. Array/object conversion parses a JSON string with the matching root. `onError` supplies a conversion-failure fallback; `onNull` supplies a null/missing fallback. Native ObjectId and UUID authoring remain outside the supported SrotaX scope.']
 if d['category'].lower().find('date')>=0:
  lines+=['','**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.']
 lines+=['','## Example' ,'', 'Expression:',*code(baseline['expression']),'','Input document:',*code(baseline['input']),'', '**Observed SrotaX result:** '+result(baseline['srotax'])+'.']
 if 'error' in baseline['srotax']:
  lines+=['','This baseline is rejected by the engine. Registration does not imply this combination works.']
 lines+=['','## Behavior for different inputs','','Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.','']
 groups=collections.defaultdict(list)
 for c in cases:
  if c['kind'] not in ['baseline','boundary example','empty arguments','unknown option']:groups[c['operand']].append(c)
 for operand,rows in groups.items():
  lines+=['### Argument: `'+operand+'`','','| Input case | Supplied value | SrotaX result |','| --- | --- | --- |']
  for c in rows:
   if c['kind']=='omitted named argument':supplied='Argument removed'
   elif 'missing' in c['kind']:supplied='Field absent'
   elif 'probe' in c['input']:supplied=compact(c['input']['probe'])
   else:
    argname=operand.split('[')[0];args=c['expression'][op]
    supplied=compact(args.get(argname)) if isinstance(args,dict) else compact(args)
   lines.append('| '+cell(c['kind'])+' | '+cell(supplied)+' | '+result(c['srotax'])+' |')
  lines.append('')
 lines+=['## Invalid invocation shapes','','| Invocation | SrotaX result |','| --- | --- |']
 for c in cases:
  if c['kind'] in ['empty arguments','unknown option']:lines.append('| '+cell(compact(c['expression']))+' | '+result(c['srotax'])+' |')
 extra=[c for c in cases if c['kind']=='boundary example']
 if extra:
  lines+=['','## Additional boundary examples','','<details>','<summary>Show '+str(len(extra))+' tested examples</summary>','']
  for c in extra:lines+=['Expression:',*code(c['expression']),'','Input:',*code(c['input']),'','**SrotaX:** '+result(c['srotax'])+'.','']
  lines+=['</details>']
 lines+=['','## Scope and reproducibility','',f'This page records **{len(cases)} executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.','',f'[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/{slug}.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.']
 downloads=root/'docs/downloads/operator-behavior';downloads.mkdir(parents=True,exist_ok=True)
 (downloads/(slug+'.json')).write_text(json.dumps([{k:v for k,v in c.items() if k not in ['mongo','status']} for c in cases],indent=2)+'\n')
 if not a.without_mongo:
  lines+=['','<!-- BEGIN MONGO PARITY -->','## MongoDB differences (removable section)','']
  if cases[0]['status']=='NOT_COMPARABLE_EXPRESSION':lines+=['This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.']
  elif report['mongoVersion']=='not run':lines+=['Live MongoDB comparison has not run for these cases.']
  else:
   counts=collections.Counter(c['status'] for c in cases)
   lines += [f"Compared with **MongoDB {report['mongoVersion']}**: **{counts['EXACT_MATCH']} exact BSON matches**, **{counts['BOTH_REJECTED']} both rejected**, **{counts['DIFFERENCE']} value/type/acceptance differences**, **{counts['FIELD_ORDER_DIFFERENCE']} object-field-order differences**.",'','“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.']
   diff=[c for c in cases if c['status'].endswith('DIFFERENCE')]
   if diff:
    lines+=['','| Tested case | SrotaX | MongoDB |','| --- | --- | --- |']
    for c in diff:lines.append('| '+cell(c['operand']+' / '+c['kind'])+' | '+result(c['srotax'])+' | '+result(c['mongo'])+' |')
   else:lines+=['','No differences were observed in the compared cases.']
   parity=root/'docs/downloads/operator-parity';parity.mkdir(parents=True,exist_ok=True)
   (parity/(slug+'.json')).write_text(json.dumps(cases,indent=2)+'\n')
   lines+=['',f'[Download full comparison evidence](../../downloads/operator-parity/{slug}.json).']
  lines+=['','<!-- END MONGO PARITY -->']
 (root/'docs/reference/operators'/f'{slug}.md').write_text('\n'.join(lines)+'\n')
(root/'docs/reference/operators.md').write_text('\n'.join(index)+'\n')
print('Generated',len(by),'pages; Mongo section', 'omitted' if a.without_mongo else 'included')

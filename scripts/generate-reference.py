"""Generate attributed operator docs from the saved Management catalog. No network calls."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
catalog=json.loads((root/'reference/operator-catalog.json').read_text())
examples={x['operator']:x for x in json.loads((root/'examples/expressions.json').read_text())}
verified={x['operator'] for x in json.loads((root/'verification/expressions.json').read_text()) if x['executed']} if (root/'verification/expressions.json').exists() else set()
visual={x['value'] for x in catalog['expressions']}
def write(name,text):
 p=root/'docs/reference'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def cell(v):return str(v).replace('|','\\|').replace('\n',' ')
index=['# Operator inventory','',f"Catalog snapshot: **{len(catalog['engineOperators'])} registered engine operators**, **{len(visual)} Visual function entries**. Target metadata: MongoDB {catalog['targetMongoVersion']}.",'','Registration is not the same as compiler acceptance, Visual availability, or verified MongoDB parity. The compiler validates the complete expression and its field types. The tested-example column refers only to the checked-in compiler/engine example, not all inputs.','','| Operator | Category | Visual entry | Example executed | Metadata classification |','| --- | --- | --- | --- | --- |']
for op in catalog['engineOperators']:
 n=op['name'];slug=n[1:];c=op.get('compatibility',{})
 index.append(f"| [{n}](operators/{slug}.md) | {cell(op['category'])} | {'Yes' if n in visual else 'No'} | {'Yes' if n in verified else 'Not in this docs suite'} | {cell(c.get('classification','Unknown'))} |")
 lines=[f'# {n}', '',op['description'],'',f"**Category:** {op['category']} · **Visual function entry:** {'Yes' if n in visual else 'No'}",'', '## Signature (engine metadata)','',f"Argument syntax: `{op['argumentSyntax']}`. Minimum arguments: {op['minArguments']}. Maximum: {op['maxArguments'] if op['maxArguments']>=0 else 'variadic'}.",'', '| Operand | Accepted types | Required | Evaluation |','| --- | --- | --- | --- |']
 for a in op['operands']:lines.append(f"| {cell(a['name'])} | {', '.join(a['acceptedTypes'])} | {a['required']} | {a.get('evaluation','EXPRESSION')} |")
 lines+=['',f"Result types: {', '.join(op['resultTypes'])}.",'', '## Null and missing (engine metadata)','',f"- Null: {op['nullBehavior']}",f"- Missing: {op['missingBehavior']}",'','## Compatibility boundary','',f"Classification: `{c.get('classification','Unknown')}`. Verification scope reported by the engine: `{c.get('verificationScope','Unspecified')}`.",'']
 lines += ['- '+s for s in c.get('limitations',[])]
 lines+=['','These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.']
 if n in verified:
  x=examples[n];lines+=['','## Executed example','','The SrotaX compiler accepted this JSON expression and the engine returned the expected value. Empty input document.','','```json',json.dumps(x['expression'],indent=2),'```','','Expected value:','','```json',json.dumps(x['expected']),'```']
 else:lines+=['','## Example coverage','','No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.']
 if op.get('alternativeSignatures'):lines+=['','## Alternative signatures (metadata)','','```json',json.dumps(op['alternativeSignatures'],indent=2),'```']
 if c.get('documentationUrl'):lines+=['',f"[MongoDB reference linked by engine metadata]({c['documentationUrl']})",'',f"Source revision recorded by engine: `{c.get('sourceRevision','unspecified')}`."]
 if n in examples and examples[n].get('expectedError'):
  lines+=['','## Reproduced limitation','','The following literal-array expression compiles but fails in the engine with `'+examples[n]['expectedError']+'`. This is a product issue; registration does not guarantee this case works.','','```json',json.dumps(examples[n]['expression'],indent=2),'```']
 write(f'operators/{slug}.md' ,'\n'.join(lines)+'\n')
write('operators.md','\n'.join(index)+'\n')
lines=['# Condition recipes','','These are SrotaX condition recipes from the API catalog. Some combine multiple engine operators; recipe names must not be presented as MongoDB operators.']
for group in catalog['conditionGroups']:
 lines+=['','## '+group['label'],'','| Label | Recipe | Input types | Operand kind | Engine dependencies |','| --- | --- | --- | --- | --- |']
 for op in group['operators']:lines.append(f"| {cell(op['label'])} | `{op['value']}` | {', '.join(op['inputTypes'])} | {op.get('operandKind','')} | {', '.join(op.get('requiredOperators',[]))} |")
lines+=['','## Aggregate List operations','','| Operation | Requires a field |','| --- | --- |']
for op in catalog['summaryOperations']:lines.append(f"| {op['label']} (`{op['value']}`) | {op['requiresField']} |")
write('conditions.md','\n'.join(lines)+'\n')
print('Generated',len(catalog['engineOperators']),'operator pages')

# Keep sidebar entries in sync with the same catalog that produces the pages.
config_path=root/'mkdocs.yml'
config=config_path.read_text()
start='    # BEGIN GENERATED OPERATOR NAV'
end='    # END GENERATED OPERATOR NAV'
nav=[start,'    - Operators:','      - Overview: reference/operators.md']
for category in sorted({op['category'] for op in catalog['engineOperators']}):
 nav.append(f'      - {json.dumps(category)}:')
 for op in sorted((op for op in catalog['engineOperators'] if op['category']==category),key=lambda op:op['name'].lower()):
  nav.append(f"        - {json.dumps(op['name'])}: reference/operators/{op['name'][1:]}.md")
nav.append(end)
block='\n'.join(nav)
if start in config:
 before,rest=config.split(start,1)
 _,after=rest.split(end,1)
 config=before+block+after
else:
 config=config.replace('    - Operators: reference/operators.md',block)
config_path.write_text(config)

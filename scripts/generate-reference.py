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
 if n == '$convert':
  header=lines.index('| Operand | Accepted types | Required | Evaluation |')
  lines[header:]=[
   '| Operand | Accepted types | Supported values | Required | Evaluation |',
   '| --- | --- | --- | --- | --- |',
   '| input | ANY | Value to convert | True | EXPRESSION |',
   '| to | INT, STRING | `"array"` (4), `"object"` (3), `"bool"` (8), `"double"` (1), `"string"` (2), `"date"` (9), `"int"` (16), `"long"` (18), `"decimal"` (19) | True | EXPRESSION |',
   '| onError | ANY | Fallback value when conversion fails | False | EXPRESSION |',
   '| onNull | ANY | Fallback value for null or missing input | False | EXPRESSION |',
   '', '`INT, STRING` describes the argument type of `to`, not the conversion result. For example, `"to": "array"` supplies a string target name and produces an array. Numeric type codes can be used instead of names.',
  ]
 lines+=['',f"Result types: {', '.join(op['resultTypes'])}.",'', '## Null and missing (engine metadata)','',f"- Null: {op['nullBehavior']}",f"- Missing: {op['missingBehavior']}",'','## Compatibility boundary','',f"Classification: `{c.get('classification','Unknown')}`. Verification scope reported by the engine: `{c.get('verificationScope','Unspecified')}`.",'']
 lines += ['- '+s for s in c.get('limitations',[])]
 if n == '$convert':
  lines[4:4] = [
   '## Convert JSON strings to array or object', '',
   'Set `to` to `"array"` or `"object"`. The input must be a JSON string whose root matches the target.', '',
   '### Convert to array', '',
   '```json', json.dumps({'$convert': {'input': '[1,2]', 'to': 'array'}}, indent=2), '```', '',
   '**Result:** `[1, 2]`', '',
   '### Convert to object', '',
   '```json', json.dumps({'$convert': {'input': '{"x":1}', 'to': 'object'}}, indent=2), '```', '',
   '**Result:** `{"x": 1}`', '',
   'Shorthand: [`$toArray`](toArray.md) and [`$toObject`](toObject.md). Invalid JSON raises an error unless `onError` is supplied. Null or missing input returns null unless `onNull` is supplied.', '',
  ]
  lines += [
   '', '## Supported conversion targets', '',
   'The current engine implements the following target names. Support depends on the input type; this is not a promise that every source type converts to every target.', '',
   '| Target | Numeric type code |', '| --- | --- |',
   '| `double` | 1 |', '| `string` | 2 |', '| `bool` | 8 |',
   '| `date` | 9 |', '| `array` | 4 |', '| `object` | 3 |', '| `int` | 16 |', '| `long` | 18 |', '| `decimal` | 19 |',
   '', 'The engine also contains a legacy `objectId` conversion (code 7). Native BSON ObjectId and UUID types are outside SrotaX’s supported authoring scope; use string identifiers.',
   '', '**JSON-string conversion to `array` and `object` is supported.** The JSON root must match the target. The shorthand operators `$toArray` and `$toObject` use the same conversion logic.',
   '', '`$objectToArray` and `$arrayToObject` transform objects and key/value pairs; they do not parse JSON strings.',
   '', '## Boolean conversion (`bool`)', '',
   'Use `"to": "bool"` (or type code `8`). Booleans retain their value; numeric zero becomes false and nonzero numbers become true. Strings, arrays, and objects become true, including empty values. Strings are not parsed as boolean literals: `"false"`, `"0"`, and `""` all become true. Null or missing input uses `onNull`, or returns null when no fallback is provided.',
   '', 'Use [`$toBool`](toBool.md) for the shorthand form.',
   '', '## Error and null fallbacks', '',
   '- `onError` returns a fallback when conversion fails. Without it, the conversion raises an error.',
   '- `onNull` returns a fallback for null or missing input. Without it, the result is null.',
   '- An unsupported string target can also return `onError`. Receiving that fallback does not mean the target is supported.',
   '', 'These are conversion fallbacks, not a catch-all for malformed expressions or invalid target type codes.',
   '', 'For example, invalid JSON returns an empty array:', '',
   '```json', '{"$convert": {"input": "not valid JSON", "to": "array", "onError": [], "onNull": []}}', '```', '', 'Result: `[]`.',
  ]
 if n in {'$convert', '$toArray', '$toObject'}:
  lines += ['', '## JSON parsing behavior', '',
   'Pass a string containing strict JSON. Comments, trailing commas, trailing documents, wrong root types, non-string inputs, null bytes in field names and numeric overflow are rejected. Duplicate object keys retain the last value. Null or missing input returns null unless a $convert onNull fallback is supplied.',
   '', 'Extended JSON wrappers such as {"$date":"2026-01-01"} remain ordinary objects. Parsed content is data, not an expression to evaluate. Integer values use 32-bit or 64-bit storage when they fit; larger integers become doubles and may lose precision. Decimal/exponent values become doubles.',
   '', 'MongoDB binary-vector conversion is not supported. Native UUID and ObjectId types remain outside product scope.',
   '', 'Verified against MongoDB 9.0.4 in 76 focused cases: matching values or rejection by both engines. Matching error codes/messages and complete MongoDB parity are not claimed.']
 if n == '$dateDiff':
  lines[4:4] = ['Use this operator to calculate the date difference between a start date and an end date.', '']
 if n in {'$median','$percentile','$stdDevPop','$stdDevSamp','$bitNot'}:
  lines+=['','These five operators were checked against MongoDB 9.0.4 in 99 focused cases: 80 matching results and 19 cases rejected by both engines. Floating-point comparison uses a relative tolerance of 1e-12; error-code parity is not established. See [statistics examples and compatibility limits](../array-statistics.md).']
 else:
  lines+=['','Catalog metadata is not certification of MongoDB equivalence. See the [MongoDB compatibility audit](../mongo-compatibility.md) for observed differences.']
 if n in verified:
  selected=[x for x in json.loads((root/'examples/expressions.json').read_text()) if x['operator']==n] if n == '$convert' else [examples[n]]
  lines+=['','## Executed examples' if len(selected)>1 else '## Executed example','','The SrotaX compiler accepted these JSON expressions and the engine returned the expected values. Empty input document.' if len(selected)>1 else 'The SrotaX compiler accepted this JSON expression and the engine returned the expected value. Empty input document.']
  for x in selected:
   if n == '$convert':lines+=['', '### Target `'+str(x['expression'][n]['to'])+'` — input `'+json.dumps(x['expression'][n]['input'])+'`']
   lines+=['','```json',json.dumps(x['expression'],indent=2),'```','','Expected value:','','```json',json.dumps(x['expected']),'```']
 else:lines+=['','## Example coverage','','No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.']
 if op.get('alternativeSignatures'):lines+=['','## Alternative signatures (metadata)','','```json',json.dumps(op['alternativeSignatures'],indent=2),'```']
 if c.get('documentationUrl'):lines+=['',f"[MongoDB reference linked by engine metadata]({c['documentationUrl']})",'',f"Source revision recorded by engine: `{c.get('sourceRevision','unspecified')}`."]
 if n in examples and examples[n].get('expectedError'):
  lines+=['','## Reproduced limitation','','The following literal-array expression compiles but fails in the engine with `'+examples[n]['expectedError']+'`. This is a product issue; registration does not guarantee this case works.','','```json',json.dumps(examples[n]['expression'],indent=2),'```']
 write(f'operators/{slug}.md' ,'\n'.join(lines)+'\n')
write('operators.md','\n'.join(index)+'\n')
lines=['# Condition recipes','','These are SrotaX condition recipes from the API catalog. Some combine multiple engine operators; recipe names must not be presented as MongoDB operators.']
lines += """
## Combine conditions with nested groups

Use **AND** when every condition must pass and **OR** when any condition may pass. A nested group lets you combine those choices in one rule.

This Decision Tree condition requires a subtotal greater than 100 **and** a country of either CA or US:

```text
subtotal > 100 AND (country = CA OR country = US)
```

[![Condition editor with an outer AND group and a nested OR group for CA or US](../images/nested-conditions.jpg)](../images/nested-conditions.jpg)

*The outer AND combines the subtotal comparison with the entire nested OR group.*

1. Open a Decision Tree condition and select **AND** for its outer group.
2. Select `input.subtotal`, **Greater than**, and `100`.
3. Select **Add group** and choose **OR** within the nested group.
4. Add `input.country` **Equals** `CA` and `input.country` **Equals** `US` inside that group.
5. Save the draft and test both matching and nonmatching inputs.

| Subtotal | Country | Condition result |
| --- | --- | --- |
| 150 | CA | True |
| 150 | US | True |
| 150 | GB | False |
| 100 | CA | False: the comparison is strictly greater than 100 |

Keep both country checks inside the nested group. Putting all three comparisons in an outer OR group would allow CA or US orders regardless of their subtotal.""".splitlines()
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

# Executed behavior is authoritative for operator pages; metadata-only regeneration
# must not overwrite the behavior tables or their separately removable parity sections.
behavior_report = root / 'verification/all-operator-behavior.json'
if behavior_report.exists():
 import subprocess, sys
 command = [sys.executable, str(root / 'scripts/generate-operator-behavior.py'), '--report', str(behavior_report)]
 if '--without-mongo' in sys.argv: command.append('--without-mongo')
 subprocess.run(command, check=True)

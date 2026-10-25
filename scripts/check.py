"""Check local links, JSON fences, fixtures and generated catalog coverage."""
import json,re
from pathlib import Path
from urllib.parse import unquote
root=Path(__file__).resolve().parents[1]
errors=[]
for p in (root/'docs').rglob('*.md'):
 text=p.read_text()
 for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
  if '://' in target or target.startswith(('#','mailto:')):continue
  path=unquote(target.split('#')[0])
  if path and not (p.parent/path).exists():errors.append(f'{p.relative_to(root)}: missing {target}')
 for block in re.findall(r'```json\s*\n(.*?)\n```',text,re.S):
  try:json.loads(block)
  except ValueError as e:errors.append(f'{p.relative_to(root)}: invalid JSON: {e}')
for directory in ['examples','reference','verification']:
 for p in (root/directory).rglob('*.json'):
  try:json.loads(p.read_text())
  except ValueError as e:errors.append(f'{p}: {e}')
catalog=json.loads((root/'reference/operator-catalog.json').read_text())
assert len({x['name'] for x in catalog['engineOperators']})==len(catalog['engineOperators'])
for op in catalog['engineOperators']:
 if not (root/'docs/reference/operators'/f"{op['name'][1:]}.md").exists():errors.append('Missing operator '+op['name'])
for dest,source in [('shipping-authoring.json','examples/shipping/authoring.json'),('shipping-cases.json','examples/shipping/cases.json'),('ShippingClient.java','examples/java/ShippingClient.java'),('runtime-openapi.json','reference/runtime-openapi.json')]:
 if (root/'docs/downloads'/dest).read_bytes()!=(root/source).read_bytes():errors.append('Stale download: '+dest)
report_path=root/'verification/all-operator-behavior.json'
if report_path.exists():
 report=json.loads(report_path.read_text())
 names={x['name'] for x in catalog['engineOperators']}
 if {c['operator'] for c in report['cases']}!=names:errors.append('Behavior report operator coverage differs from catalog')
 if len(report['cases'])!=report['caseCount']:errors.append('Behavior report case count differs')
 for name in names:
  page=(root/'docs/reference/operators'/f'{name[1:]}.md').read_text()
  for heading in ['## Syntax and arguments','## Behavior for different inputs','## Scope and reproducibility']:
   if heading not in page:errors.append(f'{name}: missing {heading}')
  if page.count('<!-- BEGIN MONGO PARITY -->')!=page.count('<!-- END MONGO PARITY -->'):errors.append(f'{name}: unbalanced parity block')
  download=json.loads((root/'docs/downloads/operator-behavior'/f'{name[1:]}.json').read_text())
  if len(download)!=sum(c['operator']==name for c in report['cases']):errors.append(f'{name}: stale behavior download')
if errors:raise SystemExit('\n'.join(errors))
print('PASS: local links, JSON blocks, fixtures, and operator page coverage')

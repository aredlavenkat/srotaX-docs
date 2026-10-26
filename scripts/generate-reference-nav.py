"""Maintain collapsible, parallel operator/stage reference navigation."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
operators=json.loads((root/'reference/operator-catalog.json').read_text())['engineOperators']
stages=json.loads((root/'reference/stage-catalog.json').read_text())
trig={'$acos','$acosh','$asin','$asinh','$atan','$atan2','$atanh','$cos','$cosh','$sin','$sinh','$tan','$tanh','$degreesToRadians','$radiansToDegrees'}
def group(d):
 n=d['name']
 if n in trig:return 'Trigonometry'
 if n.startswith('$bit') and n!='$binarySize':return 'Bitwise'
 return {'Arrays':'Array','Objects':'Object','Sets':'Set','Text':'String','Logic':'Boolean','Types and conversion':'Type and conversion','Dates':'Date','Advanced':'Miscellaneous'}.get(d['category'],d['category'])
start='    # BEGIN GENERATED OPERATOR NAV';end='    # END GENERATED OPERATOR NAV'
nav=[start,'    - Operators:','      - Overview: reference/operators.md']
for category in sorted({group(d) for d in operators}):
 nav.append('      - '+json.dumps(category)+':')
 for d in sorted([d for d in operators if group(d)==category],key=lambda d:d['name'].lower()):nav.append('        - '+json.dumps(d['name'])+': reference/operators/'+d['name'][1:]+'.md')
nav+=['    - Stages:','      - Overview: reference/stages.md']
for category in ['Reshape documents','Filter and order','Group and summarize','Combine pipelines','Window and sequence','Core extensions']:
 nav.append('      - '+json.dumps(category)+':')
 for d in sorted([d for d in stages if d['category']==category],key=lambda d:d['name'].lower()):nav.append('        - '+json.dumps(d['name'])+': reference/stages/'+d['name'][1:]+'.md')
nav+=['    - Reference verification: reference/operator-parity.md',end]
p=root/'mkdocs.yml';s=p.read_text();before,rest=s.split(start,1);_,after=rest.split(end,1);p.write_text(before+'\n'.join(nav)+after)

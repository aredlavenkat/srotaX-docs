"""Regenerate reference pages and navigation from reviewed source data and evidence."""
import json,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
catalog=json.loads((root/'reference/operator-catalog.json').read_text())
def cell(v):return str(v).replace('|','\\|').replace('\n',' ')
def write(name,text):(root/'docs/reference'/name).write_text(text)
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

commands=[['generate-operator-behavior.py','--report',str(root/'verification/all-operator-behavior.json')],['generate-stage-reference.py'],['generate-reference-nav.py']]
for command in commands:
 if '--without-mongo' in sys.argv and command[0]!='generate-reference-nav.py':command.append('--without-mongo')
 subprocess.run([sys.executable,str(root/'scripts'/command[0]),*command[1:]],check=True)

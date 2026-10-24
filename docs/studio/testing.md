# Test decisions

The same Test Panel is used by Tables, Trees, and Flows; its contents adapt to the asset.

| Tab | Use it for |
| --- | --- |
| Test Input | Enter a JSON request and run it |
| Result | Inspect the returned output |
| Trace | Inspect the matched table row, tree path, or Flow execution steps |
| Issues | Read validation and execution failures |

Use example input as a starting point, then edit it to test boundary values. Examples are not a coverage guarantee.

On **Main**, the label beside Run Test identifies the version being executed. In a **change set**, the test uses the current draft, including unsaved changes. Saving after a test is still necessary to persist the draft.

## Minimum test set

Test a normal case, each condition boundary, every branch or row you expect to reach, missing required fields, incorrect types, and empty lists where relevant. For Models, repeat affected tests after changing a shared field.

A green validation result proves structural acceptance, not that the rule matches business intent. A valid but shadowed table row can still produce the wrong business outcome.

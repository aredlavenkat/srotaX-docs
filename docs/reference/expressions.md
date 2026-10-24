# Expressions and conditions

Visual expressions choose a supported function and supply its arguments. Advanced JSON expressions use the engine's expression syntax. The modes contain separate expressions: select the one you intend to use. They are not automatically synchronized.

`input.*`, `local.*`, `output.*`, and the current list item have different scopes. Select fields from the picker where possible. A reference that exists in another step or another asset is not automatically available at the current location.

The [operator inventory](operators.md) separates registered engine operators from functions offered to the Visual editor. Scoped operators such as `$map`, `$filter`, and `$reduce` require scope-aware configuration and are not generic Visual function entries.

Condition pickers also contain business-facing recipes built from one or more operators. A recipe name does not necessarily identify a MongoDB operator. Use [condition reference](conditions.md) to inspect their metadata.

For each expression, test its normal value, null/missing inputs, wrong types, and boundary values relevant to your contract. Structural validation cannot establish that the formula is your intended business rule.

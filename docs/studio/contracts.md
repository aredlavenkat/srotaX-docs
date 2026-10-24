# Define a Data Contract

A contract declares the shape and types of the values your decision accepts and returns. Define it before adding condition columns or mapping fields.

| Section | Studio path | Purpose |
| --- | --- | --- |
| Inputs | `input.subtotal` | Incoming request; immutable in Flows |
| Local (Flows) | `local.items` | Intermediate values that steps may replace |
| Outputs | `output.fee` | Declared response fields |

## Edit fields

Select a section, expand its root row, and use **+** to add a field. Set its name, type, Required checkbox, example, and optional description. Objects contain child fields; lists declare an item type. Object lists can contain nested fields or refer to a Model.

Required means the value must be supplied where validated. An example helps construct test input; it is **not a default value** and does not populate missing production input.

## Switch between Fields and JSON

Both views edit the same schema. Switching from JSON to Fields validates and applies valid JSON automatically. If it is invalid, stay in JSON, fix the displayed errors, and switch again. There is no separate Apply to Fields action.

The editor uses `input`, `local`, and `output` sections. The authoring API uses `contract.inputs`, `contract.variables`, and `contract.outputs`. Each section is a nested schema object, not positional field arrays. See [schema reference](../reference/schemas.md).

## Use a Model

Choose a model in the root or object row's Type area. Its fields appear as a read-only preview. Choosing a model replaces custom descendants under that object. Adding a manual child clears the model binding; detaching removes the reference and its displayed descendants. Neither action is a safe way to keep a copied snapshot of the model fields.

References follow the current model in the selected change set. See [Models](models.md) before changing a shared definition.

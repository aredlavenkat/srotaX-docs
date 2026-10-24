# Build a Flow

Use a Flow to transform one request, call reusable decisions, branch, and return a response. It is not a collection ETL pipeline.

## Keep the original input

`input.*` is immutable. Read from it and write working values into `local.*`. Reuse a local variable when its previous value is no longer needed. For example:

1. Transform `input.items` into `local.items`.
2. Filter or sort `local.items` in place.
3. Aggregate `local.items` into a local total.
4. Assign the result to an output field.

You do not need `originalInput`: the original request remains in `input.*`. In-place list operations must target a compatible local list. Set Fields and Choose Fields must not modify the input namespace.

## Configure each step

Select a step to open its drawer. Choose source fields, output destination, and operation-specific options. Field choices depend on the contract and preceding steps. An expression's current item is scoped to its list operation; it is not a workspace variable.

When calling a Table, Tree, or Flow, map the called asset's input fields from available sources and map its result into the caller. Review dependency selection before merging; a published dependency and a same-change-set draft are different choices.

## Branch and return

Give each branch a complete route to a Response. Current graph editing permits one incoming connection per step; branches do not merge into a shared downstream step. Validate disconnected paths and test both sides of conditions.

Use the Test Panel's trace to inspect ordered steps and nested calls. The canvas highlights the executed path. See the [step reference](../reference/steps.md) for the supported operations.

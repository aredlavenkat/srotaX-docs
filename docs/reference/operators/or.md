# $or

Requires at least one truthy expression result.

**Category:** Logic · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `POSITIONAL`. Minimum arguments: 0. Maximum: variadic.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| expression | ANY | True | EXPRESSION |

Result types: BOOLEAN.

## Null and missing (engine metadata)

- Null: With expression set to literal null in the regression example: returns false. This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With expression set to a missing direct-field reference in the regression example: returns false. This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_SUBSET`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Executed example

The SrotaX compiler accepted this JSON expression and the engine returned the expected value. Empty input document.

```json
{
  "$or": [
    false,
    true
  ]
}
```

Expected value:

```json
true
```

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/or.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

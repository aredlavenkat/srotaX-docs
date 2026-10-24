# $ifNull

Uses a fallback when the first expression is null or missing.

**Category:** Conditional · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `POSITIONAL`. Minimum arguments: 2. Maximum: variadic.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| input | ANY | True | EXPRESSION |
| fallback | ANY | True | EXPRESSION |

Result types: ANY.

## Null and missing (engine metadata)

- Null: With input set to literal null in the regression example: returns "fallback". This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With input set to a missing direct-field reference in the regression example: returns "fallback". This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_SUBSET`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Verification covers regression cases; full BSON and locale conformance is not certified.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Executed example

The SrotaX compiler accepted this JSON expression and the engine returned the expected value. Empty input document.

```json
{
  "$ifNull": [
    null,
    "fallback"
  ]
}
```

Expected value:

```json
"fallback"
```

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/ifNull.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

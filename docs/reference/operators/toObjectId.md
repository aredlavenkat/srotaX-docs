# $toObjectId

Converts a value to objectid.

**Category:** Types and conversion · **Visual function entry:** No

## Signature (engine metadata)

Argument syntax: `SINGLE`. Minimum arguments: 1. Maximum: 1.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| input | STRING | True | EXPRESSION |

Result types: NULL, OBJECT_ID.

## Null and missing (engine metadata)

- Null: Returns null for null input.
- Missing: Returns null for missing input.

## Compatibility boundary

Classification: `MONGO_6_DIFFERENCES`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Non-date conversion failures return null without onError rather than throwing.
- Conversion matrix, BSON wrapping and overflow are not fully Mongo-certified.
- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/toObjectId.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

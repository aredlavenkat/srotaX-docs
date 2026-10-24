# $type

Returns the BSON-style type name of a value.

**Category:** Types and conversion · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `SINGLE`. Minimum arguments: 1. Maximum: 1.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| input | ANY | True | EXPRESSION |

Result types: STRING.

## Null and missing (engine metadata)

- Null: With input set to literal null in the regression example: returns "null". This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With input set to a missing direct-field reference in the regression example: returns "missing". This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_SUBSET`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/type.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

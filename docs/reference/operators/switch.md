# $switch

Selects the first branch with a true boolean condition.

**Category:** Conditional · **Visual function entry:** No

## Signature (engine metadata)

Argument syntax: `NAMED`. Minimum arguments: 1. Maximum: 2.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| branches | ARRAY | True | SCOPED_EXPRESSION |
| default | ANY | False | EXPRESSION |

Result types: ANY.

## Null and missing (engine metadata)

- Null: With branches set to literal null in the regression example: throws an exception. This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With branches set to a missing direct-field reference in the regression example: throws an exception. This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_DIFFERENCES`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Cases require Boolean.TRUE. No match without default returns null rather than a Mongo error.
- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/switch.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

# $min

Returns the least operand in an explicit expression list.

**Category:** Arrays · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `POSITIONAL`. Minimum arguments: 1. Maximum: variadic.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| value | NUMBER | True | EXPRESSION |

Result types: NUMBER.

## Null and missing (engine metadata)

- Null: With value set to literal null in the regression example: returns null. This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With value set to a missing direct-field reference in the regression example: returns null. This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_DIFFERENCES`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Describes expression usage, not accumulator stages. BSON cross-type ordering and single-array-expression traversal are not certified.
- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/min.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

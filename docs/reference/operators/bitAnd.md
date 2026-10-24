# $bitAnd

Computes bitwise AND of integers.

**Category:** Arithmetic · **Visual function entry:** No

## Signature (engine metadata)

Argument syntax: `POSITIONAL`. Minimum arguments: 2. Maximum: variadic.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| integer | INT, LONG | True | EXPRESSION |

Result types: LONG.

## Null and missing (engine metadata)

- Null: With integer set to literal null in the regression example: throws an exception. This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With integer set to a missing direct-field reference in the regression example: throws an exception. This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `NON_MONGO_6_EXPRESSION`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Mongo bitwise aggregation expressions were introduced after 6.0.
- Not a MongoDB 6.0 aggregation expression; do not expose as a portable Mongo 6.0 operator.
- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

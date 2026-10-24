# $let

Evaluates an expression with locally bound variables.

**Category:** Conditional · **Visual function entry:** No

## Signature (engine metadata)

Argument syntax: `NAMED`. Minimum arguments: 2. Maximum: 2.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| vars | OBJECT | True | BINDINGS |
| in | ANY | True | SCOPED_EXPRESSION |

Result types: ANY.

## Null and missing (engine metadata)

- Null: With vars set to literal null in the regression example: returns null. This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With vars set to a missing direct-field reference in the regression example: returns null. This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_DIFFERENCES`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Variable declarations can depend on sibling declarations, unlike Mongo lexical binding.
- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/let.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

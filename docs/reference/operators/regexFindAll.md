# $regexFindAll

Finds regex matches and their UTF-16 indexes.

**Category:** Text · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `NAMED`. Minimum arguments: 2. Maximum: 3.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| input | STRING | True | EXPRESSION |
| regex | STRING | True | EXPRESSION |
| options | STRING | False | EXPRESSION |

Result types: ARRAY.

## Null and missing (engine metadata)

- Null: With input set to literal null in the regression example: throws an exception. This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With input set to a missing direct-field reference in the regression example: throws an exception. This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_DIFFERENCES`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Uses Java regex, not full MongoDB PCRE compatibility.
- Verification covers regression cases; full BSON and locale conformance is not certified.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/regexFindAll.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

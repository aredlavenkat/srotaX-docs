# $dateTrunc

Truncates a date and returns a date value.

**Category:** Dates · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `NAMED`. Minimum arguments: 2. Maximum: 5.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| date | DATE | True | EXPRESSION |
| unit | STRING | True | EXPRESSION |
| binSize | INT | False | EXPRESSION |
| timezone | STRING | False | EXPRESSION |
| startOfWeek | STRING | False | EXPRESSION |

Result types: DATE, NULL.

## Null and missing (engine metadata)

- Null: Returns null when the required value is null.
- Missing: Missing required values resolve to null.

## Compatibility boundary

Classification: `MONGO_6_SUBSET`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Verification covers regression cases; full BSON and locale conformance is not certified.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/dateTrunc.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

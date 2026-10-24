# $dateFromString

Parses a date string and returns a date value.

**Category:** Dates · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `NAMED`. Minimum arguments: 1. Maximum: 5.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| dateString | STRING | True | EXPRESSION |
| format | STRING | False | EXPRESSION |
| timezone | STRING | False | EXPRESSION |
| onError | ANY | False | EXPRESSION |
| onNull | ANY | False | EXPRESSION |

Result types: ANY, DATE, NULL.

## Null and missing (engine metadata)

- Null: Evaluates onNull lazily for null or missing dateString; returns null when no fallback is supplied.
- Missing: Missing required values resolve to null.

## Compatibility boundary

Classification: `MONGO_6_DIFFERENCES`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- ISO input and numeric Mongo format tokens supported; permissive natural-language parsing and %U/%w/%Z parsing remain unsupported.
- Verification covers regression cases; full BSON and locale conformance is not certified.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/dateFromString.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

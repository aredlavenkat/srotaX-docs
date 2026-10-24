# $add

Adds numbers, or adds millisecond offsets to a single date.

**Category:** Arithmetic · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `POSITIONAL`. Minimum arguments: 0. Maximum: variadic.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| number | DATE, NUMBER | True | EXPRESSION |

Result types: DATE, NULL, NUMBER.

## Null and missing (engine metadata)

- Null: Returns null when the required value is null.
- Missing: Missing required values resolve to null.

## Compatibility boundary

Classification: `MONGO_6_DIFFERENCES`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Numeric promotion and full BSON edge cases are not exhaustively certified; simple collation only.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Executed example

The SrotaX compiler accepted this JSON expression and the engine returned the expected value. Empty input document.

```json
{
  "$add": [
    1,
    2,
    3
  ]
}
```

Expected value:

```json
6
```

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/add.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

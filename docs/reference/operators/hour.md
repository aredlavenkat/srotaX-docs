# $hour

Extracts hour using the host calendar.

**Category:** Dates · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `SINGLE`. Minimum arguments: 1. Maximum: 1.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| input | DATE | True | EXPRESSION |

Result types: INT, NULL.

## Null and missing (engine metadata)

- Null: Returns null when the required value is null.
- Missing: Missing required values resolve to null.

## Compatibility boundary

Classification: `MONGO_6_SUBSET`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Verification covers regression cases; full BSON and locale conformance is not certified.

These statements come from the engine catalog. This documentation has not independently certified equivalence against a running MongoDB server.

## Example coverage

No executable example for this operator is included in the documentation suite yet. Use the signature above and validate your complete expression; do not interpret registration as a guarantee for every argument combination.

## Alternative signatures (metadata)

```json
[
  {
    "syntax": "NAMED",
    "operands": [
      {
        "name": "date",
        "label": "date",
        "acceptedTypes": [
          "DATE"
        ],
        "required": true,
        "description": "Evaluated expression.",
        "evaluation": "EXPRESSION"
      },
      {
        "name": "timezone",
        "label": "timezone",
        "acceptedTypes": [
          "STRING"
        ],
        "required": false,
        "description": "Evaluated expression.",
        "evaluation": "EXPRESSION"
      }
    ],
    "minArguments": 1,
    "maxArguments": 2
  }
]
```

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/hour.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

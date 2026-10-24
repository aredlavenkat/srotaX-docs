# $cond

Evaluates Mongo truthiness and lazily returns the selected branch.

**Category:** Conditional · **Visual function entry:** Yes

## Signature (engine metadata)

Argument syntax: `POSITIONAL`. Minimum arguments: 3. Maximum: 3.

| Operand | Accepted types | Required | Evaluation |
| --- | --- | --- | --- |
| if | ANY | True | EXPRESSION |
| then | ANY | True | EXPRESSION |
| else | ANY | True | EXPRESSION |

Result types: ANY.

## Null and missing (engine metadata)

- Null: With if set to literal null in the regression example: returns "no". This is observed Fluxion behavior, not a general Mongo conformance claim.
- Missing: With if set to a missing direct-field reference in the regression example: returns "no". This is observed Fluxion behavior, not a general Mongo conformance claim.

## Compatibility boundary

Classification: `MONGO_6_SUBSET`. Verification scope reported by the engine: `ENGINE_REGRESSION_EXAMPLES`.

- Verification covers the checked-in regression examples, not full BSON, null, error or collation equivalence.

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
        "name": "if",
        "label": "If",
        "acceptedTypes": [
          "ANY"
        ],
        "required": true,
        "description": "Evaluated expression.",
        "evaluation": "EXPRESSION"
      },
      {
        "name": "then",
        "label": "Then",
        "acceptedTypes": [
          "ANY"
        ],
        "required": true,
        "description": "Evaluated expression.",
        "evaluation": "EXPRESSION"
      },
      {
        "name": "else",
        "label": "Else",
        "acceptedTypes": [
          "ANY"
        ],
        "required": true,
        "description": "Evaluated expression.",
        "evaluation": "EXPRESSION"
      }
    ],
    "minArguments": 3,
    "maxArguments": 3
  }
]
```

[MongoDB reference linked by engine metadata](https://raw.githubusercontent.com/mongodb/docs/3baea2dd8f2386d64c3c9a6805f625b80d9bacf4/source/reference/operator/aggregation/cond.txt)

Source revision recorded by engine: `3baea2dd8f2386d64c3c9a6805f625b80d9bacf4`.

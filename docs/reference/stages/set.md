# $set

## Definition

Adds or replaces fields while retaining other fields.

**Core aggregation stage** · Reshape documents. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$set": {
    "total": {
      "$multiply": [
        "$quantity",
        "$price"
      ]
    }
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `field: expression` | Yes | Destination field path and expression. A dotted path writes a nested object field. |

## Behavior

- One output document is returned for each input document.
- Direct field expressions read the incoming document. Use a later stage when one assignment depends on a previous assignment.
- Nested writes use shallow document copies in this handler. Do not rely on direct Core stage calls to provide SrotaX’s immutable-input authoring guarantees.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $set expects an object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "quantity": 2,
    "price": 5,
    "orderId": "A"
  }
]
```

Pipeline:
```json
[
  {
    "$set": {
      "total": {
        "$multiply": [
          "$quantity",
          "$price"
        ]
      }
    }
  }
]
```

Result:
```json
[
  {
    "quantity": 2,
    "price": 5,
    "orderId": "A",
    "total": 10.0
  }
]
```

### Null and missing source

Input documents:
```json
[
  {},
  {
    "value": null
  }
]
```

Pipeline:
```json
[
  {
    "$set": {
      "copy": "$value"
    }
  }
]
```

Result:
```json
[
  {
    "copy": null
  },
  {
    "value": null,
    "copy": null
  }
]
```

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/set.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.


[MongoDB $set reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

# $project

## Definition

Builds each output document from explicitly selected or computed fields.

**Core aggregation stage** · Reshape documents. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$project": {
    "name": 1,
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
| `field: 1` | No | Copy the named field. |
| `field: 0` | No | Skip this field when building the new document. |
| `field: expression` | No | Compute the destination field. Use `$literal` to assign a literal 0 or 1. |

## Behavior

- Only fields explicitly added by the specification appear in the output. `_id` is not included automatically.
- A zero entry is skipped; an exclusion-only projection returns an empty object rather than all other fields. Use `$unset` to remove fields while retaining the rest.
- The handler recognizes numeric 0/1 flags. Boolean values are computed values, not inclusion/exclusion flags.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $project stage requires an object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "_id": 7,
    "name": "Pen",
    "quantity": 2,
    "price": 5
  }
]
```

Pipeline:
```json
[
  {
    "$project": {
      "name": 1,
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
    "name": "Pen",
    "total": 10.0
  }
]
```

### Exclusion only

Input documents:
```json
[
  {
    "name": "Pen",
    "price": 5
  }
]
```

Pipeline:
```json
[
  {
    "$project": {
      "price": 0
    }
  }
]
```

Result:
```json
[
  {}
]
```

### Missing field

Input documents:
```json
[
  {}
]
```

Pipeline:
```json
[
  {
    "$project": {
      "unknown": 1
    }
  }
]
```

Result:
```json
[
  {
    "unknown": null
  }
]
```

## Verification

The 5 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/project.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- MongoDB supports exclusion projections and includes `_id` by default; this handler does neither.

[MongoDB $project reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

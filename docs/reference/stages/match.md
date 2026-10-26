# $match

## Definition

Retains documents that satisfy a condition object.

**Core aggregation stage** · Filter and order. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$match": {
    "score": {
      "$gte": 10
    }
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `condition` | Yes | Field predicates or logical expressions. Use `$expr` for an expression comparison. |

## Behavior

- All top-level field predicates must match. An empty condition retains all documents.
- `$expr` retains a document only when its expression returns boolean true.
- A failed match removes the document from the output list; it does not modify the document.
- Supported field predicates: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`, `$exists`, `$size`, `$all`, `$elemMatch`, `$regex` (with `$options`), `$type`, `$not`. Logical groups: `$and`, `$or`, `$nor`, `$not`.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $match stage requires a condition object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "score": 5
  },
  {
    "score": 12
  }
]
```

Pipeline:
```json
[
  {
    "$match": {
      "score": {
        "$gte": 10
      }
    }
  }
]
```

Result:
```json
[
  {
    "score": 12
  }
]
```

### Null and missing

Input documents:
```json
[
  {},
  {
    "score": null
  },
  {
    "score": 1
  }
]
```

Pipeline:
```json
[
  {
    "$match": {
      "score": null
    }
  }
]
```

Result:
```json
[
  {},
  {
    "score": null
  }
]
```

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/match.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- Query predicates and expression operators have different argument shapes. The expression parity suite does not certify query matching.

[MongoDB $match reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

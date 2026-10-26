# $group

## Definition

Combines documents sharing a grouping key and computes accumulator outputs.

**Core aggregation stage** · Group and summarize. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$group": {
    "_id": "$category",
    "total": {
      "$sum": "$amount"
    }
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `_id` | Yes | Grouping expression; use null for one group across all documents. |
| `field: accumulator` | No | One accumulator expression per output field, for example `{"$sum":"$amount"}`. |

## Behavior

- Produces one output per grouping key; this is a list-level aggregation.
- Accumulator operators run in grouping context, separate from expression operators with the same names.
- Use a fresh execution context for independent requests; reusing a state store can accumulate groups across calls.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $group stage must be a document |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "category": "A",
    "amount": 2
  },
  {
    "category": "A",
    "amount": 3
  },
  {
    "category": "B",
    "amount": 1
  }
]
```

Pipeline:
```json
[
  {
    "$group": {
      "_id": "$category",
      "total": {
        "$sum": "$amount"
      }
    }
  }
]
```

Result:
```json
[
  {
    "_id": "A",
    "total": 5
  },
  {
    "_id": "B",
    "total": 1
  }
]
```

### Null and missing group

Input documents:
```json
[
  {},
  {
    "category": null
  }
]
```

Pipeline:
```json
[
  {
    "$group": {
      "_id": "$category",
      "count": {
        "$sum": 1
      }
    }
  }
]
```

Result:
```json
[
  {
    "_id": null,
    "count": 2
  }
]
```

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/group.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- Expression-operator parity results do not certify grouping accumulators.

[MongoDB $group reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

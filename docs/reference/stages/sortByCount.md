# $sortByCount

## Definition

Counts documents per grouping value and sorts groups by descending count.

**Core aggregation stage** · Group and summarize. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$sortByCount": "$category"
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `expression` | Yes | Expression used as the grouping key. |

## Behavior

- Internally executes `$group` with a count followed by `$sort` on count descending.
- Output fields are `_id` and `count`. Equal-count ordering is not a business ordering guarantee.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $sortByCount requires a grouping expression |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "category": "A"
  },
  {
    "category": "A"
  },
  {
    "category": "B"
  }
]
```

Pipeline:
```json
[
  {
    "$sortByCount": "$category"
  }
]
```

Result:
```json
[
  {
    "_id": "A",
    "count": 2
  },
  {
    "_id": "B",
    "count": 1
  }
]
```

## Verification

The 3 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/sortByCount.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.


[MongoDB $sortByCount reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sortByCount/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

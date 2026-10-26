# $bucket

## Definition

Groups numeric values into explicit lower-inclusive, upper-exclusive ranges.

**Core aggregation stage** · Group and summarize. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$bucket": {
    "groupBy": "$price",
    "boundaries": [
      0,
      10,
      20
    ],
    "default": "other",
    "output": {
      "count": {
        "$sum": 1
      }
    }
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `groupBy` | Yes | Expression resolving to the numeric value to classify. |
| `boundaries` | Yes | At least two numeric boundaries in ascending order. Adjacent values define ranges. |
| `default` | No | Label for values outside the ranges or for nonnumeric/null/missing values. |
| `output` | No | Accumulator output fields. Omitted output produces only `_id`; explicitly add count with `$sum: 1`. |

## Behavior

- Only populated buckets appear, in boundary order followed by the default bucket.
- Without a default, unmatched values are skipped.
- Boundary comparison uses doubles. Use a fresh context for independent requests.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $bucket stage requires an object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "price": 3
  },
  {
    "price": 14
  },
  {
    "price": 30
  }
]
```

Pipeline:
```json
[
  {
    "$bucket": {
      "groupBy": "$price",
      "boundaries": [
        0,
        10,
        20
      ],
      "default": "other",
      "output": {
        "count": {
          "$sum": 1
        }
      }
    }
  }
]
```

Result:
```json
[
  {
    "_id": 0.0,
    "count": 1
  },
  {
    "_id": 10.0,
    "count": 1
  },
  {
    "_id": "other",
    "count": 1
  }
]
```

### Unmatched without default

Input documents:
```json
[
  {
    "price": 20
  },
  {},
  {
    "price": null
  }
]
```

Pipeline:
```json
[
  {
    "$bucket": {
      "groupBy": "$price",
      "boundaries": [
        0,
        10
      ]
    }
  }
]
```

Result:
```json
[]
```

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/bucket.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- MongoDB errors for unmatched values without a default and supplies a default count when output is omitted. Core skips those values and does not add count automatically.

[MongoDB $bucket reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucket/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

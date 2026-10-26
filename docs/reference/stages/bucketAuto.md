# $bucketAuto

## Definition

Divides the numeric value range into equal-width buckets.

**Core aggregation stage** · Group and summarize. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$bucketAuto": {
    "groupBy": "$price",
    "buckets": 2,
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
| `groupBy` | Yes | Numeric expression used to compute the value range. Nonnumeric values are ignored. |
| `buckets` | Yes | Positive integer number of buckets. |
| `output` | No | Supported accumulators: `$sum`, `$avg`, `$min`, `$max`, `$push`, `$addToSet`, `$first`, `$last`. No default count is added. |

## Behavior

- This implementation uses equal-width ranges, not equal document populations.
- Each `_id` is the numeric lower bound. Empty buckets can appear. The final upper bound is maximum + 1.
- With no numeric values the output is empty. Granularity is not implemented.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $bucketAuto stage requires an object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "price": 1
  },
  {
    "price": 2
  },
  {
    "price": 10
  }
]
```

Pipeline:
```json
[
  {
    "$bucketAuto": {
      "groupBy": "$price",
      "buckets": 2,
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
    "_id": 1.0,
    "count": 2.0
  },
  {
    "_id": 5.5,
    "count": 1.0
  }
]
```

### No numeric values

Input documents:
```json
[
  {},
  {
    "price": null
  },
  {
    "price": "x"
  }
]
```

Pipeline:
```json
[
  {
    "$bucketAuto": {
      "groupBy": "$price",
      "buckets": 2
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

[Download the executable cases and recorded results](../../downloads/stage-behavior/bucketAuto.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- MongoDB aims for balanced bucket populations and returns `_id.min`/`_id.max`. Core uses equal widths and a scalar `_id`.

[MongoDB $bucketAuto reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucketAuto/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

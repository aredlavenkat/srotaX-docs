# $setWindowFields

## Definition

Adds values computed over an ordered partition of documents.

**Core aggregation stage** · Window and sequence. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$setWindowFields": {
    "sortBy": {
      "score": 1
    },
    "output": {
      "rank": {
        "$rank": {}
      }
    }
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `partitionBy` | No | Expression identifying independent partitions. |
| `sortBy` | Yes | Exactly one field with numeric direction 1 or -1. |
| `output` | Yes | Nonempty object of output fields, each containing one supported window function. |
| `window.documents` | No | Two bounds: integer offsets, `"current"`, or `"unbounded"`. Default is unbounded-to-current. |

## Behavior

- Supported functions: `$shift`, `$rank`, `$denseRank`, `$derivative`, `$integral`, `$expMovingAvg`, `$stdDevPop`, `$stdDevSamp`, `$covariancePop`, `$covarianceSamp`.
- Only document-position windows are implemented. Range/time windows are rejected.
- A function supported as an expression or grouping accumulator is not automatically a supported window function.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $setWindowFields stage expects an object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "score": 20
  },
  {
    "score": 10
  },
  {
    "score": 20
  }
]
```

Pipeline:
```json
[
  {
    "$setWindowFields": {
      "sortBy": {
        "score": 1
      },
      "output": {
        "rank": {
          "$rank": {}
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
    "score": 20,
    "rank": 2
  },
  {
    "score": 10,
    "rank": 1
  },
  {
    "score": 20,
    "rank": 2
  }
]
```

### Unsupported sum

Input documents:
```json
[
  {
    "score": 10
  }
]
```

Pipeline:
```json
[
  {
    "$setWindowFields": {
      "sortBy": {
        "score": 1
      },
      "output": {
        "total": {
          "$sum": "$score"
        }
      }
    }
  }
]
```

**Observed error:** Unsupported window function: $sum

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/setWindowFields.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- This is a subset of MongoDB window functionality; range windows and other window accumulators are not implemented.

[MongoDB $setWindowFields reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/setWindowFields/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

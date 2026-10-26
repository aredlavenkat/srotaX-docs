# $fill

## Definition

Replaces null or missing values using a value expression or interpolation.

**Core aggregation stage** · Window and sequence. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$fill": {
    "sortBy": {
      "x": 1
    },
    "output": {
      "y": {
        "method": "linear"
      }
    }
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `sortBy` | Yes | Exactly one sort field with direction 1 or -1, including for value-based fill. |
| `partitionBy` | No | Expression grouping rows into independent partitions. |
| `output` | Yes | Nonempty object mapping destination fields to `{value: expression}` or `{method: name}`. |
| `method` | When interpolating | `"locf"` carries the last known value; `"linear"` interpolates between numeric endpoints. |

## Behavior

- Existing non-null values are preserved. Rows are sorted within each partition.
- Linear fill requires surrounding values; leading/trailing gaps without both endpoints remain unfilled.
- Use `partitionBy`; a `partitionByFields` option is not implemented in this handler.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $fill stage requires an object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "x": 0,
    "y": 0
  },
  {
    "x": 1,
    "y": null
  },
  {
    "x": 2,
    "y": 10
  }
]
```

Pipeline:
```json
[
  {
    "$fill": {
      "sortBy": {
        "x": 1
      },
      "output": {
        "y": {
          "method": "linear"
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
    "x": 0,
    "y": 0
  },
  {
    "x": 1,
    "y": 5.0
  },
  {
    "x": 2,
    "y": 10
  }
]
```

### Missing value fill

Input documents:
```json
[
  {
    "x": 1
  }
]
```

Pipeline:
```json
[
  {
    "$fill": {
      "sortBy": {
        "x": 1
      },
      "output": {
        "y": {
          "value": 0
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
    "x": 1,
    "y": 0
  }
]
```

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/fill.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- This handler requires single-field sortBy and implements a subset of fill configuration.

[MongoDB $fill reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/fill/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

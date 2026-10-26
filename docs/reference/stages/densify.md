# $densify

## Definition

Inserts documents for missing numeric or date positions.

**Core aggregation stage** · Window and sequence. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$densify": {
    "field": "x",
    "range": {
      "step": 1,
      "bounds": "full"
    }
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `field` | Yes | Numeric/date field path. |
| `range.step` | Yes | Positive increment. |
| `range.bounds` | No | `"full"` (default) or `[lower, upper]`. |
| `range.unit` | For dates | `"millisecond"`, `"second"`, `"minute"`, `"hour"`, or `"day"`. |
| `partitionByFields` | No | Nonempty array of field paths identifying independent partitions. |

## Behavior

- Processes gaps within each partition. Generated documents carry the densified field and partition fields.
- Null field values are rejected. Keep generation ranges bounded to avoid large allocations.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $densify stage requires an object |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "x": 1
  },
  {
    "x": 3
  }
]
```

Pipeline:
```json
[
  {
    "$densify": {
      "field": "x",
      "range": {
        "step": 1,
        "bounds": "full"
      }
    }
  }
]
```

Result:
```json
[
  {
    "x": 1
  },
  {
    "x": 2.0
  },
  {
    "x": 3
  }
]
```

### Null field

Input documents:
```json
[
  {
    "x": null
  }
]
```

Pipeline:
```json
[
  {
    "$densify": {
      "field": "x",
      "range": {
        "step": 1
      }
    }
  }
]
```

**Observed error:** $densify field 'x' must have at least one non-null value

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/densify.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- The `"partition"` bounds token and larger calendar units are not implemented. No live MongoDB stage parity is claimed.

[MongoDB $densify reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/densify/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

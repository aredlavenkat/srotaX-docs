# $skip

## Definition

Drops the first N documents.

**Core aggregation stage** · Filter and order. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$skip": 1
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `count` | Yes | Nonnegative numeric count. Use an integer; the handler converts a Number through Java intValue(). |

## Behavior

- Document order is preserved.
- Zero retains all input documents.
- Negative values raise an error. A count larger than the list returns an empty list.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $skip stage requires a numeric argument |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "x": 1
  },
  {
    "x": 2
  }
]
```

Pipeline:
```json
[
  {
    "$skip": 1
  }
]
```

Result:
```json
[
  {
    "x": 2
  }
]
```

### Negative count

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
    "$skip": -1
  }
]
```

**Observed error:** $skip cannot be negative

### Zero count

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
    "$skip": 0
  }
]
```

Result:
```json
[
  {
    "x": 1
  }
]
```

## Verification

The 5 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/skip.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- Core accepts zero and truncates fractional numeric counts. Do not infer MongoDB argument validation from this permissive conversion.

[MongoDB $skip reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/skip/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

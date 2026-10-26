# $limit

## Definition

Keeps the first N documents.

**Core aggregation stage** · Filter and order. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$limit": 1
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `count` | Yes | Nonnegative numeric count. Use an integer; the handler converts a Number through Java intValue(). |

## Behavior

- Document order is preserved.
- Zero returns an empty list.
- Negative values raise an error. A count larger than the list returns the whole list.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $limit stage requires a numeric argument |

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
    "$limit": 1
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
    "$limit": -1
  }
]
```

**Observed error:** $limit cannot be negative

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
    "$limit": 0
  }
]
```

Result:
```json
[]
```

## Verification

The 5 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/limit.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- Core accepts zero and truncates fractional numeric counts. Do not infer MongoDB argument validation from this permissive conversion.

[MongoDB $limit reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/limit/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

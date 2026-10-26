# $sort

## Definition

Orders documents by one or more fields.

**Core aggregation stage** · Filter and order. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$sort": {
    "score": -1,
    "name": 1
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `field: direction` | Yes | Sort field path and direction: `1` ascending or `-1` descending. Fields are compared in specification order. |

## Behavior

- Sorts the document list, not an array inside one document. Use the `$sortArray` expression for an array.
- Equal keys keep their incoming order. Missing/null values sort before non-null values in ascending order.
- Unsupported comparison values fall back to their string representations. There is no database collation setting.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $sort expects an object with sort keys |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "name": "B",
    "score": 2
  },
  {
    "name": "A",
    "score": 3
  }
]
```

Pipeline:
```json
[
  {
    "$sort": {
      "score": -1,
      "name": 1
    }
  }
]
```

Result:
```json
[
  {
    "name": "A",
    "score": 3
  },
  {
    "name": "B",
    "score": 2
  }
]
```

### Invalid direction

Input documents:
```json
[
  {
    "score": 1
  },
  {
    "score": 2
  }
]
```

Pipeline:
```json
[
  {
    "$sort": {
      "score": 0
    }
  }
]
```

**Observed error:** $sort direction must be 1 or -1: 0

### Null and missing

Input documents:
```json
[
  {
    "score": 2
  },
  {
    "score": null
  },
  {}
]
```

Pipeline:
```json
[
  {
    "$sort": {
      "score": 1
    }
  }
]
```

Result:
```json
[
  {
    "score": null
  },
  {},
  {
    "score": 2
  }
]
```

## Verification

The 5 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/sort.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- The implementation uses Core value comparison and a string fallback, not database collation.

[MongoDB $sort reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

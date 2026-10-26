# $unwind

## Definition

Produces one document for each element of an array field.

**Core aggregation stage** · Reshape documents. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$unwind": "$items"
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `path` | Yes | String field path, normally prefixed with `$`. Only the string form is implemented. |

## Behavior

- An empty array, null or missing field emits no document.
- A non-null scalar emits the original document once.
- Nested field handling uses shallow copies; prefer array expressions for document-local list transformations.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $unwind stage requires a single string field path |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "id": "A",
    "items": [
      1,
      2
    ]
  }
]
```

Pipeline:
```json
[
  {
    "$unwind": "$items"
  }
]
```

Result:
```json
[
  {
    "id": "A",
    "items": 1
  },
  {
    "id": "A",
    "items": 2
  }
]
```

### Null missing empty and scalar

Input documents:
```json
[
  {},
  {
    "items": null
  },
  {
    "items": []
  },
  {
    "items": 4
  }
]
```

Pipeline:
```json
[
  {
    "$unwind": "$items"
  }
]
```

Result:
```json
[
  {
    "items": 4
  }
]
```

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/unwind.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- The object form with `includeArrayIndex` or `preserveNullAndEmptyArrays` is not implemented.

[MongoDB $unwind reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unwind/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

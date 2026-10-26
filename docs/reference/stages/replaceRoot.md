# $replaceRoot

## Definition

Replaces the entire document with an object expression.

**Core aggregation stage** · Reshape documents. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$replaceRoot": {
    "newRoot": "$address"
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `newRoot` | Yes | Expression resolving to an object. The object becomes the complete output document. |

## Behavior

- The result must be an object. Null, missing or scalar values raise an error.
- Other fields from the original document are not retained.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $replaceRoot requires 'newRoot' field |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "name": "Alice",
    "address": {
      "city": "Toronto"
    }
  }
]
```

Pipeline:
```json
[
  {
    "$replaceRoot": {
      "newRoot": "$address"
    }
  }
]
```

Result:
```json
[
  {
    "city": "Toronto"
  }
]
```

### Missing root

Input documents:
```json
[
  {}
]
```

Pipeline:
```json
[
  {
    "$replaceRoot": {
      "newRoot": "$address"
    }
  }
]
```

**Observed error:** $replaceRoot evaluated to non-object: null

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/replaceRoot.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.


[MongoDB $replaceRoot reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

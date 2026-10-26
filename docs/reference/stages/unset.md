# $unset

## Definition

Removes named fields from each document.

**Core aggregation stage** · Reshape documents. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$unset": [
    "internal",
    "address.secret"
  ]
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `fields` | Yes | A field-name string or an array of field-name strings. Dotted paths traverse nested objects. |

## Behavior

- Other fields remain in the output. Missing paths are ignored.
- The handler copies the top-level object only; nested removal can affect shared nested maps in direct Core calls.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $unset stage requires a string or list of field names |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "name": "Pen",
    "internal": 1,
    "address": {
      "city": "Toronto",
      "secret": 2
    }
  }
]
```

Pipeline:
```json
[
  {
    "$unset": [
      "internal",
      "address.secret"
    ]
  }
]
```

Result:
```json
[
  {
    "name": "Pen",
    "address": {
      "city": "Toronto"
    }
  }
]
```

### Missing field

Input documents:
```json
[
  {
    "name": "Pen"
  }
]
```

Pipeline:
```json
[
  {
    "$unset": "unknown"
  }
]
```

Result:
```json
[
  {
    "name": "Pen"
  }
]
```

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/unset.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.


[MongoDB $unset reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

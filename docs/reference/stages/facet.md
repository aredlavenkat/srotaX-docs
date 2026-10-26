# $facet

## Definition

Runs named child pipelines over the same input list and collects their results.

**Core aggregation stage** · Combine pipelines. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$facet": {
    "first": [
      {
        "$limit": 1
      }
    ],
    "names": [
      {
        "$project": {
          "name": 1
        }
      }
    ]
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `name: pipeline` | Yes | Output field name mapped to an array of stage objects. |

## Behavior

- Returns one object with an array for each named branch, including empty branch results.
- Each branch receives a top-level copy of each input document. Nested objects are not deeply isolated by this handler.
- Unknown branch stages and non-array branch pipelines raise errors.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [{"first":[],"names":[]}] |
| invalid specification (`null`) | Error: IllegalArgumentException — $facet stage requires an object as its argument |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "name": "A"
  },
  {
    "name": "B"
  }
]
```

Pipeline:
```json
[
  {
    "$facet": {
      "first": [
        {
          "$limit": 1
        }
      ],
      "names": [
        {
          "$project": {
            "name": 1
          }
        }
      ]
    }
  }
]
```

Result:
```json
[
  {
    "first": [
      {
        "name": "A"
      }
    ],
    "names": [
      {
        "name": "A"
      },
      {
        "name": "B"
      }
    ]
  }
]
```

## Verification

The 3 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/facet.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- No MongoDB memory-size or disk-spill behavior is provided by this in-memory handler.

[MongoDB $facet reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/facet/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

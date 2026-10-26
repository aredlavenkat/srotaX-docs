# $subPipeline

## Definition

Executes inline child pipelines or resolves child references through the caller’s execution context.

**Core aggregation stage** · Core extensions. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$subPipeline": [
    {
      "pipeline": [
        {
          "$set": {
            "approved": true
          }
        }
      ]
    }
  ]
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `steps` | Yes | Array of child entries, executed sequentially. |
| `pipeline or ref` | One per child | Inline stage array or reference resolved by the host. `version` can accompany ref. |
| `input` | No | Expression selecting child input documents. |
| `output` | No | Destination for a child result; mapped children must return exactly one document. |
| `when` | No | Boolean expression controlling whether a child runs. |
| `globals` | No | Child global-variable overrides. |
| `onError` | No | `"bubble"`, `"skip"`, or inherited behavior. |
| `parallel / merge` | No | Parallel child array; merge modes `"concat"`, `"zip"`, or `"facet"`. |

## Behavior

- A reference requires a resolver in the execution context; there is no global pipeline registry.
- Mapped output preserves the parent and inserts the child result.
- This is the Core mechanism behind host-managed composition. Configure SrotaX asset dependencies through Call Flow, not raw registry names.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $subPipeline requires an array of steps |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "orderId": "A"
  }
]
```

Pipeline:
```json
[
  {
    "$subPipeline": [
      {
        "pipeline": [
          {
            "$set": {
              "approved": true
            }
          }
        ]
      }
    ]
  }
]
```

Result:
```json
[
  {
    "orderId": "A",
    "approved": true
  }
]
```

### Missing resolver

Input documents:
```json
[
  {
    "orderId": "A"
  }
]
```

Pipeline:
```json
[
  {
    "$subPipeline": [
      {
        "ref": "unknown"
      }
    ]
  }
]
```

**Observed error:** Unknown pinned sub-pipeline: unknown

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/subPipeline.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- `$subPipeline` is a Core extension, not a MongoDB stage.

<!-- END MONGO PARITY -->

# $lookup

## Definition

Adds matching records from a host-provided in-memory dataset.

**Core aggregation stage** · Combine pipelines. Use this syntax in a Core pipeline; Studio availability depends on the Flow compiler.

## Syntax

Basic form, with concrete values:
```json
{
  "$lookup": {
    "from": [
      {
        "sku": "P1",
        "price": 5
      }
    ],
    "localField": "sku",
    "foreignField": "sku",
    "as": "products"
  }
}
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `from` | Yes | Array/object of foreign records, or a dataset name provided in execution globals under `foreignCollections`. |
| `localField` | Yes | Local join field path. |
| `foreignField` | Yes | Foreign join field path. |
| `as` | No | Output field containing matched foreign records. Defaults to `results`. |
| `cacheOptions` | No | Cache settings; `maxEntries` defaults to 1024 distinct keys. Size the host dataset accordingly. |

## Behavior

- There is no database connection or collection read. The host supplies all records.
- No match yields an empty array. Lookup uses key equality in the in-memory index.
- An index stops loading after its configured key limit; large datasets can therefore omit matches.
- A named dataset must be present even when input is empty.

### Empty input and invalid specification

These cases use the basic form above unless the specification is explicitly replaced.

| Case | Observed result |
| --- | --- |
| empty input | [] |
| invalid specification (`null`) | Error: IllegalArgumentException — $lookup stage expects an object specification |

## Examples

### Basic pipeline

Input documents:
```json
[
  {
    "sku": "P1"
  },
  {
    "sku": "P2"
  }
]
```

Pipeline:
```json
[
  {
    "$lookup": {
      "from": [
        {
          "sku": "P1",
          "price": 5
        }
      ],
      "localField": "sku",
      "foreignField": "sku",
      "as": "products"
    }
  }
]
```

Result:
```json
[
  {
    "sku": "P1",
    "products": [
      {
        "sku": "P1",
        "price": 5
      }
    ]
  },
  {
    "sku": "P2",
    "products": []
  }
]
```

### Missing named dataset

Input documents:
```json
[
  {
    "sku": "P1"
  }
]
```

Pipeline:
```json
[
  {
    "$lookup": {
      "from": "products",
      "localField": "sku",
      "foreignField": "sku",
      "as": "products"
    }
  }
]
```

**Observed error:** foreign collection 'products' not available

## Verification

The 4 examples on this page were executed through Core PipelineExecutor with a fresh context for each case. They establish the displayed behavior, not all possible option combinations.

[Download the executable cases and recorded results](../../downloads/stage-behavior/lookup.json).

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Stage examples were executed in Core. They were **not** compared live with MongoDB in the expression parity suite.

- Database collection access, correlated lookup pipelines and MongoDB index behavior are not implemented.

[MongoDB $lookup reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/). Read the Core behavior above before reusing MongoDB examples.

<!-- END MONGO PARITY -->

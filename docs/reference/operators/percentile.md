# $percentile

Computes single-document statistics, ignoring nonnumeric values.

**Category:** Statistics. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ANY | Yes | Expression evaluated against the input |
| `p` | ARRAY | Yes | Literal configuration |
| `method` | STRING | Yes | Literal configuration |

Argument count: minimum 3; maximum 3.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$percentile": {
    "input": [
      10,
      20,
      30,
      40
    ],
    "p": [
      0,
      0.5,
      1
    ],
    "method": "approximate"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [10.0,20.0,40.0].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | [null,null,null] |
| missing | Field absent | [null,null,null] |
| zero | 0 | [0.0,0.0,0.0] |
| negative | -2 | [-2.0,-2.0,-2.0] |
| decimal | 2.5 | [2.5,2.5,2.5] |
| numeric string | "12" | [null,null,null] |
| text | "hello" | [null,null,null] |
| empty string | "" | [null,null,null] |
| boolean | true | [null,null,null] |
| false | false | [null,null,null] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | [null,null,null] |
| decimal128 | {"$numberDecimal":"1.25"} | [1.25,1.25,1.25] |
| empty array | [] | [null,null,null] |
| numeric array | [1,2,3] | [1.0,2.0,3.0] |
| mixed array | [1,null,"x",3] | [1.0,1.0,3.0] |
| nested array | [[1,2],[3]] | [null,null,null] |
| empty object | {} | [null,null,null] |
| object | {"x":1} | [null,null,null] |
| ISO date string | "2026-01-15T15:00:00Z" | [null,null,null] |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $percentile requires [method, p, input] |

### Argument: `p`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $percentile p must be an array |
| zero | 0 | Error: IllegalArgumentException — $percentile p must be an array |
| negative | -2 | Error: IllegalArgumentException — $percentile p must be an array |
| decimal | 2.5 | Error: IllegalArgumentException — $percentile p must be an array |
| numeric string | "12" | Error: IllegalArgumentException — $percentile p must be an array |
| text | "hello" | Error: IllegalArgumentException — $percentile p must be an array |
| empty string | "" | Error: IllegalArgumentException — $percentile p must be an array |
| boolean | true | Error: IllegalArgumentException — $percentile p must be an array |
| false | false | Error: IllegalArgumentException — $percentile p must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $percentile p must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $percentile p must be an array |
| empty array | [] | Error: IllegalArgumentException — $percentile p must be an array |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $percentile p values must be numbers from 0 to 1 |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $percentile p values must be numbers from 0 to 1 |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $percentile p values must be numbers from 0 to 1 |
| empty object | {} | Error: IllegalArgumentException — $percentile p must be an array |
| object | {"x":1} | Error: IllegalArgumentException — $percentile p must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $percentile p must be an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $percentile requires [method, p, input] |

### Argument: `method`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| zero | 0 | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| negative | -2 | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| decimal | 2.5 | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| numeric string | "12" | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| text | "hello" | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| empty string | "" | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| boolean | true | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| false | false | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| empty array | [] | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| empty object | {} | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| object | {"x":1} | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $percentile method must be the literal string approximate |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $percentile requires [method, p, input] |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$percentile":[]} | Error: IllegalArgumentException — $percentile requires [method, p, input] |
| {"$percentile":{"unexpected":1}} | Error: IllegalArgumentException — $percentile requires [method, p, input] |

## Additional boundary examples

<details>
<summary>Show 25 tested examples</summary>

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    10,
    20,
    30
  ]
}
```

**SrotaX:** [30.0,10.0,10.0,20.0,30.0,20.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    10,
    20,
    30,
    40
  ]
}
```

**SrotaX:** [40.0,10.0,10.0,20.0,30.0,20.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": []
}
```

**SrotaX:** [null,null,null,null,null,null].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": null
}
```

**SrotaX:** [null,null,null,null,null,null].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": 5
}
```

**SrotaX:** [5.0,5.0,5.0,5.0,5.0,5.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    1,
    "x",
    null,
    3
  ]
}
```

**SrotaX:** [3.0,1.0,1.0,1.0,3.0,1.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    1,
    [
      50
    ],
    3
  ]
}
```

**SrotaX:** [3.0,1.0,1.0,1.0,3.0,1.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    "x",
    null,
    {}
  ]
}
```

**SrotaX:** [null,null,null,null,null,null].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    1,
    {
      "$numberDouble": "NaN"
    },
    3
  ]
}
```

**SrotaX:** [3.0,1.0,1.0,1.0,3.0,1.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    1,
    {
      "$numberDouble": "Infinity"
    },
    3
  ]
}
```

**SrotaX:** [Infinity,1.0,1.0,3.0,Infinity,3.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    {
      "$numberDecimal": "1.2"
    },
    2,
    3
  ]
}
```

**SrotaX:** [3.0,1.2,1.2,2.0,3.0,2.0].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    1e+100,
    2e+100,
    3e+100
  ]
}
```

**SrotaX:** [3e+100,1e+100,1e+100,2e+100,3e+100,2e+100].

Expression:
```json
{
  "$percentile": {
    "input": "$values",
    "method": "approximate",
    "p": [
      1,
      0,
      0.25,
      0.5,
      0.75,
      0.5
    ]
  }
}
```

Input:
```json
{
  "values": [
    {
      "$numberDouble": "Infinity"
    }
  ]
}
```

**SrotaX:** [Infinity,Infinity,Infinity,Infinity,Infinity,Infinity].

Expression:
```json
{
  "$percentile": {
    "input": "$missing",
    "method": "approximate",
    "p": [
      0,
      0.5,
      1
    ]
  }
}
```

Input:
```json
{}
```

**SrotaX:** [null,null,null].

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3
    ],
    "method": "continuous",
    "p": [
      0.5
    ]
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $percentile method must be the literal string approximate.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3
    ],
    "method": null,
    "p": [
      0.5
    ]
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $percentile method must be the literal string approximate.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3
    ],
    "method": {
      "$literal": "approximate"
    },
    "p": [
      0.5
    ]
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $percentile method must be the literal string approximate.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": []
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** Error: IllegalArgumentException — $percentile p must be an array.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": [
      -1
    ]
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** Error: IllegalArgumentException — $percentile p values must be numbers from 0 to 1.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": [
      1.1
    ]
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** Error: IllegalArgumentException — $percentile p values must be numbers from 0 to 1.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": [
      "0.5"
    ]
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** Error: IllegalArgumentException — $percentile p values must be numbers from 0 to 1.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": [
      null
    ]
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** Error: IllegalArgumentException — $percentile p values must be numbers from 0 to 1.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": {
      "$literal": [
        0.5
      ]
    }
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** [2.0].

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": "$ps"
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** Error: IllegalArgumentException — $percentile p must be constant.

Expression:
```json
{
  "$percentile": {
    "input": [
      1,
      2,
      3,
      4
    ],
    "method": "approximate",
    "p": [
      {
        "$divide": [
          1,
          2
        ]
      }
    ]
  }
}
```

Input:
```json
{
  "ps": [
    0.5
  ]
}
```

**SrotaX:** [2.0].

</details>

## Scope and reproducibility

This page records **86 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/percentile.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **36 exact BSON matches**, **50 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/percentile.json).

<!-- END MONGO PARITY -->

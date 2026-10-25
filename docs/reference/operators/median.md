# $median

Computes single-document statistics, ignoring nonnumeric values.

**Category:** Statistics. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ANY | Yes | Expression evaluated against the input |
| `method` | STRING | Yes | Literal configuration |

Argument count: minimum 2; maximum 2.

Declared result types: **DOUBLE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$median": {
    "input": [
      10,
      20,
      30,
      40
    ],
    "method": "approximate"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 20.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | -2.0 (double) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | null |
| boolean | true | null |
| false | false | null |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | null |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (double) |
| empty array | [] | null |
| numeric array | [1,2,3] | 2.0 (double) |
| mixed array | [1,null,"x",3] | 1.0 (double) |
| nested array | [[1,2],[3]] | null |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | null |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $median requires [input, method] |

### Argument: `method`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $median method must be the literal string approximate |
| zero | 0 | Error: IllegalArgumentException — $median method must be the literal string approximate |
| negative | -2 | Error: IllegalArgumentException — $median method must be the literal string approximate |
| decimal | 2.5 | Error: IllegalArgumentException — $median method must be the literal string approximate |
| numeric string | "12" | Error: IllegalArgumentException — $median method must be the literal string approximate |
| text | "hello" | Error: IllegalArgumentException — $median method must be the literal string approximate |
| empty string | "" | Error: IllegalArgumentException — $median method must be the literal string approximate |
| boolean | true | Error: IllegalArgumentException — $median method must be the literal string approximate |
| false | false | Error: IllegalArgumentException — $median method must be the literal string approximate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $median method must be the literal string approximate |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $median method must be the literal string approximate |
| empty array | [] | Error: IllegalArgumentException — $median method must be the literal string approximate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $median method must be the literal string approximate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $median method must be the literal string approximate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $median method must be the literal string approximate |
| empty object | {} | Error: IllegalArgumentException — $median method must be the literal string approximate |
| object | {"x":1} | Error: IllegalArgumentException — $median method must be the literal string approximate |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $median method must be the literal string approximate |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $median requires [input, method] |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$median":[]} | Error: IllegalArgumentException — $median requires [input, method] |
| {"$median":{"unexpected":1}} | Error: IllegalArgumentException — $median requires [input, method] |

## Additional boundary examples

<details>
<summary>Show 17 tested examples</summary>

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 20.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 20.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": []
}
```

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": null
}
```

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": 5
}
```

**SrotaX:** 5.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 3.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 2.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** 2.0E100 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
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

**SrotaX:** Infinity (double).

Expression:
```json
{
  "$median": {
    "input": "$missing",
    "method": "approximate"
  }
}
```

Input:
```json
{}
```

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": [
      1,
      2,
      3
    ],
    "method": "continuous"
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $median method must be the literal string approximate.

Expression:
```json
{
  "$median": {
    "input": [
      1,
      2,
      3
    ],
    "method": null
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $median method must be the literal string approximate.

Expression:
```json
{
  "$median": {
    "input": [
      1,
      2,
      3
    ],
    "method": {
      "$literal": "approximate"
    }
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $median method must be the literal string approximate.

</details>

## Scope and reproducibility

This page records **59 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/median.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **34 exact BSON matches**, **25 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/median.json).

<!-- END MONGO PARITY -->

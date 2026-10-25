# $stdDevPop

Computes single-document statistics, ignoring nonnumeric values.

**Category:** Statistics. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `value` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 0; maximum variadic.

Declared result types: **DOUBLE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$stdDevPop": [
    10,
    10,
    10
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 0.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `value[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 0.0 (double) |
| missing | Field absent | 0.0 (double) |
| zero | 0 | 4.714045207910316 (double) |
| negative | -2 | 5.656854249492381 (double) |
| decimal | 2.5 | 3.5355339059327378 (double) |
| numeric string | "12" | 0.0 (double) |
| text | "hello" | 0.0 (double) |
| empty string | "" | 0.0 (double) |
| boolean | true | 0.0 (double) |
| false | false | 0.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 4.124789556921527 (double) |
| empty array | [] | 0.0 (double) |
| numeric array | [1,2,3] | 0.0 (double) |
| mixed array | [1,null,"x",3] | 0.0 (double) |
| nested array | [[1,2],[3]] | 0.0 (double) |
| empty object | {} | 0.0 (double) |
| object | {"x":1} | 0.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 0.0 (double) |

### Argument: `value[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 0.0 (double) |
| missing | Field absent | 0.0 (double) |
| zero | 0 | 4.714045207910316 (double) |
| negative | -2 | 5.656854249492381 (double) |
| decimal | 2.5 | 3.5355339059327378 (double) |
| numeric string | "12" | 0.0 (double) |
| text | "hello" | 0.0 (double) |
| empty string | "" | 0.0 (double) |
| boolean | true | 0.0 (double) |
| false | false | 0.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 4.124789556921527 (double) |
| empty array | [] | 0.0 (double) |
| numeric array | [1,2,3] | 0.0 (double) |
| mixed array | [1,null,"x",3] | 0.0 (double) |
| nested array | [[1,2],[3]] | 0.0 (double) |
| empty object | {} | 0.0 (double) |
| object | {"x":1} | 0.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 0.0 (double) |

### Argument: `value[2]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 0.0 (double) |
| missing | Field absent | 0.0 (double) |
| zero | 0 | 4.714045207910316 (double) |
| negative | -2 | 5.656854249492381 (double) |
| decimal | 2.5 | 3.5355339059327378 (double) |
| numeric string | "12" | 0.0 (double) |
| text | "hello" | 0.0 (double) |
| empty string | "" | 0.0 (double) |
| boolean | true | 0.0 (double) |
| false | false | 0.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 4.124789556921527 (double) |
| empty array | [] | 0.0 (double) |
| numeric array | [1,2,3] | 0.0 (double) |
| mixed array | [1,null,"x",3] | 0.0 (double) |
| nested array | [[1,2],[3]] | 0.0 (double) |
| empty object | {} | 0.0 (double) |
| object | {"x":1} | 0.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 0.0 (double) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$stdDevPop":[]} | null |
| {"$stdDevPop":{"unexpected":1}} | null |

## Additional boundary examples

<details>
<summary>Show 21 tested examples</summary>

Expression:
```json
{
  "$stdDevPop": "$values"
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

**SrotaX:** 8.16496580927726 (double).

Expression:
```json
{
  "$stdDevPop": "$values"
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

**SrotaX:** 11.180339887498949 (double).

Expression:
```json
{
  "$stdDevPop": "$values"
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
  "$stdDevPop": "$values"
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
  "$stdDevPop": "$values"
}
```

Input:
```json
{
  "values": 5
}
```

**SrotaX:** 0.0 (double).

Expression:
```json
{
  "$stdDevPop": "$values"
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
  "$stdDevPop": "$values"
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
  "$stdDevPop": "$values"
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
  "$stdDevPop": "$values"
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

**SrotaX:** NaN (double).

Expression:
```json
{
  "$stdDevPop": "$values"
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

**SrotaX:** NaN (double).

Expression:
```json
{
  "$stdDevPop": "$values"
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

**SrotaX:** 0.7363574011458173 (double).

Expression:
```json
{
  "$stdDevPop": "$values"
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

**SrotaX:** 8.164965809277259E99 (double).

Expression:
```json
{
  "$stdDevPop": "$values"
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

**SrotaX:** NaN (double).

Expression:
```json
{
  "$stdDevPop": "$missing"
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
  "$stdDevPop": []
}
```

Input:
```json
{
  "values": [
    1,
    2,
    3
  ]
}
```

**SrotaX:** null.

Expression:
```json
{
  "$stdDevPop": [
    1
  ]
}
```

Input:
```json
{
  "values": [
    1,
    2,
    3
  ]
}
```

**SrotaX:** 0.0 (double).

Expression:
```json
{
  "$stdDevPop": [
    1,
    2,
    3
  ]
}
```

Input:
```json
{
  "values": [
    1,
    2,
    3
  ]
}
```

**SrotaX:** 0.816496580927726 (double).

Expression:
```json
{
  "$stdDevPop": [
    "$values"
  ]
}
```

Input:
```json
{
  "values": [
    1,
    2,
    3
  ]
}
```

**SrotaX:** 0.816496580927726 (double).

Expression:
```json
{
  "$stdDevPop": [
    "$values",
    7
  ]
}
```

Input:
```json
{
  "values": [
    1,
    2,
    3
  ]
}
```

**SrotaX:** 0.0 (double).

Expression:
```json
{
  "$stdDevPop": [
    null,
    "x"
  ]
}
```

Input:
```json
{
  "values": [
    1,
    2,
    3
  ]
}
```

**SrotaX:** null.

Expression:
```json
{
  "$stdDevPop": [
    1e+16,
    1.0000000000000002e+16,
    1.0000000000000004e+16
  ]
}
```

Input:
```json
{
  "values": [
    1,
    2,
    3
  ]
}
```

**SrotaX:** 2.0 (double).

</details>

## Scope and reproducibility

This page records **81 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/stdDevPop.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **79 exact BSON matches**, **0 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| value[0] / zero | 4.714045207910316 (double) | 4.714045207910317 (double) |
| value[1] / zero | 4.714045207910316 (double) | 4.714045207910317 (double) |

[Download full comparison evidence](../../downloads/operator-parity/stdDevPop.json).

<!-- END MONGO PARITY -->

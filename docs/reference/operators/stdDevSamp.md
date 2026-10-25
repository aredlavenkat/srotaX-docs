# $stdDevSamp

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
  "$stdDevSamp": [
    10,
    20,
    30
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 10.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `value[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 7.0710678118654755 (double) |
| missing | Field absent | 7.0710678118654755 (double) |
| zero | 0 | 15.275252316519467 (double) |
| negative | -2 | 16.3707055437449 (double) |
| decimal | 2.5 | 13.919410907075054 (double) |
| numeric string | "12" | 7.0710678118654755 (double) |
| text | "hello" | 7.0710678118654755 (double) |
| empty string | "" | 7.0710678118654755 (double) |
| boolean | true | 7.0710678118654755 (double) |
| false | false | 7.0710678118654755 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 7.0710678118654755 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 14.595233240114162 (double) |
| empty array | [] | 7.0710678118654755 (double) |
| numeric array | [1,2,3] | 7.0710678118654755 (double) |
| mixed array | [1,null,"x",3] | 7.0710678118654755 (double) |
| nested array | [[1,2],[3]] | 7.0710678118654755 (double) |
| empty object | {} | 7.0710678118654755 (double) |
| object | {"x":1} | 7.0710678118654755 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 7.0710678118654755 (double) |

### Argument: `value[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 14.142135623730951 (double) |
| missing | Field absent | 14.142135623730951 (double) |
| zero | 0 | 15.275252316519467 (double) |
| negative | -2 | 16.165807537309522 (double) |
| decimal | 2.5 | 14.215601757693317 (double) |
| numeric string | "12" | 14.142135623730951 (double) |
| text | "hello" | 14.142135623730951 (double) |
| empty string | "" | 14.142135623730951 (double) |
| boolean | true | 14.142135623730951 (double) |
| false | false | 14.142135623730951 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 14.142135623730951 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 14.737282653189496 (double) |
| empty array | [] | 14.142135623730951 (double) |
| numeric array | [1,2,3] | 14.142135623730951 (double) |
| mixed array | [1,null,"x",3] | 14.142135623730951 (double) |
| nested array | [[1,2],[3]] | 14.142135623730951 (double) |
| empty object | {} | 14.142135623730951 (double) |
| object | {"x":1} | 14.142135623730951 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 14.142135623730951 (double) |

### Argument: `value[2]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 7.0710678118654755 (double) |
| missing | Field absent | 7.0710678118654755 (double) |
| zero | 0 | 10.0 (double) |
| negative | -2 | 11.015141094572204 (double) |
| decimal | 2.5 | 8.779711460710615 (double) |
| numeric string | "12" | 7.0710678118654755 (double) |
| text | "hello" | 7.0710678118654755 (double) |
| empty string | "" | 7.0710678118654755 (double) |
| boolean | true | 7.0710678118654755 (double) |
| false | false | 7.0710678118654755 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 7.0710678118654755 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 9.38194187433142 (double) |
| empty array | [] | 7.0710678118654755 (double) |
| numeric array | [1,2,3] | 7.0710678118654755 (double) |
| mixed array | [1,null,"x",3] | 7.0710678118654755 (double) |
| nested array | [[1,2],[3]] | 7.0710678118654755 (double) |
| empty object | {} | 7.0710678118654755 (double) |
| object | {"x":1} | 7.0710678118654755 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 7.0710678118654755 (double) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$stdDevSamp":[]} | null |
| {"$stdDevSamp":{"unexpected":1}} | null |

## Additional boundary examples

<details>
<summary>Show 21 tested examples</summary>

Expression:
```json
{
  "$stdDevSamp": "$values"
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

**SrotaX:** 10.0 (double).

Expression:
```json
{
  "$stdDevSamp": "$values"
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

**SrotaX:** 12.909944487358056 (double).

Expression:
```json
{
  "$stdDevSamp": "$values"
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
  "$stdDevSamp": "$values"
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
  "$stdDevSamp": "$values"
}
```

Input:
```json
{
  "values": 5
}
```

**SrotaX:** null.

Expression:
```json
{
  "$stdDevSamp": "$values"
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

**SrotaX:** 1.4142135623730951 (double).

Expression:
```json
{
  "$stdDevSamp": "$values"
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

**SrotaX:** 1.4142135623730951 (double).

Expression:
```json
{
  "$stdDevSamp": "$values"
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
  "$stdDevSamp": "$values"
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
  "$stdDevSamp": "$values"
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
  "$stdDevSamp": "$values"
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

**SrotaX:** 0.9018499505645787 (double).

Expression:
```json
{
  "$stdDevSamp": "$values"
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

**SrotaX:** 9.999999999999998E99 (double).

Expression:
```json
{
  "$stdDevSamp": "$values"
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

**SrotaX:** null.

Expression:
```json
{
  "$stdDevSamp": "$missing"
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
  "$stdDevSamp": []
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
  "$stdDevSamp": [
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

**SrotaX:** null.

Expression:
```json
{
  "$stdDevSamp": [
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

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$stdDevSamp": [
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

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$stdDevSamp": [
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

**SrotaX:** null.

Expression:
```json
{
  "$stdDevSamp": [
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
  "$stdDevSamp": [
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

**SrotaX:** 2.449489742783178 (double).

</details>

## Scope and reproducibility

This page records **81 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/stdDevSamp.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **81 exact BSON matches**, **0 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/stdDevSamp.json).

<!-- END MONGO PARITY -->

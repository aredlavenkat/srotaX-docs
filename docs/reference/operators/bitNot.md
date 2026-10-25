# $bitNot

Flips int32 or int64 bits, preserving integer width.

**Category:** Bitwise. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `value` | INT, LONG, MISSING, NULL | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **INT, LONG, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$bitNot": 5
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** -6 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `value`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | -1 (int32) |
| negative | -2 | 1 (int32) |
| decimal | 2.5 | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| numeric string | "12" | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| text | "hello" | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| empty string | "" | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| boolean | true | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| false | false | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| empty array | [] | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| empty object | {} | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| object | {"x":1} | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$bitNot":[]} | Error: IllegalArgumentException — $bitNot requires exactly one operand |
| {"$bitNot":{"unexpected":1}} | Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |

## Additional boundary examples

<details>
<summary>Show 15 tested examples</summary>

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": 5
}
```

**SrotaX:** -6 (int32).

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": {
    "$numberLong": "5"
  }
}
```

**SrotaX:** -6 (int64).

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": -2147483648
}
```

**SrotaX:** 2147483647 (int32).

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": {
    "$numberLong": "-9223372036854775808"
  }
}
```

**SrotaX:** 9223372036854775807 (int64).

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": null
}
```

**SrotaX:** null.

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": 5.0
}
```

**SrotaX:** Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": {
    "$numberDecimal": "5"
  }
}
```

**SrotaX:** Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": "5"
}
```

**SrotaX:** Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

Expression:
```json
{
  "$bitNot": "$value"
}
```

Input:
```json
{
  "value": [
    5
  ]
}
```

**SrotaX:** Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

Expression:
```json
{
  "$bitNot": [
    5
  ]
}
```

Input:
```json
{}
```

**SrotaX:** -6 (int32).

Expression:
```json
{
  "$bitNot": []
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $bitNot requires exactly one operand.

Expression:
```json
{
  "$bitNot": [
    1,
    2
  ]
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $bitNot requires exactly one operand.

Expression:
```json
{
  "$bitNot": "$missing"
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
  "$bitNot": {
    "$toInt": 5.5
  }
}
```

Input:
```json
{}
```

**SrotaX:** -6 (int32).

Expression:
```json
{
  "$bitNot": {
    "$literal": [
      5
    ]
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

</details>

## Scope and reproducibility

This page records **37 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/bitNot.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **13 exact BSON matches**, **24 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/bitNot.json).

<!-- END MONGO PARITY -->

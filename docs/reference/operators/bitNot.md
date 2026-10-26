# $bitNot

## Definition

Flips int32 or int64 bits, preserving integer width.

**Expression operator** · Bitwise · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$bitNot": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to evaluate.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `value` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| numeric string | "12" | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| text | "hello" | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| boolean | true | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| empty array | [] | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| numeric array | [1,2,3] | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| object | {"x":1} | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$bitNot":[]} | Error — $bitNot requires exactly one operand |
| {"$bitNot":{"unexpected":1}} | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `value`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | -1 (int32) |
| negative | -2 | 1 (int32) |
| decimal | 2.5 | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| numeric string | "12" | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| text | "hello" | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| empty string | "" | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| boolean | true | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| false | false | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| empty array | [] | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| numeric array | [1,2,3] | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| mixed array | [1,null,"x",3] | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| nested array | [[1,2],[3]] | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| empty object | {} | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| object | {"x":1} | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly |


</details>

## Additional boundary examples

<details markdown="1">
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

**SrotaX:** Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

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

**SrotaX:** Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

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

**SrotaX:** Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

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

**SrotaX:** Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

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

**SrotaX:** Error — $bitNot requires exactly one operand.

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

**SrotaX:** Error — $bitNot requires exactly one operand.

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

**SrotaX:** Error — $bitNot requires an int32 or int64; use $toInt or $toLong explicitly.

</details>

## Verification

This page records **37 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/bitNot.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **13 exact BSON matches**, **24 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/bitNot.json).

<!-- END MONGO PARITY -->

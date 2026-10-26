# $stdDevPop

## Definition

Computes single-document statistics, ignoring nonnumeric values.

**Expression operator** · Statistics · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$stdDevPop": [ <value>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | See argument count below | Expression supplying the value to evaluate. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `value` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | 0.0 (double) |
| missing | Field absent | 0.0 (double) |
| decimal | 2.5 | 3.5355339059327378 (double) |
| numeric string | "12" | 0.0 (double) |
| text | "hello" | 0.0 (double) |
| boolean | true | 0.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0.0 (double) |
| empty array | [] | 0.0 (double) |
| numeric array | [1,2,3] | 0.0 (double) |
| object | {"x":1} | 0.0 (double) |
| null | null | 0.0 (double) |
| missing | Field absent | 0.0 (double) |
| decimal | 2.5 | 3.5355339059327378 (double) |
| numeric string | "12" | 0.0 (double) |
| text | "hello" | 0.0 (double) |
| boolean | true | 0.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0.0 (double) |
| empty array | [] | 0.0 (double) |
| numeric array | [1,2,3] | 0.0 (double) |
| object | {"x":1} | 0.0 (double) |
| null | null | 0.0 (double) |
| missing | Field absent | 0.0 (double) |
| decimal | 2.5 | 3.5355339059327378 (double) |
| numeric string | "12" | 0.0 (double) |
| text | "hello" | 0.0 (double) |
| boolean | true | 0.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0.0 (double) |
| empty array | [] | 0.0 (double) |
| numeric array | [1,2,3] | 0.0 (double) |
| object | {"x":1} | 0.0 (double) |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$stdDevPop":[]} | null |
| {"$stdDevPop":{"unexpected":1}} | null |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `value[0]`**

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

**Argument: `value[1]`**

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

**Argument: `value[2]`**

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


</details>

## Additional boundary examples

<details markdown="1">
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

## Verification

This page records **81 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/stdDevPop.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **79 exact BSON matches**, **0 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| value[0] / zero | 4.714045207910316 (double) | 4.714045207910317 (double) |
| value[1] / zero | 4.714045207910316 (double) | 4.714045207910317 (double) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/stdDevPop.json).

<!-- END MONGO PARITY -->

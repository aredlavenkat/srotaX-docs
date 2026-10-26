# $subtract

## Definition

Subtracts numbers, subtracts a millisecond offset from a date, or returns the millisecond difference between two dates.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$subtract": [ <left>, <right> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `left` | Yes | Expression to subtract from. |
| `right` | Yes | Expression to subtract. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `left` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | 0.5 (double) |
| numeric string | "12" | Error — $subtract only supports numeric types. |
| text | "hello" | Error — $subtract only supports numeric types. |
| boolean | true | Error — $subtract only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489199998'} (date) |
| empty array | [] | Error — $subtract only supports numeric types. |
| numeric array | [1,2,3] | Error — $subtract only supports numeric types. |
| object | {"x":1} | Error — $subtract only supports numeric types. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$subtract":[]} | Error — $subtract requires exactly two arguments. |
| {"$subtract":{"unexpected":1}} | Error — $subtract requires exactly two arguments. |

## Examples

Expression:
```json
{
  "$subtract": [
    5,
    2
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `left[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | -2.0 (double) |
| negative | -2 | -4.0 (double) |
| decimal | 2.5 | 0.5 (double) |
| numeric string | "12" | Error — $subtract only supports numeric types. |
| text | "hello" | Error — $subtract only supports numeric types. |
| empty string | "" | Error — $subtract only supports numeric types. |
| boolean | true | Error — $subtract only supports numeric types. |
| false | false | Error — $subtract only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489199998'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | -0.75 (double) |
| empty array | [] | Error — $subtract only supports numeric types. |
| numeric array | [1,2,3] | Error — $subtract only supports numeric types. |
| mixed array | [1,null,"x",3] | Error — $subtract only supports numeric types. |
| nested array | [[1,2],[3]] | Error — $subtract only supports numeric types. |
| empty object | {} | Error — $subtract only supports numeric types. |
| object | {"x":1} | Error — $subtract only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $subtract only supports numeric types. |

**Argument: `right[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 5.0 (double) |
| negative | -2 | 7.0 (double) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | Error — $subtract only supports numeric types. |
| text | "hello" | Error — $subtract only supports numeric types. |
| empty string | "" | Error — $subtract only supports numeric types. |
| boolean | true | Error — $subtract only supports numeric types. |
| false | false | Error — $subtract only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $subtract only supports numeric types. |
| decimal128 | {"$numberDecimal":"1.25"} | 3.75 (double) |
| empty array | [] | Error — $subtract only supports numeric types. |
| numeric array | [1,2,3] | Error — $subtract only supports numeric types. |
| mixed array | [1,null,"x",3] | Error — $subtract only supports numeric types. |
| nested array | [[1,2],[3]] | Error — $subtract only supports numeric types. |
| empty object | {} | Error — $subtract only supports numeric types. |
| object | {"x":1} | Error — $subtract only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $subtract only supports numeric types. |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/subtract.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **27 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 3.0 (double) | 3 (int32) |
| left[0] / zero | -2.0 (double) | -2 (int32) |
| left[0] / negative | -4.0 (double) | -4 (int32) |
| left[0] / decimal128 | -0.75 (double) | -0.75 (decimal128) |
| right[1] / zero | 5.0 (double) | 5 (int32) |
| right[1] / negative | 7.0 (double) | 7 (int32) |
| right[1] / decimal128 | 3.75 (double) | 3.75 (decimal128) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/subtract.json).

<!-- END MONGO PARITY -->

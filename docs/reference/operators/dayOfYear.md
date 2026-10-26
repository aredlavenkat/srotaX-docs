# $dayOfYear

## Definition

Extracts day of year using the host calendar.

**Expression operator** · Dates · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$dayOfYear": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $dayofyear requires a Date input |
| missing | Field absent | Error — $dayofyear requires a Date input |
| decimal | 2.5 | Error — $dayofyear requires a Date input |
| numeric string | "12" | Error — $dayofyear requires a Date input |
| text | "hello" | Error — $dayofyear requires a Date input |
| boolean | true | Error — $dayofyear requires a Date input |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 15 (int32) |
| empty array | [] | Error — $dayofyear requires a Date input |
| numeric array | [1,2,3] | Error — $dayofyear requires a Date input |
| object | {"x":1} | Error — $dayofyear requires a Date input |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$dayOfYear":[]} | Error — $dayofyear requires a Date input |
| {"$dayOfYear":{"unexpected":1}} | Error — $dayofyear requires a Date input |

## Examples

Expression:
```json
{
  "$dayOfYear": {
    "$toDate": "2024-01-02T03:04:05.006Z"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 1 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $dayofyear requires a Date input |
| missing | Field absent | Error — $dayofyear requires a Date input |
| zero | 0 | Error — $dayofyear requires a Date input |
| negative | -2 | Error — $dayofyear requires a Date input |
| decimal | 2.5 | Error — $dayofyear requires a Date input |
| numeric string | "12" | Error — $dayofyear requires a Date input |
| text | "hello" | Error — $dayofyear requires a Date input |
| empty string | "" | Error — $dayofyear requires a Date input |
| boolean | true | Error — $dayofyear requires a Date input |
| false | false | Error — $dayofyear requires a Date input |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 15 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $dayofyear requires a Date input |
| empty array | [] | Error — $dayofyear requires a Date input |
| numeric array | [1,2,3] | Error — $dayofyear requires a Date input |
| mixed array | [1,null,"x",3] | Error — $dayofyear requires a Date input |
| nested array | [[1,2],[3]] | Error — $dayofyear requires a Date input |
| empty object | {} | Error — $dayofyear requires a Date input |
| object | {"x":1} | Error — $dayofyear requires a Date input |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $dayofyear requires a Date input |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dayOfYear.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **1 exact BSON matches**, **18 both rejected**, **3 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 1 (int32) | 2 (int32) |
| input / null | Error — $dayofyear requires a Date input | null |
| input / missing | Error — $dayofyear requires a Date input | null |

</details>

[Download full comparison evidence](../../downloads/operator-parity/dayOfYear.json).

<!-- END MONGO PARITY -->

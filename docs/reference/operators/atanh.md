# $atanh

## Definition

Computes inverse hyperbolic tangent.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$atanh": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $atanh expects a numeric argument |
| missing | Field absent | Error — $atanh expects a numeric argument |
| decimal | 2.5 | Error — $atanh is defined for values between -1 and 1 |
| numeric string | "12" | Error — $atanh expects a numeric argument |
| text | "hello" | Error — $atanh expects a numeric argument |
| boolean | true | Error — $atanh expects a numeric argument |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $atanh expects a numeric argument |
| empty array | [] | Error — $atanh expects a numeric argument |
| numeric array | [1,2,3] | Error — $atanh expects a numeric argument |
| object | {"x":1} | Error — $atanh expects a numeric argument |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$atanh":[]} | Error — $atanh expects a numeric argument |
| {"$atanh":{"unexpected":1}} | Error — $atanh expects a numeric argument |

## Examples

Expression:
```json
{
  "$atanh": 0
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

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $atanh expects a numeric argument |
| missing | Field absent | Error — $atanh expects a numeric argument |
| zero | 0 | 0.0 (double) |
| negative | -2 | Error — $atanh is defined for values between -1 and 1 |
| decimal | 2.5 | Error — $atanh is defined for values between -1 and 1 |
| numeric string | "12" | Error — $atanh expects a numeric argument |
| text | "hello" | Error — $atanh expects a numeric argument |
| empty string | "" | Error — $atanh expects a numeric argument |
| boolean | true | Error — $atanh expects a numeric argument |
| false | false | Error — $atanh expects a numeric argument |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $atanh expects a numeric argument |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $atanh is defined for values between -1 and 1 |
| empty array | [] | Error — $atanh expects a numeric argument |
| numeric array | [1,2,3] | Error — $atanh expects a numeric argument |
| mixed array | [1,null,"x",3] | Error — $atanh expects a numeric argument |
| nested array | [[1,2],[3]] | Error — $atanh expects a numeric argument |
| empty object | {} | Error — $atanh expects a numeric argument |
| object | {"x":1} | Error — $atanh expects a numeric argument |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $atanh expects a numeric argument |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/atanh.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **18 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error — $atanh expects a numeric argument | null |
| input / missing | Error — $atanh expects a numeric argument | null |

</details>

[Download full comparison evidence](../../downloads/operator-parity/atanh.json).

<!-- END MONGO PARITY -->

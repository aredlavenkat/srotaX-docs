# $toUpper

## Definition

Converts text to upper case.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$toUpper": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | "" |
| missing | Field absent | "" |
| decimal | 2.5 | Error — $toUpper requires a string. |
| numeric string | "12" | "12" |
| text | "hello" | "HELLO" |
| boolean | true | Error — $toUpper requires a string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $toUpper requires a string. |
| empty array | [] | Error — $toUpper requires a string. |
| numeric array | [1,2,3] | Error — $toUpper requires a string. |
| object | {"x":1} | Error — $toUpper requires a string. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$toUpper":[]} | Error — $toUpper requires one argument |
| {"$toUpper":{"unexpected":1}} | Error — $toUpper requires a string. |

## Examples

Expression:
```json
{
  "$toUpper": "Ca"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "CA".

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | "" |
| missing | Field absent | "" |
| zero | 0 | Error — $toUpper requires a string. |
| negative | -2 | Error — $toUpper requires a string. |
| decimal | 2.5 | Error — $toUpper requires a string. |
| numeric string | "12" | "12" |
| text | "hello" | "HELLO" |
| empty string | "" | "" |
| boolean | true | Error — $toUpper requires a string. |
| false | false | Error — $toUpper requires a string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $toUpper requires a string. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $toUpper requires a string. |
| empty array | [] | Error — $toUpper requires a string. |
| numeric array | [1,2,3] | Error — $toUpper requires a string. |
| mixed array | [1,null,"x",3] | Error — $toUpper requires a string. |
| nested array | [[1,2],[3]] | Error — $toUpper requires a string. |
| empty object | {} | Error — $toUpper requires a string. |
| object | {"x":1} | Error — $toUpper requires a string. |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toUpper.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **10 both rejected**, **5 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / zero | Error — $toUpper requires a string. | "0" |
| input / negative | Error — $toUpper requires a string. | "-2" |
| input / decimal | Error — $toUpper requires a string. | "2.5" |
| input / typed date | Error — $toUpper requires a string. | "2026-01-15T15:00:00.000Z" |
| input / decimal128 | Error — $toUpper requires a string. | "1.25" |

</details>

[Download full comparison evidence](../../downloads/operator-parity/toUpper.json).

<!-- END MONGO PARITY -->

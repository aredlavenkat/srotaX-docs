# $toDate

## Definition

Converts a value to date.

**Expression operator** · Types and conversion · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$toDate": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | {'$numberLong': '2'} (date) |
| numeric string | "12" | Error — $convert failed for target date |
| text | "hello" | Error — $convert failed for target date |
| boolean | true | Error — $convert failed for target date |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| empty array | [] | Error — $convert failed for target date |
| numeric array | [1,2,3] | Error — $convert failed for target date |
| object | {"x":1} | Error — $convert failed for target date |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$toDate":[]} | Error — $toDate requires one argument |
| {"$toDate":{"unexpected":1}} | Error — $convert failed for target date |

## Examples

Expression:
```json
{
  "$toDate": "2024-01-02T00:00:00Z"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {'$numberLong': '1704153600000'} (date).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '0'} (date) |
| negative | -2 | {'$numberLong': '-2'} (date) |
| decimal | 2.5 | {'$numberLong': '2'} (date) |
| numeric string | "12" | Error — $convert failed for target date |
| text | "hello" | Error — $convert failed for target date |
| empty string | "" | Error — $convert failed for target date |
| boolean | true | Error — $convert failed for target date |
| false | false | Error — $convert failed for target date |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | {'$numberLong': '1'} (date) |
| empty array | [] | Error — $convert failed for target date |
| numeric array | [1,2,3] | Error — $convert failed for target date |
| mixed array | [1,null,"x",3] | Error — $convert failed for target date |
| nested array | [[1,2],[3]] | Error — $convert failed for target date |
| empty object | {} | Error — $convert failed for target date |
| object | {"x":1} | Error — $convert failed for target date |
| ISO date string | "2026-01-15T15:00:00Z" | {'$numberLong': '1768489200000'} (date) |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toDate.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **13 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / zero | {'$numberLong': '0'} (date) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Unsupported conversion from int to date in $convert with no  |
| input / negative | {'$numberLong': '-2'} (date) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Unsupported conversion from int to date in $convert with no  |

</details>

[Download full comparison evidence](../../downloads/operator-parity/toDate.json).

<!-- END MONGO PARITY -->

# $toLong

## Definition

Converts a value to long.

**Expression operator** · Types and conversion · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$toLong": <expression> }
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
| decimal | 2.5 | 2 (int64) |
| numeric string | "12" | 12 (int64) |
| text | "hello" | Error — $convert failed for target long |
| boolean | true | 1 (int64) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 1768489200000 (int64) |
| empty array | [] | Error — $convert failed for target long |
| numeric array | [1,2,3] | Error — $convert failed for target long |
| object | {"x":1} | Error — $convert failed for target long |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$toLong":[]} | Error — $convert failed for target long |
| {"$toLong":{"unexpected":1}} | Error — $convert failed for target long |

## Examples

Expression:
```json
{
  "$toLong": "12"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 12 (int64).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (int64) |
| negative | -2 | -2 (int64) |
| decimal | 2.5 | 2 (int64) |
| numeric string | "12" | 12 (int64) |
| text | "hello" | Error — $convert failed for target long |
| empty string | "" | Error — $convert failed for target long |
| boolean | true | 1 (int64) |
| false | false | 0 (int64) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 1768489200000 (int64) |
| decimal128 | {"$numberDecimal":"1.25"} | 1 (int64) |
| empty array | [] | Error — $convert failed for target long |
| numeric array | [1,2,3] | Error — $convert failed for target long |
| mixed array | [1,null,"x",3] | Error — $convert failed for target long |
| nested array | [[1,2],[3]] | Error — $convert failed for target long |
| empty object | {} | Error — $convert failed for target long |
| object | {"x":1} | Error — $convert failed for target long |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $convert failed for target long |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toLong.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **11 exact BSON matches**, **11 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/toLong.json).

<!-- END MONGO PARITY -->

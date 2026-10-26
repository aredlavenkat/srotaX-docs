# $strLenCP

## Definition

Counts Unicode code points in a string.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$strLenCP": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $strLenCP requires a string. |
| missing | Field absent | Error — $strLenCP requires a string. |
| decimal | 2.5 | Error — $strLenCP requires a string. |
| numeric string | "12" | 2 (int32) |
| text | "hello" | 5 (int32) |
| boolean | true | Error — $strLenCP requires a string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $strLenCP requires a string. |
| empty array | [] | Error — $strLenCP requires a string. |
| numeric array | [1,2,3] | Error — $strLenCP requires a string. |
| object | {"x":1} | Error — $strLenCP requires a string. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$strLenCP":[]} | Error — $strLenCP requires one argument |
| {"$strLenCP":{"unexpected":1}} | Error — $strLenCP requires a string. |

## Examples

Expression:
```json
{
  "$strLenCP": "abc"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $strLenCP requires a string. |
| missing | Field absent | Error — $strLenCP requires a string. |
| zero | 0 | Error — $strLenCP requires a string. |
| negative | -2 | Error — $strLenCP requires a string. |
| decimal | 2.5 | Error — $strLenCP requires a string. |
| numeric string | "12" | 2 (int32) |
| text | "hello" | 5 (int32) |
| empty string | "" | 0 (int32) |
| boolean | true | Error — $strLenCP requires a string. |
| false | false | Error — $strLenCP requires a string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $strLenCP requires a string. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $strLenCP requires a string. |
| empty array | [] | Error — $strLenCP requires a string. |
| numeric array | [1,2,3] | Error — $strLenCP requires a string. |
| mixed array | [1,null,"x",3] | Error — $strLenCP requires a string. |
| nested array | [[1,2],[3]] | Error — $strLenCP requires a string. |
| empty object | {} | Error — $strLenCP requires a string. |
| object | {"x":1} | Error — $strLenCP requires a string. |
| ISO date string | "2026-01-15T15:00:00Z" | 20 (int32) |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/strLenCP.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **17 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/strLenCP.json).

<!-- END MONGO PARITY -->

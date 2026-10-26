# $sqrt

## Definition

Computes the square root.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$sqrt": <expression> }
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
| decimal | 2.5 | 1.5811388300841898 (double) |
| numeric string | "12" | Error — $sqrt expects a numeric argument. |
| text | "hello" | Error — $sqrt expects a numeric argument. |
| boolean | true | Error — $sqrt expects a numeric argument. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $sqrt expects a numeric argument. |
| empty array | [] | Error — $sqrt expects a numeric argument. |
| numeric array | [1,2,3] | Error — $sqrt expects a numeric argument. |
| object | {"x":1} | Error — $sqrt expects a numeric argument. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$sqrt":[]} | Error — $sqrt expects a numeric argument. |
| {"$sqrt":{"unexpected":1}} | Error — $sqrt expects a numeric argument. |

## Examples

Expression:
```json
{
  "$sqrt": 4
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | Error — $sqrt does not support negative numbers. |
| decimal | 2.5 | 1.5811388300841898 (double) |
| numeric string | "12" | Error — $sqrt expects a numeric argument. |
| text | "hello" | Error — $sqrt expects a numeric argument. |
| empty string | "" | Error — $sqrt expects a numeric argument. |
| boolean | true | Error — $sqrt expects a numeric argument. |
| false | false | Error — $sqrt expects a numeric argument. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $sqrt expects a numeric argument. |
| decimal128 | {"$numberDecimal":"1.25"} | 1.118033988749895 (double) |
| empty array | [] | Error — $sqrt expects a numeric argument. |
| numeric array | [1,2,3] | Error — $sqrt expects a numeric argument. |
| mixed array | [1,null,"x",3] | Error — $sqrt expects a numeric argument. |
| nested array | [[1,2],[3]] | Error — $sqrt expects a numeric argument. |
| empty object | {} | Error — $sqrt expects a numeric argument. |
| object | {"x":1} | Error — $sqrt expects a numeric argument. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $sqrt expects a numeric argument. |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$sqrt": -1
}
```

Input:
```json
{}
```

**SrotaX:** Error — $sqrt does not support negative numbers..

</details>

## Verification

This page records **23 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/sqrt.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **17 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / decimal128 | 1.118033988749895 (double) | 1.118033988749894848204586834365638 (decimal128) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/sqrt.json).

<!-- END MONGO PARITY -->

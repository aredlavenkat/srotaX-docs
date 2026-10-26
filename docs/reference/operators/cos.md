# $cos

## Definition

Computes cosine.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$cos": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $cos expects a numeric argument. |
| missing | Field absent | Error — $cos expects a numeric argument. |
| decimal | 2.5 | -0.8011436155469337 (double) |
| numeric string | "12" | Error — $cos expects a numeric argument. |
| text | "hello" | Error — $cos expects a numeric argument. |
| boolean | true | Error — $cos expects a numeric argument. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $cos expects a numeric argument. |
| empty array | [] | Error — $cos expects a numeric argument. |
| numeric array | [1,2,3] | Error — $cos expects a numeric argument. |
| object | {"x":1} | Error — $cos expects a numeric argument. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$cos":[]} | Error — $cos expects a numeric argument. |
| {"$cos":{"unexpected":1}} | Error — $cos expects a numeric argument. |

## Examples

Expression:
```json
{
  "$cos": 0
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 1.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $cos expects a numeric argument. |
| missing | Field absent | Error — $cos expects a numeric argument. |
| zero | 0 | 1.0 (double) |
| negative | -2 | -0.4161468365471424 (double) |
| decimal | 2.5 | -0.8011436155469337 (double) |
| numeric string | "12" | Error — $cos expects a numeric argument. |
| text | "hello" | Error — $cos expects a numeric argument. |
| empty string | "" | Error — $cos expects a numeric argument. |
| boolean | true | Error — $cos expects a numeric argument. |
| false | false | Error — $cos expects a numeric argument. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $cos expects a numeric argument. |
| decimal128 | {"$numberDecimal":"1.25"} | 0.3153223623952687 (double) |
| empty array | [] | Error — $cos expects a numeric argument. |
| numeric array | [1,2,3] | Error — $cos expects a numeric argument. |
| mixed array | [1,null,"x",3] | Error — $cos expects a numeric argument. |
| nested array | [[1,2],[3]] | Error — $cos expects a numeric argument. |
| empty object | {} | Error — $cos expects a numeric argument. |
| object | {"x":1} | Error — $cos expects a numeric argument. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $cos expects a numeric argument. |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/cos.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **15 both rejected**, **3 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error — $cos expects a numeric argument. | null |
| input / missing | Error — $cos expects a numeric argument. | null |
| input / decimal128 | 0.3153223623952687 (double) | 0.3153223623952686654475385524380380 (decimal128) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/cos.json).

<!-- END MONGO PARITY -->

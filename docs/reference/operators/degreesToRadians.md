# $degreesToRadians

## Definition

Computes conversion from degrees to radians.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$degreesToRadians": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $degreesToRadians expects a numeric input. |
| missing | Field absent | Error — $degreesToRadians expects a numeric input. |
| decimal | 2.5 | 0.04363323129985824 (double) |
| numeric string | "12" | Error — $degreesToRadians expects a numeric input. |
| text | "hello" | Error — $degreesToRadians expects a numeric input. |
| boolean | true | Error — $degreesToRadians expects a numeric input. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $degreesToRadians expects a numeric input. |
| empty array | [] | Error — $degreesToRadians expects a numeric input. |
| numeric array | [1,2,3] | Error — $degreesToRadians expects a numeric input. |
| object | {"x":1} | Error — $degreesToRadians expects a numeric input. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$degreesToRadians":[]} | Error — $degreesToRadians expects a numeric input. |
| {"$degreesToRadians":{"unexpected":1}} | Error — $degreesToRadians expects a numeric input. |

## Examples

Expression:
```json
{
  "$degreesToRadians": 0
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
| null | null | Error — $degreesToRadians expects a numeric input. |
| missing | Field absent | Error — $degreesToRadians expects a numeric input. |
| zero | 0 | 0.0 (double) |
| negative | -2 | -0.03490658503988659 (double) |
| decimal | 2.5 | 0.04363323129985824 (double) |
| numeric string | "12" | Error — $degreesToRadians expects a numeric input. |
| text | "hello" | Error — $degreesToRadians expects a numeric input. |
| empty string | "" | Error — $degreesToRadians expects a numeric input. |
| boolean | true | Error — $degreesToRadians expects a numeric input. |
| false | false | Error — $degreesToRadians expects a numeric input. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $degreesToRadians expects a numeric input. |
| decimal128 | {"$numberDecimal":"1.25"} | 0.02181661564992912 (double) |
| empty array | [] | Error — $degreesToRadians expects a numeric input. |
| numeric array | [1,2,3] | Error — $degreesToRadians expects a numeric input. |
| mixed array | [1,null,"x",3] | Error — $degreesToRadians expects a numeric input. |
| nested array | [[1,2],[3]] | Error — $degreesToRadians expects a numeric input. |
| empty object | {} | Error — $degreesToRadians expects a numeric input. |
| object | {"x":1} | Error — $degreesToRadians expects a numeric input. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $degreesToRadians expects a numeric input. |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/degreesToRadians.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **15 both rejected**, **3 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error — $degreesToRadians expects a numeric input. | null |
| input / missing | Error — $degreesToRadians expects a numeric input. | null |
| input / decimal128 | 0.02181661564992912 (double) | 0.02181661564992911971154613460610766 (decimal128) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/degreesToRadians.json).

<!-- END MONGO PARITY -->

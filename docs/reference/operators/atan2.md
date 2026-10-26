# $atan2

## Definition

Computes two-argument inverse tangent.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$atan2": [ <left>, <right> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `left` | Yes | Y-coordinate expression. |
| `right` | Yes | X-coordinate expression. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `left` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $atan2 only supports numeric values. |
| missing | Field absent | Error — $atan2 only supports numeric values. |
| decimal | 2.5 | 1.1902899496825317 (double) |
| numeric string | "12" | Error — $atan2 only supports numeric values. |
| text | "hello" | Error — $atan2 only supports numeric values. |
| boolean | true | Error — $atan2 only supports numeric values. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $atan2 only supports numeric values. |
| empty array | [] | Error — $atan2 only supports numeric values. |
| numeric array | [1,2,3] | Error — $atan2 only supports numeric values. |
| object | {"x":1} | Error — $atan2 only supports numeric values. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$atan2":[]} | Error — $atan2 requires two numeric arguments. |
| {"$atan2":{"unexpected":1}} | Error — $atan2 requires two numeric arguments. |

## Examples

Expression:
```json
{
  "$atan2": [
    0,
    1
  ]
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

**Argument: `left[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $atan2 only supports numeric values. |
| missing | Field absent | Error — $atan2 only supports numeric values. |
| zero | 0 | 0.0 (double) |
| negative | -2 | -1.1071487177940904 (double) |
| decimal | 2.5 | 1.1902899496825317 (double) |
| numeric string | "12" | Error — $atan2 only supports numeric values. |
| text | "hello" | Error — $atan2 only supports numeric values. |
| empty string | "" | Error — $atan2 only supports numeric values. |
| boolean | true | Error — $atan2 only supports numeric values. |
| false | false | Error — $atan2 only supports numeric values. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $atan2 only supports numeric values. |
| decimal128 | {"$numberDecimal":"1.25"} | 0.8960553845713439 (double) |
| empty array | [] | Error — $atan2 only supports numeric values. |
| numeric array | [1,2,3] | Error — $atan2 only supports numeric values. |
| mixed array | [1,null,"x",3] | Error — $atan2 only supports numeric values. |
| nested array | [[1,2],[3]] | Error — $atan2 only supports numeric values. |
| empty object | {} | Error — $atan2 only supports numeric values. |
| object | {"x":1} | Error — $atan2 only supports numeric values. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $atan2 only supports numeric values. |

**Argument: `right[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $atan2 only supports numeric values. |
| missing | Field absent | Error — $atan2 only supports numeric values. |
| zero | 0 | 0.0 (double) |
| negative | -2 | 3.141592653589793 (double) |
| decimal | 2.5 | 0.0 (double) |
| numeric string | "12" | Error — $atan2 only supports numeric values. |
| text | "hello" | Error — $atan2 only supports numeric values. |
| empty string | "" | Error — $atan2 only supports numeric values. |
| boolean | true | Error — $atan2 only supports numeric values. |
| false | false | Error — $atan2 only supports numeric values. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $atan2 only supports numeric values. |
| decimal128 | {"$numberDecimal":"1.25"} | 0.0 (double) |
| empty array | [] | Error — $atan2 only supports numeric values. |
| numeric array | [1,2,3] | Error — $atan2 only supports numeric values. |
| mixed array | [1,null,"x",3] | Error — $atan2 only supports numeric values. |
| nested array | [[1,2],[3]] | Error — $atan2 only supports numeric values. |
| empty object | {} | Error — $atan2 only supports numeric values. |
| object | {"x":1} | Error — $atan2 only supports numeric values. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $atan2 only supports numeric values. |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/atan2.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **28 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| left[0] / null | Error — $atan2 only supports numeric values. | null |
| left[0] / missing | Error — $atan2 only supports numeric values. | null |
| left[0] / decimal128 | 0.8960553845713439 (double) | 0.8960553845713439561748007180299378 (decimal128) |
| right[1] / null | Error — $atan2 only supports numeric values. | null |
| right[1] / missing | Error — $atan2 only supports numeric values. | null |
| right[1] / decimal128 | 0.0 (double) | 0E-6176 (decimal128) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/atan2.json).

<!-- END MONGO PARITY -->

# $log

## Definition

Computes a logarithm using the supplied base.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$log": [ <left>, <right> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `left` | Yes | Number whose logarithm is calculated. |
| `right` | Yes | Logarithm base. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `left` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $log number must resolve to a numeric value |
| missing | Field absent | Error — $log number must resolve to a numeric value |
| decimal | 2.5 | 1.3219280948873624 (double) |
| numeric string | "12" | Error — $log number must resolve to a numeric value |
| text | "hello" | Error — $log number must resolve to a numeric value |
| boolean | true | Error — $log number must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $log number must resolve to a numeric value |
| empty array | [] | Error — $log number must resolve to a numeric value |
| numeric array | [1,2,3] | Error — $log number must resolve to a numeric value |
| object | {"x":1} | Error — $log number must resolve to a numeric value |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$log":[]} | Error — $log expects [number, base] |
| {"$log":{"unexpected":1}} | Error — $log expects [number, base] |

## Examples

Expression:
```json
{
  "$log": [
    8,
    2
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `left[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $log number must resolve to a numeric value |
| missing | Field absent | Error — $log number must resolve to a numeric value |
| zero | 0 | Error — $log requires positive number and base != 1 |
| negative | -2 | Error — $log requires positive number and base != 1 |
| decimal | 2.5 | 1.3219280948873624 (double) |
| numeric string | "12" | Error — $log number must resolve to a numeric value |
| text | "hello" | Error — $log number must resolve to a numeric value |
| empty string | "" | Error — $log number must resolve to a numeric value |
| boolean | true | Error — $log number must resolve to a numeric value |
| false | false | Error — $log number must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $log number must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | 0.32192809488736235 (double) |
| empty array | [] | Error — $log number must resolve to a numeric value |
| numeric array | [1,2,3] | Error — $log number must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error — $log number must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error — $log number must resolve to a numeric value |
| empty object | {} | Error — $log number must resolve to a numeric value |
| object | {"x":1} | Error — $log number must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $log number must resolve to a numeric value |

**Argument: `right[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $log base must resolve to a numeric value |
| missing | Field absent | Error — $log base must resolve to a numeric value |
| zero | 0 | Error — $log requires positive number and base != 1 |
| negative | -2 | Error — $log requires positive number and base != 1 |
| decimal | 2.5 | 2.26941239209809 (double) |
| numeric string | "12" | Error — $log base must resolve to a numeric value |
| text | "hello" | Error — $log base must resolve to a numeric value |
| empty string | "" | Error — $log base must resolve to a numeric value |
| boolean | true | Error — $log base must resolve to a numeric value |
| false | false | Error — $log base must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $log base must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | 9.318851158516168 (double) |
| empty array | [] | Error — $log base must resolve to a numeric value |
| numeric array | [1,2,3] | Error — $log base must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error — $log base must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error — $log base must resolve to a numeric value |
| empty object | {} | Error — $log base must resolve to a numeric value |
| object | {"x":1} | Error — $log base must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $log base must resolve to a numeric value |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/log.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **32 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| left[0] / null | Error — $log number must resolve to a numeric value | null |
| left[0] / missing | Error — $log number must resolve to a numeric value | null |
| left[0] / decimal128 | 0.32192809488736235 (double) | 0.3219280948873623478703194294893902 (decimal128) |
| right[1] / null | Error — $log base must resolve to a numeric value | null |
| right[1] / missing | Error — $log base must resolve to a numeric value | null |
| right[1] / decimal128 | 9.318851158516168 (double) | 9.318851158516169628007195475350726 (decimal128) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/log.json).

<!-- END MONGO PARITY -->

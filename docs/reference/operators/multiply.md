# $multiply

## Definition

Multiplies numeric operands.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$multiply": [ <number>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | See argument count below | Numeric expression. Repeat the argument when the syntax accepts multiple operands. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `number` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | 7.5 (double) |
| numeric string | "12" | Error — $multiply only supports numeric types. |
| text | "hello" | Error — $multiply only supports numeric types. |
| boolean | true | Error — $multiply only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $multiply only supports numeric types. |
| empty array | [] | Error — $multiply only supports numeric types. |
| numeric array | [1,2,3] | Error — $multiply only supports numeric types. |
| object | {"x":1} | Error — $multiply only supports numeric types. |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | 5.0 (double) |
| numeric string | "12" | Error — $multiply only supports numeric types. |
| text | "hello" | Error — $multiply only supports numeric types. |
| boolean | true | Error — $multiply only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $multiply only supports numeric types. |
| empty array | [] | Error — $multiply only supports numeric types. |
| numeric array | [1,2,3] | Error — $multiply only supports numeric types. |
| object | {"x":1} | Error — $multiply only supports numeric types. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$multiply":[]} | 1.0 (double) |
| {"$multiply":{"unexpected":1}} | Error — $multiply requires an array of values. |

## Examples

Expression:
```json
{
  "$multiply": [
    2,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 6.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `number[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | -6.0 (double) |
| decimal | 2.5 | 7.5 (double) |
| numeric string | "12" | Error — $multiply only supports numeric types. |
| text | "hello" | Error — $multiply only supports numeric types. |
| empty string | "" | Error — $multiply only supports numeric types. |
| boolean | true | Error — $multiply only supports numeric types. |
| false | false | Error — $multiply only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $multiply only supports numeric types. |
| decimal128 | {"$numberDecimal":"1.25"} | 3.75 (double) |
| empty array | [] | Error — $multiply only supports numeric types. |
| numeric array | [1,2,3] | Error — $multiply only supports numeric types. |
| mixed array | [1,null,"x",3] | Error — $multiply only supports numeric types. |
| nested array | [[1,2],[3]] | Error — $multiply only supports numeric types. |
| empty object | {} | Error — $multiply only supports numeric types. |
| object | {"x":1} | Error — $multiply only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $multiply only supports numeric types. |

**Argument: `number[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | -4.0 (double) |
| decimal | 2.5 | 5.0 (double) |
| numeric string | "12" | Error — $multiply only supports numeric types. |
| text | "hello" | Error — $multiply only supports numeric types. |
| empty string | "" | Error — $multiply only supports numeric types. |
| boolean | true | Error — $multiply only supports numeric types. |
| false | false | Error — $multiply only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $multiply only supports numeric types. |
| decimal128 | {"$numberDecimal":"1.25"} | 2.5 (double) |
| empty array | [] | Error — $multiply only supports numeric types. |
| numeric array | [1,2,3] | Error — $multiply only supports numeric types. |
| mixed array | [1,null,"x",3] | Error — $multiply only supports numeric types. |
| nested array | [[1,2],[3]] | Error — $multiply only supports numeric types. |
| empty object | {} | Error — $multiply only supports numeric types. |
| object | {"x":1} | Error — $multiply only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $multiply only supports numeric types. |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/multiply.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **6 exact BSON matches**, **27 both rejected**, **8 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 6.0 (double) | 6 (int32) |
| number[0] / zero | 0.0 (double) | 0 (int32) |
| number[0] / negative | -6.0 (double) | -6 (int32) |
| number[0] / decimal128 | 3.75 (double) | 3.75 (decimal128) |
| number[1] / zero | 0.0 (double) | 0 (int32) |
| number[1] / negative | -4.0 (double) | -4 (int32) |
| number[1] / decimal128 | 2.5 (double) | 2.50 (decimal128) |
| all / empty arguments | 1.0 (double) | 1 (int32) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/multiply.json).

<!-- END MONGO PARITY -->

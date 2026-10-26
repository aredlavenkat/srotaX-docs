# $bitOr

## Definition

Computes bitwise OR of integers.

**Expression operator** · Arithmetic · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$bitOr": [ <integer>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `integer` | See argument count below | Integer expression used in the bitwise operation. |

Arguments are positional: keep the order shown. Supply 2 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `integer` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $bitOr expects numeric operands |
| missing | Field absent | Error — $bitOr expects numeric operands |
| decimal | 2.5 | 7 (int64) |
| numeric string | "12" | Error — $bitOr expects numeric operands |
| text | "hello" | Error — $bitOr expects numeric operands |
| boolean | true | Error — $bitOr expects numeric operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $bitOr expects numeric operands |
| empty array | [] | Error — $bitOr expects numeric operands |
| numeric array | [1,2,3] | Error — $bitOr expects numeric operands |
| object | {"x":1} | Error — $bitOr expects numeric operands |
| null | null | Error — $bitOr expects numeric operands |
| missing | Field absent | Error — $bitOr expects numeric operands |
| decimal | 2.5 | 3 (int64) |
| numeric string | "12" | Error — $bitOr expects numeric operands |
| text | "hello" | Error — $bitOr expects numeric operands |
| boolean | true | Error — $bitOr expects numeric operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $bitOr expects numeric operands |
| empty array | [] | Error — $bitOr expects numeric operands |
| numeric array | [1,2,3] | Error — $bitOr expects numeric operands |
| object | {"x":1} | Error — $bitOr expects numeric operands |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$bitOr":[]} | Error — $bitOr expects an array of at least two numeric operands |
| {"$bitOr":{"unexpected":1}} | Error — $bitOr expects an array of at least two numeric operands |

## Examples

Expression:
```json
{
  "$bitOr": [
    3,
    5
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 7 (int64).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `integer[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $bitOr expects numeric operands |
| missing | Field absent | Error — $bitOr expects numeric operands |
| zero | 0 | 5 (int64) |
| negative | -2 | -1 (int64) |
| decimal | 2.5 | 7 (int64) |
| numeric string | "12" | Error — $bitOr expects numeric operands |
| text | "hello" | Error — $bitOr expects numeric operands |
| empty string | "" | Error — $bitOr expects numeric operands |
| boolean | true | Error — $bitOr expects numeric operands |
| false | false | Error — $bitOr expects numeric operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $bitOr expects numeric operands |
| decimal128 | {"$numberDecimal":"1.25"} | 5 (int64) |
| empty array | [] | Error — $bitOr expects numeric operands |
| numeric array | [1,2,3] | Error — $bitOr expects numeric operands |
| mixed array | [1,null,"x",3] | Error — $bitOr expects numeric operands |
| nested array | [[1,2],[3]] | Error — $bitOr expects numeric operands |
| empty object | {} | Error — $bitOr expects numeric operands |
| object | {"x":1} | Error — $bitOr expects numeric operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $bitOr expects numeric operands |

**Argument: `integer[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $bitOr expects numeric operands |
| missing | Field absent | Error — $bitOr expects numeric operands |
| zero | 0 | 3 (int64) |
| negative | -2 | -1 (int64) |
| decimal | 2.5 | 3 (int64) |
| numeric string | "12" | Error — $bitOr expects numeric operands |
| text | "hello" | Error — $bitOr expects numeric operands |
| empty string | "" | Error — $bitOr expects numeric operands |
| boolean | true | Error — $bitOr expects numeric operands |
| false | false | Error — $bitOr expects numeric operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $bitOr expects numeric operands |
| decimal128 | {"$numberDecimal":"1.25"} | 3 (int64) |
| empty array | [] | Error — $bitOr expects numeric operands |
| numeric array | [1,2,3] | Error — $bitOr expects numeric operands |
| mixed array | [1,null,"x",3] | Error — $bitOr expects numeric operands |
| nested array | [[1,2],[3]] | Error — $bitOr expects numeric operands |
| empty object | {} | Error — $bitOr expects numeric operands |
| object | {"x":1} | Error — $bitOr expects numeric operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $bitOr expects numeric operands |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/bitOr.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **0 exact BSON matches**, **27 both rejected**, **14 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 7 (int64) | 7 (int32) |
| integer[0] / null | Error — $bitOr expects numeric operands | null |
| integer[0] / missing | Error — $bitOr expects numeric operands | null |
| integer[0] / zero | 5 (int64) | 5 (int32) |
| integer[0] / negative | -1 (int64) | -1 (int32) |
| integer[0] / decimal | 7 (int64) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitOr only supports int and long operands. |
| integer[0] / decimal128 | 5 (int64) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitOr only supports int and long operands. |
| integer[1] / null | Error — $bitOr expects numeric operands | null |
| integer[1] / missing | Error — $bitOr expects numeric operands | null |
| integer[1] / zero | 3 (int64) | 3 (int32) |
| integer[1] / negative | -1 (int64) | -1 (int32) |
| integer[1] / decimal | 3 (int64) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitOr only supports int and long operands. |
| integer[1] / decimal128 | 3 (int64) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitOr only supports int and long operands. |
| all / empty arguments | Error — $bitOr expects an array of at least two numeric operands | 0 (int32) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/bitOr.json).

<!-- END MONGO PARITY -->

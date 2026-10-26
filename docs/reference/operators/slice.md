# $slice

## Definition

Extracts an array segment; negative indexes are not Mongo-compatible.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$slice": [ <array>, <positionOrCount>, <count> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | Expression supplying the source array. |
| `positionOrCount` | Yes | With two arguments, the number of elements to keep. With three arguments, the starting position. |
| `count` | No | Number of elements to keep in the three-argument form. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–3 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `array` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $slice expects first argument to be an array |
| missing | Field absent | Error — $slice expects first argument to be an array |
| decimal | 2.5 | Error — $slice expects first argument to be an array |
| numeric string | "12" | Error — $slice expects first argument to be an array |
| text | "hello" | Error — $slice expects first argument to be an array |
| boolean | true | Error — $slice expects first argument to be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $slice expects first argument to be an array |
| empty array | [] | Error — fromIndex(1) &gt; toIndex(0) |
| numeric array | [1,2,3] | [2] |
| object | {"x":1} | Error — $slice expects first argument to be an array |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$slice":[]} | Error — $slice expects [array, limit] or [array, skip, limit] |
| {"$slice":{"unexpected":1}} | Error — $slice expects [array, limit] or [array, skip, limit] |

## Examples

Expression:
```json
{
  "$slice": [
    [
      1,
      2,
      3
    ],
    1,
    1
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [2].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `array[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $slice expects first argument to be an array |
| missing | Field absent | Error — $slice expects first argument to be an array |
| zero | 0 | Error — $slice expects first argument to be an array |
| negative | -2 | Error — $slice expects first argument to be an array |
| decimal | 2.5 | Error — $slice expects first argument to be an array |
| numeric string | "12" | Error — $slice expects first argument to be an array |
| text | "hello" | Error — $slice expects first argument to be an array |
| empty string | "" | Error — $slice expects first argument to be an array |
| boolean | true | Error — $slice expects first argument to be an array |
| false | false | Error — $slice expects first argument to be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $slice expects first argument to be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $slice expects first argument to be an array |
| empty array | [] | Error — fromIndex(1) &gt; toIndex(0) |
| numeric array | [1,2,3] | [2] |
| mixed array | [1,null,"x",3] | [null] |
| nested array | [[1,2],[3]] | [[3]] |
| empty object | {} | Error — $slice expects first argument to be an array |
| object | {"x":1} | Error — $slice expects first argument to be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $slice expects first argument to be an array |

**Argument: `positionOrCount[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $slice requires numeric skip/limit values |
| missing | Field absent | Error — $slice requires numeric skip/limit values |
| zero | 0 | [1] |
| negative | -2 | [] |
| decimal | 2.5 | [3] |
| numeric string | "12" | Error — $slice requires numeric skip/limit values |
| text | "hello" | Error — $slice requires numeric skip/limit values |
| empty string | "" | Error — $slice requires numeric skip/limit values |
| boolean | true | Error — $slice requires numeric skip/limit values |
| false | false | Error — $slice requires numeric skip/limit values |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $slice requires numeric skip/limit values |
| decimal128 | {"$numberDecimal":"1.25"} | [2] |
| empty array | [] | Error — $slice requires numeric skip/limit values |
| numeric array | [1,2,3] | Error — $slice requires numeric skip/limit values |
| mixed array | [1,null,"x",3] | Error — $slice requires numeric skip/limit values |
| nested array | [[1,2],[3]] | Error — $slice requires numeric skip/limit values |
| empty object | {} | Error — $slice requires numeric skip/limit values |
| object | {"x":1} | Error — $slice requires numeric skip/limit values |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $slice requires numeric skip/limit values |

**Argument: `count[2]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $slice requires numeric skip/limit values |
| missing | Field absent | Error — $slice requires numeric skip/limit values |
| zero | 0 | [] |
| negative | -2 | [] |
| decimal | 2.5 | [2,3] |
| numeric string | "12" | Error — $slice requires numeric skip/limit values |
| text | "hello" | Error — $slice requires numeric skip/limit values |
| empty string | "" | Error — $slice requires numeric skip/limit values |
| boolean | true | Error — $slice requires numeric skip/limit values |
| false | false | Error — $slice requires numeric skip/limit values |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $slice requires numeric skip/limit values |
| decimal128 | {"$numberDecimal":"1.25"} | [2] |
| empty array | [] | Error — $slice requires numeric skip/limit values |
| numeric array | [1,2,3] | Error — $slice requires numeric skip/limit values |
| mixed array | [1,null,"x",3] | Error — $slice requires numeric skip/limit values |
| nested array | [[1,2],[3]] | Error — $slice requires numeric skip/limit values |
| empty object | {} | Error — $slice requires numeric skip/limit values |
| object | {"x":1} | Error — $slice requires numeric skip/limit values |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $slice requires numeric skip/limit values |


</details>

## Verification

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/slice.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **41 both rejected**, **14 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| array[0] / null | Error — $slice expects first argument to be an array | null |
| array[0] / missing | Error — $slice expects first argument to be an array | null |
| array[0] / empty array | Error — fromIndex(1) &gt; toIndex(0) | [] |
| positionOrCount[1] / null | Error — $slice requires numeric skip/limit values | null |
| positionOrCount[1] / missing | Error — $slice requires numeric skip/limit values | null |
| positionOrCount[1] / negative | [] | [2] |
| positionOrCount[1] / decimal | [3] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Second argument to $slice can't be represented as a 32-bit i |
| positionOrCount[1] / decimal128 | [2] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Second argument to $slice can't be represented as a 32-bit i |
| count[2] / null | Error — $slice requires numeric skip/limit values | null |
| count[2] / missing | Error — $slice requires numeric skip/limit values | null |
| count[2] / zero | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice must be positive: 0 |
| count[2] / negative | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice must be positive: -2 |
| count[2] / decimal | [2,3] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice can't be represented as a 32-bit in |
| count[2] / decimal128 | [2] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice can't be represented as a 32-bit in |

</details>

[Download full comparison evidence](../../downloads/operator-parity/slice.json).

<!-- END MONGO PARITY -->

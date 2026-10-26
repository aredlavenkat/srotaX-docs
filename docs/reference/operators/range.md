# $range

## Definition

Generates numbers from an inclusive start to an exclusive end.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$range": [ <start>, <end>, <step> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start` | Yes | Inclusive starting integer. |
| `end` | Yes | Exclusive ending integer. |
| `step` | No | Increment between generated values. Defaults to `1`; use a negative step for descending values. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–3 arguments.

**Resource limit:** very large ranges can exhaust engine memory. Bound range sizes before execution; an extreme-endpoint probe exhausted the test JVM and is excluded from the bounded tables below.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `start` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $range start argument must resolve to a numeric value |
| missing | Field absent | Error — $range start argument must resolve to a numeric value |
| decimal | 2.5 | [2.5] |
| numeric string | "12" | Error — $range start argument must resolve to a numeric value |
| text | "hello" | Error — $range start argument must resolve to a numeric value |
| boolean | true | Error — $range start argument must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $range start argument must resolve to a numeric value |
| empty array | [] | Error — $range start argument must resolve to a numeric value |
| numeric array | [1,2,3] | Error — $range start argument must resolve to a numeric value |
| object | {"x":1} | Error — $range start argument must resolve to a numeric value |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$range":[]} | Error — $range expects [start, end, step?] |
| {"$range":{"unexpected":1}} | Error — $range expects [start, end, step?] |

## Examples

Expression:
```json
{
  "$range": [
    0,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [0,1,2].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `start[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $range start argument must resolve to a numeric value |
| missing | Field absent | Error — $range start argument must resolve to a numeric value |
| zero | 0 | [0,1,2] |
| negative | -2 | [-2,-1,0,1,2] |
| decimal | 2.5 | [2.5] |
| numeric string | "12" | Error — $range start argument must resolve to a numeric value |
| text | "hello" | Error — $range start argument must resolve to a numeric value |
| empty string | "" | Error — $range start argument must resolve to a numeric value |
| boolean | true | Error — $range start argument must resolve to a numeric value |
| false | false | Error — $range start argument must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $range start argument must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | [1.25,2.25] |
| empty array | [] | Error — $range start argument must resolve to a numeric value |
| numeric array | [1,2,3] | Error — $range start argument must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error — $range start argument must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error — $range start argument must resolve to a numeric value |
| empty object | {} | Error — $range start argument must resolve to a numeric value |
| object | {"x":1} | Error — $range start argument must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $range start argument must resolve to a numeric value |

**Argument: `end[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $range end argument must resolve to a numeric value |
| missing | Field absent | Error — $range end argument must resolve to a numeric value |
| zero | 0 | [] |
| negative | -2 | [] |
| decimal | 2.5 | [0.0,1.0,2.0] |
| numeric string | "12" | Error — $range end argument must resolve to a numeric value |
| text | "hello" | Error — $range end argument must resolve to a numeric value |
| empty string | "" | Error — $range end argument must resolve to a numeric value |
| boolean | true | Error — $range end argument must resolve to a numeric value |
| false | false | Error — $range end argument must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $range end argument must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | [0.0,1.0] |
| empty array | [] | Error — $range end argument must resolve to a numeric value |
| numeric array | [1,2,3] | Error — $range end argument must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error — $range end argument must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error — $range end argument must resolve to a numeric value |
| empty object | {} | Error — $range end argument must resolve to a numeric value |
| object | {"x":1} | Error — $range end argument must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $range end argument must resolve to a numeric value |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/range.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **32 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | [0,1,2] | [0,1,2] |
| start[0] / zero | [0,1,2] | [0,1,2] |
| start[0] / negative | [-2,-1,0,1,2] | [-2,-1,0,1,2] |
| start[0] / decimal | [2.5] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires a starting value that can be represented as  |
| start[0] / decimal128 | [1.25,2.25] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires a starting value that can be represented as  |
| end[1] / decimal | [0.0,1.0,2.0] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires an ending value that can be represented as a |
| end[1] / decimal128 | [0.0,1.0] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires an ending value that can be represented as a |

</details>

[Download full comparison evidence](../../downloads/operator-parity/range.json).

<!-- END MONGO PARITY -->

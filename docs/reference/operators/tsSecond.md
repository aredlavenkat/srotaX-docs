# $tsSecond

## Definition

Reads seconds from a Fluxion timestamp map.

**Expression operator** · Dates · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$tsSecond": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $tsSecond expects a timestamp object |
| numeric string | "12" | Error — $tsSecond expects a timestamp object |
| text | "hello" | Error — $tsSecond expects a timestamp object |
| boolean | true | Error — $tsSecond expects a timestamp object |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $tsSecond expects a timestamp object |
| empty array | [] | Error — $tsSecond expects a timestamp object |
| numeric array | [1,2,3] | Error — $tsSecond expects a timestamp object |
| object | {"x":1} | null |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$tsSecond":[]} | Error — $tsSecond expects a timestamp object |
| {"$tsSecond":{"unexpected":1}} | null |

## Examples

Expression:
```json
{
  "$tsSecond": {
    "t": 10,
    "i": 2
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 10 (int64).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $tsSecond expects a timestamp object |
| negative | -2 | Error — $tsSecond expects a timestamp object |
| decimal | 2.5 | Error — $tsSecond expects a timestamp object |
| numeric string | "12" | Error — $tsSecond expects a timestamp object |
| text | "hello" | Error — $tsSecond expects a timestamp object |
| empty string | "" | Error — $tsSecond expects a timestamp object |
| boolean | true | Error — $tsSecond expects a timestamp object |
| false | false | Error — $tsSecond expects a timestamp object |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $tsSecond expects a timestamp object |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $tsSecond expects a timestamp object |
| empty array | [] | Error — $tsSecond expects a timestamp object |
| numeric array | [1,2,3] | Error — $tsSecond expects a timestamp object |
| mixed array | [1,null,"x",3] | Error — $tsSecond expects a timestamp object |
| nested array | [[1,2],[3]] | Error — $tsSecond expects a timestamp object |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $tsSecond expects a timestamp object |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/tsSecond.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **16 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 10 (int64) | Error — Failed to optimize pipeline :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |
| input / empty object | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |
| input / object | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |
| all / unknown option | null | Error — Failed to optimize pipeline :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |

</details>

[Download full comparison evidence](../../downloads/operator-parity/tsSecond.json).

<!-- END MONGO PARITY -->

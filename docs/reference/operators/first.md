# $first

## Definition

Reads the first array element.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$first": <expression> }
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
| decimal | 2.5 | null |
| numeric string | "12" | null |
| text | "hello" | null |
| boolean | true | null |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | null |
| empty array | [] | null |
| numeric array | [1,2,3] | 1 (int32) |
| object | {"x":1} | null |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$first":[]} | null |
| {"$first":{"unexpected":1}} | null |

## Examples

Expression:
```json
{
  "$first": {
    "$literal": [
      1,
      2
    ]
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 1 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | null |
| negative | -2 | null |
| decimal | 2.5 | null |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | null |
| boolean | true | null |
| false | false | null |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | null |
| decimal128 | {"$numberDecimal":"1.25"} | null |
| empty array | [] | null |
| numeric array | [1,2,3] | 1 (int32) |
| mixed array | [1,null,"x",3] | 1 (int32) |
| nested array | [[1,2],[3]] | [1,2] |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | null |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/first.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **6 exact BSON matches**, **0 both rejected**, **16 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / zero | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is int |
| input / negative | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is int |
| input / decimal | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is double |
| input / numeric string | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is string |
| input / text | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is string |
| input / empty string | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is string |
| input / boolean | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is bool |
| input / false | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is bool |
| input / typed date | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is date |
| input / decimal128 | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is decimal |
| input / empty array | null | Missing (field omitted) |
| input / empty object | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is object |
| input / object | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is object |
| input / ISO date string | null | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $first's argument must be an array, but is string |
| all / empty arguments | null | Error — Invalid $project :: caused by :: Expression $first takes exactly 1 arguments. 0 were passed in. |
| all / unknown option | null | Error — Failed to optimize pipeline :: caused by :: $first's argument must be an array, but is object |

</details>

[Download full comparison evidence](../../downloads/operator-parity/first.json).

<!-- END MONGO PARITY -->

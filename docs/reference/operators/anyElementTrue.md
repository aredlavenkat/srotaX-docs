# $anyElementTrue

Tests whether any array value is truthy under Fluxion coercion.

**Category:** Sets. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `array` | ARRAY | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **BOOLEAN**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$anyElementTrue": [
    [
      true,
      false
    ]
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** true.

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `array[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| zero | 0 | false |
| negative | -2 | true |
| decimal | 2.5 | true |
| numeric string | "12" | true |
| text | "hello" | true |
| empty string | "" | false |
| boolean | true | true |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | true |
| decimal128 | {"$numberDecimal":"1.25"} | true |
| empty array | [] | false |
| numeric array | [1,2,3] | true |
| mixed array | [1,null,"x",3] | true |
| nested array | [[1,2],[3]] | true |
| empty object | {} | true |
| object | {"x":1} | true |
| ISO date string | "2026-01-15T15:00:00Z" | true |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$anyElementTrue":[]} | false |
| {"$anyElementTrue":{"unexpected":1}} | Error: IllegalArgumentException — $anyElementTrue expects an array. |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/anyElementTrue.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **1 both rejected**, **16 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| array[0] / null | false | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is null |
| array[0] / missing | false | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is missing |
| array[0] / zero | false | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is int |
| array[0] / negative | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is int |
| array[0] / decimal | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is double |
| array[0] / numeric string | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is string |
| array[0] / text | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is string |
| array[0] / empty string | false | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is string |
| array[0] / boolean | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is bool |
| array[0] / false | false | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is bool |
| array[0] / typed date | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is date |
| array[0] / decimal128 | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is decimal |
| array[0] / empty object | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is object |
| array[0] / object | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is object |
| array[0] / ISO date string | true | Error: Location17041 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $anyElementTrue's argument must be an array, but is string |
| all / empty arguments | false | Error: Location16020 — Invalid $project :: caused by :: Expression $anyElementTrue takes exactly 1 arguments. 0 were passed in. |

[Download full comparison evidence](../../downloads/operator-parity/anyElementTrue.json).

<!-- END MONGO PARITY -->

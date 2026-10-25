# $bitXor

Computes bitwise exclusive OR of integers.

**Category:** Arithmetic. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `integer` | INT, LONG | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum variadic.

Declared result types: **LONG**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$bitXor": [
    3,
    5
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 6 (int64).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `integer[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $bitXor expects numeric operands |
| missing | Field absent | Error: IllegalArgumentException — $bitXor expects numeric operands |
| zero | 0 | 5 (int64) |
| negative | -2 | -5 (int64) |
| decimal | 2.5 | 7 (int64) |
| numeric string | "12" | Error: IllegalArgumentException — $bitXor expects numeric operands |
| text | "hello" | Error: IllegalArgumentException — $bitXor expects numeric operands |
| empty string | "" | Error: IllegalArgumentException — $bitXor expects numeric operands |
| boolean | true | Error: IllegalArgumentException — $bitXor expects numeric operands |
| false | false | Error: IllegalArgumentException — $bitXor expects numeric operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $bitXor expects numeric operands |
| decimal128 | {"$numberDecimal":"1.25"} | 4 (int64) |
| empty array | [] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| empty object | {} | Error: IllegalArgumentException — $bitXor expects numeric operands |
| object | {"x":1} | Error: IllegalArgumentException — $bitXor expects numeric operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $bitXor expects numeric operands |

### Argument: `integer[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $bitXor expects numeric operands |
| missing | Field absent | Error: IllegalArgumentException — $bitXor expects numeric operands |
| zero | 0 | 3 (int64) |
| negative | -2 | -3 (int64) |
| decimal | 2.5 | 1 (int64) |
| numeric string | "12" | Error: IllegalArgumentException — $bitXor expects numeric operands |
| text | "hello" | Error: IllegalArgumentException — $bitXor expects numeric operands |
| empty string | "" | Error: IllegalArgumentException — $bitXor expects numeric operands |
| boolean | true | Error: IllegalArgumentException — $bitXor expects numeric operands |
| false | false | Error: IllegalArgumentException — $bitXor expects numeric operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $bitXor expects numeric operands |
| decimal128 | {"$numberDecimal":"1.25"} | 2 (int64) |
| empty array | [] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $bitXor expects numeric operands |
| empty object | {} | Error: IllegalArgumentException — $bitXor expects numeric operands |
| object | {"x":1} | Error: IllegalArgumentException — $bitXor expects numeric operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $bitXor expects numeric operands |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$bitXor":[]} | Error: IllegalArgumentException — $bitXor expects an array of at least two numeric operands |
| {"$bitXor":{"unexpected":1}} | Error: IllegalArgumentException — $bitXor expects an array of at least two numeric operands |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/bitXor.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **0 exact BSON matches**, **27 both rejected**, **14 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 6 (int64) | 6 (int32) |
| integer[0] / null | Error: IllegalArgumentException — $bitXor expects numeric operands | null |
| integer[0] / missing | Error: IllegalArgumentException — $bitXor expects numeric operands | null |
| integer[0] / zero | 5 (int64) | 5 (int32) |
| integer[0] / negative | -5 (int64) | -5 (int32) |
| integer[0] / decimal | 7 (int64) | Error: TypeMismatch — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitXor only supports int and long operands. |
| integer[0] / decimal128 | 4 (int64) | Error: TypeMismatch — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitXor only supports int and long operands. |
| integer[1] / null | Error: IllegalArgumentException — $bitXor expects numeric operands | null |
| integer[1] / missing | Error: IllegalArgumentException — $bitXor expects numeric operands | null |
| integer[1] / zero | 3 (int64) | 3 (int32) |
| integer[1] / negative | -3 (int64) | -3 (int32) |
| integer[1] / decimal | 1 (int64) | Error: TypeMismatch — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitXor only supports int and long operands. |
| integer[1] / decimal128 | 2 (int64) | Error: TypeMismatch — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $bitXor only supports int and long operands. |
| all / empty arguments | Error: IllegalArgumentException — $bitXor expects an array of at least two numeric operands | 0 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/bitXor.json).

<!-- END MONGO PARITY -->

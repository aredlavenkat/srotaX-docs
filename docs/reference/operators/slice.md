# $slice

Extracts an array segment; negative indexes are not Mongo-compatible.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `array` | ARRAY | Yes | Expression evaluated against the input |
| `positionOrCount` | INT | Yes | Expression evaluated against the input |
| `count` | INT | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 3.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `array[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $slice expects first argument to be an array |
| missing | Field absent | Error: IllegalArgumentException — $slice expects first argument to be an array |
| zero | 0 | Error: IllegalArgumentException — $slice expects first argument to be an array |
| negative | -2 | Error: IllegalArgumentException — $slice expects first argument to be an array |
| decimal | 2.5 | Error: IllegalArgumentException — $slice expects first argument to be an array |
| numeric string | "12" | Error: IllegalArgumentException — $slice expects first argument to be an array |
| text | "hello" | Error: IllegalArgumentException — $slice expects first argument to be an array |
| empty string | "" | Error: IllegalArgumentException — $slice expects first argument to be an array |
| boolean | true | Error: IllegalArgumentException — $slice expects first argument to be an array |
| false | false | Error: IllegalArgumentException — $slice expects first argument to be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $slice expects first argument to be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $slice expects first argument to be an array |
| empty array | [] | Error: IllegalArgumentException — fromIndex(1) &gt; toIndex(0) |
| numeric array | [1,2,3] | [2] |
| mixed array | [1,null,"x",3] | [null] |
| nested array | [[1,2],[3]] | [[3]] |
| empty object | {} | Error: IllegalArgumentException — $slice expects first argument to be an array |
| object | {"x":1} | Error: IllegalArgumentException — $slice expects first argument to be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $slice expects first argument to be an array |

### Argument: `positionOrCount[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| missing | Field absent | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| zero | 0 | [1] |
| negative | -2 | [] |
| decimal | 2.5 | [3] |
| numeric string | "12" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| text | "hello" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| empty string | "" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| boolean | true | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| false | false | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| decimal128 | {"$numberDecimal":"1.25"} | [2] |
| empty array | [] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| empty object | {} | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| object | {"x":1} | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |

### Argument: `count[2]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| missing | Field absent | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| zero | 0 | [] |
| negative | -2 | [] |
| decimal | 2.5 | [2,3] |
| numeric string | "12" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| text | "hello" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| empty string | "" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| boolean | true | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| false | false | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| decimal128 | {"$numberDecimal":"1.25"} | [2] |
| empty array | [] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| empty object | {} | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| object | {"x":1} | Error: IllegalArgumentException — $slice requires numeric skip/limit values |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $slice requires numeric skip/limit values |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$slice":[]} | Error: IllegalArgumentException — $slice expects [array, limit] or [array, skip, limit] |
| {"$slice":{"unexpected":1}} | Error: IllegalArgumentException — $slice expects [array, limit] or [array, skip, limit] |

## Scope and reproducibility

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/slice.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **41 both rejected**, **14 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| array[0] / null | Error: IllegalArgumentException — $slice expects first argument to be an array | null |
| array[0] / missing | Error: IllegalArgumentException — $slice expects first argument to be an array | null |
| array[0] / empty array | Error: IllegalArgumentException — fromIndex(1) &gt; toIndex(0) | [] |
| positionOrCount[1] / null | Error: IllegalArgumentException — $slice requires numeric skip/limit values | null |
| positionOrCount[1] / missing | Error: IllegalArgumentException — $slice requires numeric skip/limit values | null |
| positionOrCount[1] / negative | [] | [2] |
| positionOrCount[1] / decimal | [3] | Error: Location28726 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Second argument to $slice can't be represented as a 32-bit i |
| positionOrCount[1] / decimal128 | [2] | Error: Location28726 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Second argument to $slice can't be represented as a 32-bit i |
| count[2] / null | Error: IllegalArgumentException — $slice requires numeric skip/limit values | null |
| count[2] / missing | Error: IllegalArgumentException — $slice requires numeric skip/limit values | null |
| count[2] / zero | [] | Error: Location28729 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice must be positive: 0 |
| count[2] / negative | [] | Error: Location28729 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice must be positive: -2 |
| count[2] / decimal | [2,3] | Error: Location28728 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice can't be represented as a 32-bit in |
| count[2] / decimal128 | [2] | Error: Location28728 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: Third argument to $slice can't be represented as a 32-bit in |

[Download full comparison evidence](../../downloads/operator-parity/slice.json).

<!-- END MONGO PARITY -->

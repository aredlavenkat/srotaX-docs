# $range

Generates numbers from an inclusive start to an exclusive end.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `start` | INT | Yes | Expression evaluated against the input |
| `end` | INT | Yes | Expression evaluated against the input |
| `step` | INT | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 3.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Resource limit:** very large ranges can exhaust engine memory. Bound range sizes before execution; an extreme-endpoint probe exhausted the test JVM and is excluded from the bounded tables below.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `start[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| missing | Field absent | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| zero | 0 | [0,1,2] |
| negative | -2 | [-2,-1,0,1,2] |
| decimal | 2.5 | [2.5] |
| numeric string | "12" | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| text | "hello" | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| empty string | "" | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| boolean | true | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| false | false | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | [1.25,2.25] |
| empty array | [] | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| empty object | {} | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| object | {"x":1} | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $range start argument must resolve to a numeric value |

### Argument: `end[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| missing | Field absent | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| zero | 0 | [] |
| negative | -2 | [] |
| decimal | 2.5 | [0.0,1.0,2.0] |
| numeric string | "12" | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| text | "hello" | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| empty string | "" | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| boolean | true | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| false | false | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | [0.0,1.0] |
| empty array | [] | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| empty object | {} | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| object | {"x":1} | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $range end argument must resolve to a numeric value |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$range":[]} | Error: IllegalArgumentException — $range expects [start, end, step?] |
| {"$range":{"unexpected":1}} | Error: IllegalArgumentException — $range expects [start, end, step?] |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/range.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **32 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | [0,1,2] | [0,1,2] |
| start[0] / zero | [0,1,2] | [0,1,2] |
| start[0] / negative | [-2,-1,0,1,2] | [-2,-1,0,1,2] |
| start[0] / decimal | [2.5] | Error: Location34444 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires a starting value that can be represented as  |
| start[0] / decimal128 | [1.25,2.25] | Error: Location34444 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires a starting value that can be represented as  |
| end[1] / decimal | [0.0,1.0,2.0] | Error: Location34446 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires an ending value that can be represented as a |
| end[1] / decimal128 | [0.0,1.0] | Error: Location34446 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $range requires an ending value that can be represented as a |

[Download full comparison evidence](../../downloads/operator-parity/range.json).

<!-- END MONGO PARITY -->

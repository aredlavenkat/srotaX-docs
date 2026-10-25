# $tsSecond

Reads seconds from a Fluxion timestamp map.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | OBJECT | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **LONG, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| negative | -2 | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| decimal | 2.5 | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| numeric string | "12" | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| text | "hello" | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| empty string | "" | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| boolean | true | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| false | false | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| empty array | [] | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $tsSecond expects a timestamp object |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$tsSecond":[]} | Error: IllegalArgumentException — $tsSecond expects a timestamp object |
| {"$tsSecond":{"unexpected":1}} | null |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/tsSecond.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **16 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 10 (int64) | Error: Location5687301 — Failed to optimize pipeline :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |
| input / empty object | null | Error: Location5687301 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |
| input / object | null | Error: Location5687301 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |
| all / unknown option | null | Error: Location5687301 — Failed to optimize pipeline :: caused by ::  Argument to $tsSecond must be a timestamp, but is object |

[Download full comparison evidence](../../downloads/operator-parity/tsSecond.json).

<!-- END MONGO PARITY -->

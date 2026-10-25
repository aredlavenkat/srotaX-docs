# $year

Extracts year using the host calendar.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | DATE | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **INT, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$year": {
    "$toDate": "2024-01-02T03:04:05.006Z"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2024 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| negative | -2 | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| decimal | 2.5 | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| numeric string | "12" | Error: IllegalArgumentException — Cannot convert value to date: 12 |
| text | "hello" | Error: IllegalArgumentException — Cannot convert value to date: hello |
| empty string | "" | Error: IllegalArgumentException — Cannot convert value to date:  |
| boolean | true | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| false | false | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 2026 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty array | [] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty object | {} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | 2026 (int32) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$year":[]} | Error: IllegalArgumentException — One date required |
| {"$year":{"unexpected":1}} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/year.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **17 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / ISO date string | 2026 (int32) | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type string to Date |

[Download full comparison evidence](../../downloads/operator-parity/year.json).

<!-- END MONGO PARITY -->

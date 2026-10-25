# $dateDiff

Counts elapsed whole units between dates.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `startDate` | DATE | Yes | Expression evaluated against the input |
| `endDate` | DATE | Yes | Expression evaluated against the input |
| `unit` | STRING | Yes | Expression evaluated against the input |
| `timezone` | STRING | No | Expression evaluated against the input |
| `startOfWeek` | STRING | No | Expression evaluated against the input |

Argument count: minimum 3; maximum 5.

Declared result types: **LONG, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$dateDiff": {
    "startDate": {
      "$toDate": "2024-01-01T00:00:00Z"
    },
    "endDate": {
      "$toDate": "2024-01-03T00:00:00Z"
    },
    "unit": "day"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2 (int64).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `startDate`

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | -743 (int64) |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty array | [] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty object | {} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | -743 (int64) |
| omitted named argument | Argument removed | null |

### Argument: `endDate`

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 745 (int64) |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty array | [] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty object | {} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | 745 (int64) |
| omitted named argument | Argument removed | null |

### Argument: `unit`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — unit must be a string |
| negative | -2 | Error: IllegalArgumentException — unit must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — unit must be a string |
| numeric string | "12" | Error: IllegalArgumentException — Invalid date unit: 12 |
| text | "hello" | Error: IllegalArgumentException — Invalid date unit: hello |
| empty string | "" | Error: IllegalArgumentException — Invalid date unit:  |
| boolean | true | Error: IllegalArgumentException — unit must be a string |
| false | false | Error: IllegalArgumentException — unit must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — unit must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — unit must be a string |
| empty array | [] | Error: IllegalArgumentException — unit must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — unit must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — unit must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — unit must be a string |
| empty object | {} | Error: IllegalArgumentException — unit must be a string |
| object | {"x":1} | Error: IllegalArgumentException — unit must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Invalid date unit: 2026-01-15T15:00:00Z |
| omitted named argument | Argument removed | null |

### Argument: `timezone`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — timezone must be a string |
| negative | -2 | Error: IllegalArgumentException — timezone must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — timezone must be a string |
| numeric string | "12" | Error: DateTimeException — Invalid ID for region-based ZoneId, invalid format: 12 |
| text | "hello" | Error: ZoneRulesException — Unknown time-zone ID: hello |
| empty string | "" | Error: DateTimeException — Invalid ID for ZoneOffset, invalid format:  |
| boolean | true | Error: IllegalArgumentException — timezone must be a string |
| false | false | Error: IllegalArgumentException — timezone must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — timezone must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — timezone must be a string |
| empty array | [] | Error: IllegalArgumentException — timezone must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — timezone must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — timezone must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — timezone must be a string |
| empty object | {} | Error: IllegalArgumentException — timezone must be a string |
| object | {"x":1} | Error: IllegalArgumentException — timezone must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error: DateTimeException — Invalid ID for region-based ZoneId, invalid format: 2026-01-15T15:00:00Z |
| omitted named argument | Argument removed | 2 (int64) |

### Argument: `startOfWeek`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 2 (int64) |
| missing | Field absent | 2 (int64) |
| zero | 0 | 2 (int64) |
| negative | -2 | 2 (int64) |
| decimal | 2.5 | 2 (int64) |
| numeric string | "12" | 2 (int64) |
| text | "hello" | 2 (int64) |
| empty string | "" | 2 (int64) |
| boolean | true | 2 (int64) |
| false | false | 2 (int64) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 2 (int64) |
| decimal128 | {"$numberDecimal":"1.25"} | 2 (int64) |
| empty array | [] | 2 (int64) |
| numeric array | [1,2,3] | 2 (int64) |
| mixed array | [1,null,"x",3] | 2 (int64) |
| nested array | [[1,2],[3]] | 2 (int64) |
| empty object | {} | 2 (int64) |
| object | {"x":1} | 2 (int64) |
| ISO date string | "2026-01-15T15:00:00Z" | 2 (int64) |
| omitted named argument | Argument removed | 2 (int64) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$dateDiff":[]} | Error: IllegalArgumentException — Date operator requires named arguments |
| {"$dateDiff":{"unexpected":1}} | null |

## Scope and reproducibility

This page records **103 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateDiff.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **32 exact BSON matches**, **65 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| startDate / ISO date string | -743 (int64) | Error: Location5166307 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $dateDiff requires 'startDate' to be a date, but got string |
| endDate / ISO date string | 745 (int64) | Error: Location5166307 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $dateDiff requires 'endDate' to be a date, but got string |
| startDate / omitted named argument | null | Error: Location5166303 — Invalid $project :: caused by :: Missing 'startDate' parameter to $dateDiff |
| endDate / omitted named argument | null | Error: Location5166304 — Invalid $project :: caused by :: Missing 'endDate' parameter to $dateDiff |
| unit / omitted named argument | null | Error: Location5166305 — Invalid $project :: caused by :: Missing 'unit' parameter to $dateDiff |
| all / unknown option | null | Error: Location5166302 — Invalid $project :: caused by :: Unrecognized argument to $dateDiff: unexpected |

[Download full comparison evidence](../../downloads/operator-parity/dateDiff.json).

<!-- END MONGO PARITY -->

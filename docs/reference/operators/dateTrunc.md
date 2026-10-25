# $dateTrunc

Truncates a date and returns a date value.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `date` | DATE | Yes | Expression evaluated against the input |
| `unit` | STRING | Yes | Expression evaluated against the input |
| `binSize` | INT | No | Expression evaluated against the input |
| `timezone` | STRING | No | Expression evaluated against the input |
| `startOfWeek` | STRING | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 5.

Declared result types: **DATE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$dateTrunc": {
    "date": {
      "$toDate": "2024-01-02T03:04:05.006Z"
    },
    "unit": "day",
    "timezone": "UTC"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {'$numberLong': '1704153600000'} (date).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `date`

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768435200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty array | [] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty object | {} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | {'$numberLong': '1768435200000'} (date) |
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

### Argument: `binSize`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — binSize must be positive |
| negative | -2 | Error: IllegalArgumentException — binSize must be positive |
| decimal | 2.5 | Error: IllegalArgumentException — binSize must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — binSize must be an integer |
| text | "hello" | Error: IllegalArgumentException — binSize must be an integer |
| empty string | "" | Error: IllegalArgumentException — binSize must be an integer |
| boolean | true | Error: IllegalArgumentException — binSize must be an integer |
| false | false | Error: IllegalArgumentException — binSize must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — binSize must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — binSize must be an int64 |
| empty array | [] | Error: IllegalArgumentException — binSize must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — binSize must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — binSize must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — binSize must be an integer |
| empty object | {} | Error: IllegalArgumentException — binSize must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — binSize must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — binSize must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

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
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `startOfWeek`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704153600000'} (date) |
| decimal | 2.5 | {'$numberLong': '1704153600000'} (date) |
| numeric string | "12" | {'$numberLong': '1704153600000'} (date) |
| text | "hello" | {'$numberLong': '1704153600000'} (date) |
| empty string | "" | {'$numberLong': '1704153600000'} (date) |
| boolean | true | {'$numberLong': '1704153600000'} (date) |
| false | false | {'$numberLong': '1704153600000'} (date) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1704153600000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | {'$numberLong': '1704153600000'} (date) |
| empty array | [] | {'$numberLong': '1704153600000'} (date) |
| numeric array | [1,2,3] | {'$numberLong': '1704153600000'} (date) |
| mixed array | [1,null,"x",3] | {'$numberLong': '1704153600000'} (date) |
| nested array | [[1,2],[3]] | {'$numberLong': '1704153600000'} (date) |
| empty object | {} | {'$numberLong': '1704153600000'} (date) |
| object | {"x":1} | {'$numberLong': '1704153600000'} (date) |
| ISO date string | "2026-01-15T15:00:00Z" | {'$numberLong': '1704153600000'} (date) |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$dateTrunc":[]} | Error: IllegalArgumentException — Date operator requires named arguments |
| {"$dateTrunc":{"unexpected":1}} | null |

## Scope and reproducibility

This page records **103 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateTrunc.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **30 exact BSON matches**, **67 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| date / ISO date string | {'$numberLong': '1768435200000'} (date) | Error: Location5166307 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $dateTrunc requires 'date' to be a date, but got string |
| startOfWeek / null | null | {'$numberLong': '1704153600000'} (date) |
| startOfWeek / missing | null | {'$numberLong': '1704153600000'} (date) |
| date / omitted named argument | null | Error: Location5439009 — Invalid $project :: caused by :: Missing 'date' parameter to $dateTrunc |
| unit / omitted named argument | null | Error: Location5439010 — Invalid $project :: caused by :: Missing 'unit' parameter to $dateTrunc |
| all / unknown option | null | Error: Location5439008 — Invalid $project :: caused by :: Unrecognized argument to $dateTrunc: unexpected. Expected arguments are date, unit, and optionally, binSize, timezone, startOfWeek |

[Download full comparison evidence](../../downloads/operator-parity/dateTrunc.json).

<!-- END MONGO PARITY -->

# $dateSubtract

Subtracts a calendar amount and returns a date value.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `startDate` | DATE | Yes | Expression evaluated against the input |
| `unit` | STRING | Yes | Expression evaluated against the input |
| `amount` | LONG | Yes | Expression evaluated against the input |
| `timezone` | STRING | No | Expression evaluated against the input |

Argument count: minimum 3; maximum 4.

Declared result types: **DATE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$dateSubtract": {
    "startDate": {
      "$toDate": "2024-01-02T03:04:05.006Z"
    },
    "unit": "day",
    "amount": 1
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {'$numberLong': '1704078245006'} (date).

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768402800000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty array | [] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty object | {} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | {'$numberLong': '1768402800000'} (date) |
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

### Argument: `amount`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704164645006'} (date) |
| negative | -2 | {'$numberLong': '1704337445006'} (date) |
| decimal | 2.5 | Error: IllegalArgumentException — amount must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — amount must be an integer |
| text | "hello" | Error: IllegalArgumentException — amount must be an integer |
| empty string | "" | Error: IllegalArgumentException — amount must be an integer |
| boolean | true | Error: IllegalArgumentException — amount must be an integer |
| false | false | Error: IllegalArgumentException — amount must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — amount must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — amount must be an int64 |
| empty array | [] | Error: IllegalArgumentException — amount must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — amount must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — amount must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — amount must be an integer |
| empty object | {} | Error: IllegalArgumentException — amount must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — amount must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — amount must be an integer |
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
| omitted named argument | Argument removed | {'$numberLong': '1704078245006'} (date) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$dateSubtract":[]} | Error: IllegalArgumentException — Date operator requires named arguments |
| {"$dateSubtract":{"unexpected":1}} | null |

## Scope and reproducibility

This page records **83 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateSubtract.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **13 exact BSON matches**, **65 both rejected**, **5 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| startDate / ISO date string | {'$numberLong': '1768402800000'} (date) | Error: Location5166403 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $dateSubtract requires startDate to be convertible to a date |
| startDate / omitted named argument | null | Error: Location5166402 — Invalid $project :: caused by :: $dateSubtract requires startDate, unit, and amount to be present |
| unit / omitted named argument | null | Error: Location5166402 — Invalid $project :: caused by :: $dateSubtract requires startDate, unit, and amount to be present |
| amount / omitted named argument | null | Error: Location5166402 — Invalid $project :: caused by :: $dateSubtract requires startDate, unit, and amount to be present |
| all / unknown option | null | Error: Location5166401 — Invalid $project :: caused by :: Unrecognized argument to $dateSubtract: unexpected. Expected arguments are startDate, unit, amount, and optionally timezone. |

[Download full comparison evidence](../../downloads/operator-parity/dateSubtract.json).

<!-- END MONGO PARITY -->

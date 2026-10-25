# $dateToParts

Extracts calendar fields into an object.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `date` | DATE | Yes | Expression evaluated against the input |
| `timezone` | STRING | No | Expression evaluated against the input |
| `iso8601` | BOOLEAN | No | Expression evaluated against the input |

Argument count: minimum 1; maximum 3.

Declared result types: **NULL, OBJECT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$dateToParts": {
    "date": {
      "$toDate": "2024-01-02T03:04:05.006Z"
    },
    "timezone": "UTC"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {"year":2024,"month":1,"day":2,"hour":3,"minute":4,"second":5,"millisecond":6}.

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {"year":2026,"month":1,"day":15,"hour":15,"minute":0,"second":0,"millisecond":0} |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty array | [] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| empty object | {} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error: IllegalArgumentException — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | {"year":2026,"month":1,"day":15,"hour":15,"minute":0,"second":0,"millisecond":0} |
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
| omitted named argument | Argument removed | {"year":2024,"month":1,"day":2,"hour":3,"minute":4,"second":5,"millisecond":6} |

### Argument: `iso8601`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — iso8601 must be boolean |
| missing | Field absent | Error: IllegalArgumentException — iso8601 must be boolean |
| zero | 0 | Error: IllegalArgumentException — iso8601 must be boolean |
| negative | -2 | Error: IllegalArgumentException — iso8601 must be boolean |
| decimal | 2.5 | Error: IllegalArgumentException — iso8601 must be boolean |
| numeric string | "12" | Error: IllegalArgumentException — iso8601 must be boolean |
| text | "hello" | Error: IllegalArgumentException — iso8601 must be boolean |
| empty string | "" | Error: IllegalArgumentException — iso8601 must be boolean |
| boolean | true | {"isoWeekYear":2024,"isoWeek":1,"isoDayOfWeek":2,"hour":3,"minute":4,"second":5,"millisecond":6} |
| false | false | {"year":2024,"month":1,"day":2,"hour":3,"minute":4,"second":5,"millisecond":6} |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — iso8601 must be boolean |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — iso8601 must be boolean |
| empty array | [] | Error: IllegalArgumentException — iso8601 must be boolean |
| numeric array | [1,2,3] | Error: IllegalArgumentException — iso8601 must be boolean |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — iso8601 must be boolean |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — iso8601 must be boolean |
| empty object | {} | Error: IllegalArgumentException — iso8601 must be boolean |
| object | {"x":1} | Error: IllegalArgumentException — iso8601 must be boolean |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — iso8601 must be boolean |
| omitted named argument | Argument removed | {"year":2024,"month":1,"day":2,"hour":3,"minute":4,"second":5,"millisecond":6} |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$dateToParts":[]} | Error: IllegalArgumentException — Date operator requires named arguments |
| {"$dateToParts":{"unexpected":1}} | null |

## Scope and reproducibility

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateToParts.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **10 exact BSON matches**, **48 both rejected**, **5 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| date / ISO date string | {"year":2026,"month":1,"day":15,"hour":15,"minute":0,"second":0,"millisecond":0} | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type string to Date |
| iso8601 / null | Error: IllegalArgumentException — iso8601 must be boolean | null |
| iso8601 / missing | Error: IllegalArgumentException — iso8601 must be boolean | null |
| date / omitted named argument | null | Error: Location40522 — Invalid $project :: caused by :: Missing 'date' parameter to $dateToParts |
| all / unknown option | null | Error: Location40520 — Invalid $project :: caused by :: Unrecognized argument to $dateToParts: unexpected |

[Download full comparison evidence](../../downloads/operator-parity/dateToParts.json).

<!-- END MONGO PARITY -->

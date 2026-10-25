# $dateToString

Formats a typed date using supported numeric format tokens.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `date` | DATE, OBJECT_ID, TIMESTAMP | Yes | Expression evaluated against the input |
| `format` | STRING | No | Expression evaluated against the input |
| `timezone` | STRING | No | Expression evaluated against the input |
| `onNull` | ANY | No | Expression evaluated against the input |

Argument count: minimum 1; maximum 4.

Declared result types: **ANY, NULL, STRING**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$dateToString": {
    "date": {
      "$toDate": "2024-01-02T03:04:05.006Z"
    },
    "format": "%Y-%m-%d",
    "timezone": "UTC"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "2024-01-02".

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `date`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| negative | -2 | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| decimal | 2.5 | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| numeric string | "12" | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| text | "hello" | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| empty string | "" | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| boolean | true | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| false | false | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "2026-01-15" |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| empty array | [] | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| empty object | {} | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| object | {"x":1} | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $dateToString requires date |

### Argument: `format`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $dateToString format must be a string |
| negative | -2 | Error: IllegalArgumentException — $dateToString format must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — $dateToString format must be a string |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | Error: IllegalArgumentException — $dateToString format must be a string |
| false | false | Error: IllegalArgumentException — $dateToString format must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $dateToString format must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $dateToString format must be a string |
| empty array | [] | Error: IllegalArgumentException — $dateToString format must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $dateToString format must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $dateToString format must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $dateToString format must be a string |
| empty object | {} | Error: IllegalArgumentException — $dateToString format must be a string |
| object | {"x":1} | Error: IllegalArgumentException — $dateToString format must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | "2024-01-02T03:04:05.006Z" |

### Argument: `timezone`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $dateToString timezone must be a string |
| negative | -2 | Error: IllegalArgumentException — $dateToString timezone must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — $dateToString timezone must be a string |
| numeric string | "12" | Error: DateTimeException — Invalid ID for region-based ZoneId, invalid format: 12 |
| text | "hello" | Error: ZoneRulesException — Unknown time-zone ID: hello |
| empty string | "" | Error: DateTimeException — Invalid ID for ZoneOffset, invalid format:  |
| boolean | true | Error: IllegalArgumentException — $dateToString timezone must be a string |
| false | false | Error: IllegalArgumentException — $dateToString timezone must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $dateToString timezone must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $dateToString timezone must be a string |
| empty array | [] | Error: IllegalArgumentException — $dateToString timezone must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $dateToString timezone must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $dateToString timezone must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $dateToString timezone must be a string |
| empty object | {} | Error: IllegalArgumentException — $dateToString timezone must be a string |
| object | {"x":1} | Error: IllegalArgumentException — $dateToString timezone must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error: DateTimeException — Invalid ID for region-based ZoneId, invalid format: 2026-01-15T15:00:00Z |
| omitted named argument | Argument removed | "2024-01-02" |

### Argument: `onNull`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | "2024-01-02" |
| missing | Field absent | "2024-01-02" |
| zero | 0 | "2024-01-02" |
| negative | -2 | "2024-01-02" |
| decimal | 2.5 | "2024-01-02" |
| numeric string | "12" | "2024-01-02" |
| text | "hello" | "2024-01-02" |
| empty string | "" | "2024-01-02" |
| boolean | true | "2024-01-02" |
| false | false | "2024-01-02" |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "2024-01-02" |
| decimal128 | {"$numberDecimal":"1.25"} | "2024-01-02" |
| empty array | [] | "2024-01-02" |
| numeric array | [1,2,3] | "2024-01-02" |
| mixed array | [1,null,"x",3] | "2024-01-02" |
| nested array | [[1,2],[3]] | "2024-01-02" |
| empty object | {} | "2024-01-02" |
| object | {"x":1} | "2024-01-02" |
| ISO date string | "2026-01-15T15:00:00Z" | "2024-01-02" |
| omitted named argument | Argument removed | "2024-01-02" |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$dateToString":[]} | Error: IllegalArgumentException — $dateToString requires date |
| {"$dateToString":{"unexpected":1}} | Error: IllegalArgumentException — $dateToString requires date |

## Scope and reproducibility

This page records **83 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateToString.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **34 exact BSON matches**, **49 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/dateToString.json).

<!-- END MONGO PARITY -->

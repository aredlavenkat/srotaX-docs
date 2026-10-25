# $dateFromParts

Builds a date value from calendar parts.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `year` | INT | No | Expression evaluated against the input |
| `month` | INT | No | Expression evaluated against the input |
| `day` | INT | No | Expression evaluated against the input |
| `hour` | INT | No | Expression evaluated against the input |
| `minute` | INT | No | Expression evaluated against the input |
| `second` | INT | No | Expression evaluated against the input |
| `millisecond` | INT | No | Expression evaluated against the input |
| `isoWeekYear` | INT | No | Expression evaluated against the input |
| `isoWeek` | INT | No | Expression evaluated against the input |
| `isoDayOfWeek` | INT | No | Expression evaluated against the input |
| `timezone` | STRING | No | Expression evaluated against the input |

Argument count: minimum 1; maximum 11.

Declared result types: **DATE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$dateFromParts": {
    "year": 2024,
    "month": 1,
    "day": 2
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

### Argument: `year`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — Year must be 1..9999 |
| negative | -2 | Error: IllegalArgumentException — Year must be 1..9999 |
| decimal | 2.5 | Error: IllegalArgumentException — year must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — year must be an integer |
| text | "hello" | Error: IllegalArgumentException — year must be an integer |
| empty string | "" | Error: IllegalArgumentException — year must be an integer |
| boolean | true | Error: IllegalArgumentException — year must be an integer |
| false | false | Error: IllegalArgumentException — year must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — year must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — year must be an int64 |
| empty array | [] | Error: IllegalArgumentException — year must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — year must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — year must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — year must be an integer |
| empty object | {} | Error: IllegalArgumentException — year must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — year must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — year must be an integer |
| omitted named argument | Argument removed | Error: IllegalArgumentException — year or isoWeekYear is required |

### Argument: `month`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1701475200000'} (date) |
| negative | -2 | {'$numberLong': '1696204800000'} (date) |
| decimal | 2.5 | Error: IllegalArgumentException — month must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — month must be an integer |
| text | "hello" | Error: IllegalArgumentException — month must be an integer |
| empty string | "" | Error: IllegalArgumentException — month must be an integer |
| boolean | true | Error: IllegalArgumentException — month must be an integer |
| false | false | Error: IllegalArgumentException — month must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — month must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — month must be an int64 |
| empty array | [] | Error: IllegalArgumentException — month must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — month must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — month must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — month must be an integer |
| empty object | {} | Error: IllegalArgumentException — month must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — month must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — month must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `day`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1703980800000'} (date) |
| negative | -2 | {'$numberLong': '1703808000000'} (date) |
| decimal | 2.5 | Error: IllegalArgumentException — day must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — day must be an integer |
| text | "hello" | Error: IllegalArgumentException — day must be an integer |
| empty string | "" | Error: IllegalArgumentException — day must be an integer |
| boolean | true | Error: IllegalArgumentException — day must be an integer |
| false | false | Error: IllegalArgumentException — day must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — day must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — day must be an int64 |
| empty array | [] | Error: IllegalArgumentException — day must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — day must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — day must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — day must be an integer |
| empty object | {} | Error: IllegalArgumentException — day must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — day must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — day must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704067200000'} (date) |

### Argument: `hour`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704146400000'} (date) |
| decimal | 2.5 | Error: IllegalArgumentException — hour must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — hour must be an integer |
| text | "hello" | Error: IllegalArgumentException — hour must be an integer |
| empty string | "" | Error: IllegalArgumentException — hour must be an integer |
| boolean | true | Error: IllegalArgumentException — hour must be an integer |
| false | false | Error: IllegalArgumentException — hour must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — hour must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — hour must be an int64 |
| empty array | [] | Error: IllegalArgumentException — hour must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — hour must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — hour must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — hour must be an integer |
| empty object | {} | Error: IllegalArgumentException — hour must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — hour must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — hour must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `minute`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704153480000'} (date) |
| decimal | 2.5 | Error: IllegalArgumentException — minute must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — minute must be an integer |
| text | "hello" | Error: IllegalArgumentException — minute must be an integer |
| empty string | "" | Error: IllegalArgumentException — minute must be an integer |
| boolean | true | Error: IllegalArgumentException — minute must be an integer |
| false | false | Error: IllegalArgumentException — minute must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — minute must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — minute must be an int64 |
| empty array | [] | Error: IllegalArgumentException — minute must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — minute must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — minute must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — minute must be an integer |
| empty object | {} | Error: IllegalArgumentException — minute must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — minute must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — minute must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `second`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704153598000'} (date) |
| decimal | 2.5 | Error: IllegalArgumentException — second must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — second must be an integer |
| text | "hello" | Error: IllegalArgumentException — second must be an integer |
| empty string | "" | Error: IllegalArgumentException — second must be an integer |
| boolean | true | Error: IllegalArgumentException — second must be an integer |
| false | false | Error: IllegalArgumentException — second must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — second must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — second must be an int64 |
| empty array | [] | Error: IllegalArgumentException — second must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — second must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — second must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — second must be an integer |
| empty object | {} | Error: IllegalArgumentException — second must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — second must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — second must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `millisecond`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704153599998'} (date) |
| decimal | 2.5 | Error: IllegalArgumentException — millisecond must be an int64 |
| numeric string | "12" | Error: IllegalArgumentException — millisecond must be an integer |
| text | "hello" | Error: IllegalArgumentException — millisecond must be an integer |
| empty string | "" | Error: IllegalArgumentException — millisecond must be an integer |
| boolean | true | Error: IllegalArgumentException — millisecond must be an integer |
| false | false | Error: IllegalArgumentException — millisecond must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — millisecond must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — millisecond must be an int64 |
| empty array | [] | Error: IllegalArgumentException — millisecond must be an integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — millisecond must be an integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — millisecond must be an integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — millisecond must be an integer |
| empty object | {} | Error: IllegalArgumentException — millisecond must be an integer |
| object | {"x":1} | Error: IllegalArgumentException — millisecond must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — millisecond must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `isoWeekYear`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| negative | -2 | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| decimal | 2.5 | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| numeric string | "12" | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| text | "hello" | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| empty string | "" | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| boolean | true | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| false | false | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| empty array | [] | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| empty object | {} | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| object | {"x":1} | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Cannot mix ISO week and calendar fields |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `isoWeek`

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

### Argument: `isoDayOfWeek`

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

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$dateFromParts":[]} | Error: IllegalArgumentException — Date operator requires named arguments |
| {"$dateFromParts":{"unexpected":1}} | Error: IllegalArgumentException — year or isoWeekYear is required |

## Scope and reproducibility

This page records **223 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateFromParts.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **39 exact BSON matches**, **144 both rejected**, **40 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| isoWeekYear / null | null | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeekYear / missing | null | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / null | null | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / missing | null | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / zero | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / negative | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / decimal | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / numeric string | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / text | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / empty string | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / boolean | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / false | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / typed date | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / decimal128 | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / empty array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / numeric array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / mixed array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / nested array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / empty object | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / object | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / ISO date string | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / null | null | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / missing | null | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / zero | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / negative | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / decimal | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / numeric string | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / text | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / empty string | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / boolean | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / false | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / typed date | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / decimal128 | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / empty array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / numeric array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / mixed array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / nested array | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / empty object | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / object | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / ISO date string | {'$numberLong': '1704153600000'} (date) | Error: Location40489 — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |

[Download full comparison evidence](../../downloads/operator-parity/dateFromParts.json).

<!-- END MONGO PARITY -->

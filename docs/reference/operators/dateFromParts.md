# $dateFromParts

## Definition

Builds a date value from calendar parts.

**Expression operator** · Dates · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$dateFromParts": {
    "year": <year>,
    "month": <month>,
    "day": <day>,
    "hour": <hour>,
    "minute": <minute>,
    "second": <second>,
    "millisecond": <millisecond>,
    "isoWeekYear": <isoWeekYear>,
    "isoWeek": <isoWeek>,
    "isoDayOfWeek": <isoDayOfWeek>,
    "timezone": <timezone>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `year` | One year form | Calendar year expression. Valid years are 1 through 9999. |
| `month` | No | Calendar month expression. Defaults to 1. |
| `day` | No | Day-of-month expression. Defaults to 1. |
| `hour` | No | Hour expression. Defaults to 0. |
| `minute` | No | Minute expression. Defaults to 0. |
| `second` | No | Second expression. Defaults to 0. |
| `millisecond` | No | Millisecond expression. Defaults to 0. |
| `isoWeekYear` | One year form | ISO week-numbering year. Use the ISO fields instead of the calendar year/month/day fields. Valid years are 1 through 9999. |
| `isoWeek` | No | ISO week number. Defaults to 1. |
| `isoDayOfWeek` | No | ISO weekday number. Defaults to 1. |
| `timezone` | No | Timezone name or offset used for the calendar operation, for example `"America/Toronto"` or `"+05:30"`. Defaults to UTC when omitted. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `year` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — year must be an int64 |
| numeric string | "12" | Error — year must be an integer |
| text | "hello" | Error — year must be an integer |
| boolean | true | Error — year must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — year must be an integer |
| empty array | [] | Error — year must be an integer |
| numeric array | [1,2,3] | Error — year must be an integer |
| object | {"x":1} | Error — year must be an integer |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$dateFromParts":[]} | Error — Date operator requires named arguments |
| {"$dateFromParts":{"unexpected":1}} | Error — year or isoWeekYear is required |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `year`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — Year must be 1..9999 |
| negative | -2 | Error — Year must be 1..9999 |
| decimal | 2.5 | Error — year must be an int64 |
| numeric string | "12" | Error — year must be an integer |
| text | "hello" | Error — year must be an integer |
| empty string | "" | Error — year must be an integer |
| boolean | true | Error — year must be an integer |
| false | false | Error — year must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — year must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — year must be an int64 |
| empty array | [] | Error — year must be an integer |
| numeric array | [1,2,3] | Error — year must be an integer |
| mixed array | [1,null,"x",3] | Error — year must be an integer |
| nested array | [[1,2],[3]] | Error — year must be an integer |
| empty object | {} | Error — year must be an integer |
| object | {"x":1} | Error — year must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — year must be an integer |
| omitted named argument | Argument removed | Error — year or isoWeekYear is required |

**Argument: `month`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1701475200000'} (date) |
| negative | -2 | {'$numberLong': '1696204800000'} (date) |
| decimal | 2.5 | Error — month must be an int64 |
| numeric string | "12" | Error — month must be an integer |
| text | "hello" | Error — month must be an integer |
| empty string | "" | Error — month must be an integer |
| boolean | true | Error — month must be an integer |
| false | false | Error — month must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — month must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — month must be an int64 |
| empty array | [] | Error — month must be an integer |
| numeric array | [1,2,3] | Error — month must be an integer |
| mixed array | [1,null,"x",3] | Error — month must be an integer |
| nested array | [[1,2],[3]] | Error — month must be an integer |
| empty object | {} | Error — month must be an integer |
| object | {"x":1} | Error — month must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — month must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `day`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1703980800000'} (date) |
| negative | -2 | {'$numberLong': '1703808000000'} (date) |
| decimal | 2.5 | Error — day must be an int64 |
| numeric string | "12" | Error — day must be an integer |
| text | "hello" | Error — day must be an integer |
| empty string | "" | Error — day must be an integer |
| boolean | true | Error — day must be an integer |
| false | false | Error — day must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — day must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — day must be an int64 |
| empty array | [] | Error — day must be an integer |
| numeric array | [1,2,3] | Error — day must be an integer |
| mixed array | [1,null,"x",3] | Error — day must be an integer |
| nested array | [[1,2],[3]] | Error — day must be an integer |
| empty object | {} | Error — day must be an integer |
| object | {"x":1} | Error — day must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — day must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704067200000'} (date) |

**Argument: `hour`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704146400000'} (date) |
| decimal | 2.5 | Error — hour must be an int64 |
| numeric string | "12" | Error — hour must be an integer |
| text | "hello" | Error — hour must be an integer |
| empty string | "" | Error — hour must be an integer |
| boolean | true | Error — hour must be an integer |
| false | false | Error — hour must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — hour must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — hour must be an int64 |
| empty array | [] | Error — hour must be an integer |
| numeric array | [1,2,3] | Error — hour must be an integer |
| mixed array | [1,null,"x",3] | Error — hour must be an integer |
| nested array | [[1,2],[3]] | Error — hour must be an integer |
| empty object | {} | Error — hour must be an integer |
| object | {"x":1} | Error — hour must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — hour must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `minute`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704153480000'} (date) |
| decimal | 2.5 | Error — minute must be an int64 |
| numeric string | "12" | Error — minute must be an integer |
| text | "hello" | Error — minute must be an integer |
| empty string | "" | Error — minute must be an integer |
| boolean | true | Error — minute must be an integer |
| false | false | Error — minute must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — minute must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — minute must be an int64 |
| empty array | [] | Error — minute must be an integer |
| numeric array | [1,2,3] | Error — minute must be an integer |
| mixed array | [1,null,"x",3] | Error — minute must be an integer |
| nested array | [[1,2],[3]] | Error — minute must be an integer |
| empty object | {} | Error — minute must be an integer |
| object | {"x":1} | Error — minute must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — minute must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `second`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704153598000'} (date) |
| decimal | 2.5 | Error — second must be an int64 |
| numeric string | "12" | Error — second must be an integer |
| text | "hello" | Error — second must be an integer |
| empty string | "" | Error — second must be an integer |
| boolean | true | Error — second must be an integer |
| false | false | Error — second must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — second must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — second must be an int64 |
| empty array | [] | Error — second must be an integer |
| numeric array | [1,2,3] | Error — second must be an integer |
| mixed array | [1,null,"x",3] | Error — second must be an integer |
| nested array | [[1,2],[3]] | Error — second must be an integer |
| empty object | {} | Error — second must be an integer |
| object | {"x":1} | Error — second must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — second must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `millisecond`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | {'$numberLong': '1704153600000'} (date) |
| negative | -2 | {'$numberLong': '1704153599998'} (date) |
| decimal | 2.5 | Error — millisecond must be an int64 |
| numeric string | "12" | Error — millisecond must be an integer |
| text | "hello" | Error — millisecond must be an integer |
| empty string | "" | Error — millisecond must be an integer |
| boolean | true | Error — millisecond must be an integer |
| false | false | Error — millisecond must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — millisecond must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — millisecond must be an int64 |
| empty array | [] | Error — millisecond must be an integer |
| numeric array | [1,2,3] | Error — millisecond must be an integer |
| mixed array | [1,null,"x",3] | Error — millisecond must be an integer |
| nested array | [[1,2],[3]] | Error — millisecond must be an integer |
| empty object | {} | Error — millisecond must be an integer |
| object | {"x":1} | Error — millisecond must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — millisecond must be an integer |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `isoWeekYear`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — Cannot mix ISO week and calendar fields |
| negative | -2 | Error — Cannot mix ISO week and calendar fields |
| decimal | 2.5 | Error — Cannot mix ISO week and calendar fields |
| numeric string | "12" | Error — Cannot mix ISO week and calendar fields |
| text | "hello" | Error — Cannot mix ISO week and calendar fields |
| empty string | "" | Error — Cannot mix ISO week and calendar fields |
| boolean | true | Error — Cannot mix ISO week and calendar fields |
| false | false | Error — Cannot mix ISO week and calendar fields |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Cannot mix ISO week and calendar fields |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Cannot mix ISO week and calendar fields |
| empty array | [] | Error — Cannot mix ISO week and calendar fields |
| numeric array | [1,2,3] | Error — Cannot mix ISO week and calendar fields |
| mixed array | [1,null,"x",3] | Error — Cannot mix ISO week and calendar fields |
| nested array | [[1,2],[3]] | Error — Cannot mix ISO week and calendar fields |
| empty object | {} | Error — Cannot mix ISO week and calendar fields |
| object | {"x":1} | Error — Cannot mix ISO week and calendar fields |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Cannot mix ISO week and calendar fields |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `isoWeek`**

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

**Argument: `isoDayOfWeek`**

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

**Argument: `timezone`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — timezone must be a string |
| negative | -2 | Error — timezone must be a string |
| decimal | 2.5 | Error — timezone must be a string |
| numeric string | "12" | Error — Invalid ID for region-based ZoneId, invalid format: 12 |
| text | "hello" | Error — Unknown time-zone ID: hello |
| empty string | "" | Error — Invalid ID for ZoneOffset, invalid format:  |
| boolean | true | Error — timezone must be a string |
| false | false | Error — timezone must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — timezone must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — timezone must be a string |
| empty array | [] | Error — timezone must be a string |
| numeric array | [1,2,3] | Error — timezone must be a string |
| mixed array | [1,null,"x",3] | Error — timezone must be a string |
| nested array | [[1,2],[3]] | Error — timezone must be a string |
| empty object | {} | Error — timezone must be a string |
| object | {"x":1} | Error — timezone must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Invalid ID for region-based ZoneId, invalid format: 2026-01-15T15:00:00Z |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |


</details>

## Verification

This page records **223 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateFromParts.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **39 exact BSON matches**, **144 both rejected**, **40 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| isoWeekYear / null | null | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeekYear / missing | null | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / null | null | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / missing | null | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / zero | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / negative | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / decimal | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / numeric string | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / text | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / empty string | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / boolean | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / false | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / typed date | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / decimal128 | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / empty array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / numeric array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / mixed array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / nested array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / empty object | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / object | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoWeek / ISO date string | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / null | null | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / missing | null | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / zero | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / negative | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / decimal | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / numeric string | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / text | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / empty string | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / boolean | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / false | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / typed date | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / decimal128 | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / empty array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / numeric array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / mixed array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / nested array | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / empty object | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / object | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |
| isoDayOfWeek / ISO date string | {'$numberLong': '1704153600000'} (date) | Error — Invalid $project :: caused by :: $dateFromParts does not allow mixing natural dates with ISO dates |

</details>

[Download full comparison evidence](../../downloads/operator-parity/dateFromParts.json).

<!-- END MONGO PARITY -->

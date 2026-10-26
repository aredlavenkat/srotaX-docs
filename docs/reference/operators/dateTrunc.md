# $dateTrunc

## Definition

Truncates a date and returns a date value.

**Expression operator** · Dates · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$dateTrunc": {
    "date": <date>,
    "unit": <unit>,
    "binSize": <binSize>,
    "timezone": <timezone>,
    "startOfWeek": <startOfWeek>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `date` | Yes | Expression supplying the date to process. |
| `unit` | Yes | Time unit name, such as `"day"` or `"hour"`. See Supported values below. |
| `binSize` | No | Number of units in each truncation interval. Defaults to 1. |
| `timezone` | No | Timezone name or offset used for the calendar operation, for example `"America/Toronto"` or `"+05:30"`. Defaults to UTC when omitted. |
| `startOfWeek` | No | Weekday name for week-based calculations, for example `"monday"`. |

## Supported values

`unit`: `"year"`, `"quarter"`, `"month"`, `"week"`, `"day"`, `"hour"`, `"minute"`, `"second"`, `"millisecond"`. Names are case-sensitive. An omitted timezone defaults to UTC for these named date operators. Where supported, `startOfWeek` defaults to Sunday and accepts full weekday names or three-letter abbreviations, case-insensitively.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `date` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — Expected a date; convert strings with $toDate |
| numeric string | "12" | Error — Cannot convert value to date: 12 |
| text | "hello" | Error — Cannot convert value to date: hello |
| boolean | true | Error — Expected a date; convert strings with $toDate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768435200000'} (date) |
| empty array | [] | Error — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error — Expected a date; convert strings with $toDate |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$dateTrunc":[]} | Error — Date operator requires named arguments |
| {"$dateTrunc":{"unexpected":1}} | null |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `date`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — Expected a date; convert strings with $toDate |
| negative | -2 | Error — Expected a date; convert strings with $toDate |
| decimal | 2.5 | Error — Expected a date; convert strings with $toDate |
| numeric string | "12" | Error — Cannot convert value to date: 12 |
| text | "hello" | Error — Cannot convert value to date: hello |
| empty string | "" | Error — Cannot convert value to date:  |
| boolean | true | Error — Expected a date; convert strings with $toDate |
| false | false | Error — Expected a date; convert strings with $toDate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768435200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Expected a date; convert strings with $toDate |
| empty array | [] | Error — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error — Expected a date; convert strings with $toDate |
| empty object | {} | Error — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | {'$numberLong': '1768435200000'} (date) |
| omitted named argument | Argument removed | null |

**Argument: `unit`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — unit must be a string |
| negative | -2 | Error — unit must be a string |
| decimal | 2.5 | Error — unit must be a string |
| numeric string | "12" | Error — Invalid date unit: 12 |
| text | "hello" | Error — Invalid date unit: hello |
| empty string | "" | Error — Invalid date unit:  |
| boolean | true | Error — unit must be a string |
| false | false | Error — unit must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — unit must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — unit must be a string |
| empty array | [] | Error — unit must be a string |
| numeric array | [1,2,3] | Error — unit must be a string |
| mixed array | [1,null,"x",3] | Error — unit must be a string |
| nested array | [[1,2],[3]] | Error — unit must be a string |
| empty object | {} | Error — unit must be a string |
| object | {"x":1} | Error — unit must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Invalid date unit: 2026-01-15T15:00:00Z |
| omitted named argument | Argument removed | null |

**Argument: `binSize`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — binSize must be positive |
| negative | -2 | Error — binSize must be positive |
| decimal | 2.5 | Error — binSize must be an int64 |
| numeric string | "12" | Error — binSize must be an integer |
| text | "hello" | Error — binSize must be an integer |
| empty string | "" | Error — binSize must be an integer |
| boolean | true | Error — binSize must be an integer |
| false | false | Error — binSize must be an integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — binSize must be an integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — binSize must be an int64 |
| empty array | [] | Error — binSize must be an integer |
| numeric array | [1,2,3] | Error — binSize must be an integer |
| mixed array | [1,null,"x",3] | Error — binSize must be an integer |
| nested array | [[1,2],[3]] | Error — binSize must be an integer |
| empty object | {} | Error — binSize must be an integer |
| object | {"x":1} | Error — binSize must be an integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — binSize must be an integer |
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

**Argument: `startOfWeek`**

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


</details>

## Verification

This page records **103 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateTrunc.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **30 exact BSON matches**, **67 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| date / ISO date string | {'$numberLong': '1768435200000'} (date) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $dateTrunc requires 'date' to be a date, but got string |
| startOfWeek / null | null | {'$numberLong': '1704153600000'} (date) |
| startOfWeek / missing | null | {'$numberLong': '1704153600000'} (date) |
| date / omitted named argument | null | Error — Invalid $project :: caused by :: Missing 'date' parameter to $dateTrunc |
| unit / omitted named argument | null | Error — Invalid $project :: caused by :: Missing 'unit' parameter to $dateTrunc |
| all / unknown option | null | Error — Invalid $project :: caused by :: Unrecognized argument to $dateTrunc: unexpected. Expected arguments are date, unit, and optionally, binSize, timezone, startOfWeek |

</details>

[Download full comparison evidence](../../downloads/operator-parity/dateTrunc.json).

<!-- END MONGO PARITY -->

# $dateDiff

## Definition

Counts elapsed whole units between dates.

**Expression operator** · Dates · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$dateDiff": {
    "startDate": <startDate>,
    "endDate": <endDate>,
    "unit": <unit>,
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
| `startDate` | Yes | Expression supplying the starting date. |
| `endDate` | Yes | Expression supplying the ending date. |
| `unit` | Yes | Time unit name, such as `"day"` or `"hour"`. See Supported values below. |
| `timezone` | No | Timezone name or offset used for the calendar operation, for example `"America/Toronto"` or `"+05:30"`. Defaults to UTC when omitted. |
| `startOfWeek` | No | Weekday name for week-based calculations, for example `"monday"`. |

## Supported values

`unit`: `"year"`, `"quarter"`, `"month"`, `"week"`, `"day"`, `"hour"`, `"minute"`, `"second"`, `"millisecond"`. Names are case-sensitive. An omitted timezone defaults to UTC for these named date operators. Where supported, `startOfWeek` defaults to Sunday and accepts full weekday names or three-letter abbreviations, case-insensitively.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `startDate` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — Expected a date; convert strings with $toDate |
| numeric string | "12" | Error — Cannot convert value to date: 12 |
| text | "hello" | Error — Cannot convert value to date: hello |
| boolean | true | Error — Expected a date; convert strings with $toDate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | -743 (int64) |
| empty array | [] | Error — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error — Expected a date; convert strings with $toDate |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$dateDiff":[]} | Error — Date operator requires named arguments |
| {"$dateDiff":{"unexpected":1}} | null |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `startDate`**

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | -743 (int64) |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Expected a date; convert strings with $toDate |
| empty array | [] | Error — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error — Expected a date; convert strings with $toDate |
| empty object | {} | Error — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | -743 (int64) |
| omitted named argument | Argument removed | null |

**Argument: `endDate`**

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 745 (int64) |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Expected a date; convert strings with $toDate |
| empty array | [] | Error — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error — Expected a date; convert strings with $toDate |
| empty object | {} | Error — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | 745 (int64) |
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
| omitted named argument | Argument removed | 2 (int64) |

**Argument: `startOfWeek`**

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


</details>

## Verification

This page records **103 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateDiff.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **32 exact BSON matches**, **65 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| startDate / ISO date string | -743 (int64) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $dateDiff requires 'startDate' to be a date, but got string |
| endDate / ISO date string | 745 (int64) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $dateDiff requires 'endDate' to be a date, but got string |
| startDate / omitted named argument | null | Error — Invalid $project :: caused by :: Missing 'startDate' parameter to $dateDiff |
| endDate / omitted named argument | null | Error — Invalid $project :: caused by :: Missing 'endDate' parameter to $dateDiff |
| unit / omitted named argument | null | Error — Invalid $project :: caused by :: Missing 'unit' parameter to $dateDiff |
| all / unknown option | null | Error — Invalid $project :: caused by :: Unrecognized argument to $dateDiff: unexpected |

</details>

[Download full comparison evidence](../../downloads/operator-parity/dateDiff.json).

<!-- END MONGO PARITY -->

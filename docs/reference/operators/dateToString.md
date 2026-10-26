# $dateToString

## Definition

Formats a typed date using supported numeric format tokens.

**Expression operator** · Dates · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$dateToString": {
    "date": <date>,
    "format": <format>,
    "timezone": <timezone>,
    "onNull": <onNull>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `date` | Yes | Expression supplying the date to process. |
| `format` | No | Date format string. See Supported values below for the tokens implemented by this operator. Default: `%Y-%m-%dT%H:%M:%S.%LZ` for UTC, or `%Y-%m-%dT%H:%M:%S.%L` for a non-UTC zone. |
| `timezone` | No | Timezone name or offset used for the calendar operation, for example `"America/Toronto"` or `"+05:30"`. Defaults to UTC when omitted. |
| `onNull` | No | Fallback expression for null or missing input. If omitted, the null-input result is null. |

## Supported values

Supported `format` tokens: `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`, `%L`, `%j`, `%G`, `%V`, `%u`, `%z`, `%%`, `%w`, `%U`, `%Z`. Unsupported tokens raise an error. For example, `%Y-%m-%d` represents year-month-day.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `date` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| numeric string | "12" | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| text | "hello" | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| boolean | true | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "2026-01-15" |
| empty array | [] | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| numeric array | [1,2,3] | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| object | {"x":1} | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$dateToString":[]} | Error — $dateToString requires date |
| {"$dateToString":{"unexpected":1}} | Error — $dateToString requires date |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `date`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| negative | -2 | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| decimal | 2.5 | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| numeric string | "12" | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| text | "hello" | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| empty string | "" | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| boolean | true | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| false | false | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "2026-01-15" |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| empty array | [] | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| numeric array | [1,2,3] | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| mixed array | [1,null,"x",3] | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| nested array | [[1,2],[3]] | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| empty object | {} | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| object | {"x":1} | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $dateToString date must be a date, timestamp, or ObjectId; convert strings using $toDate |
| omitted named argument | Argument removed | Error — $dateToString requires date |

**Argument: `format`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $dateToString format must be a string |
| negative | -2 | Error — $dateToString format must be a string |
| decimal | 2.5 | Error — $dateToString format must be a string |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | Error — $dateToString format must be a string |
| false | false | Error — $dateToString format must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $dateToString format must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $dateToString format must be a string |
| empty array | [] | Error — $dateToString format must be a string |
| numeric array | [1,2,3] | Error — $dateToString format must be a string |
| mixed array | [1,null,"x",3] | Error — $dateToString format must be a string |
| nested array | [[1,2],[3]] | Error — $dateToString format must be a string |
| empty object | {} | Error — $dateToString format must be a string |
| object | {"x":1} | Error — $dateToString format must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | "2024-01-02T03:04:05.006Z" |

**Argument: `timezone`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $dateToString timezone must be a string |
| negative | -2 | Error — $dateToString timezone must be a string |
| decimal | 2.5 | Error — $dateToString timezone must be a string |
| numeric string | "12" | Error — Invalid ID for region-based ZoneId, invalid format: 12 |
| text | "hello" | Error — Unknown time-zone ID: hello |
| empty string | "" | Error — Invalid ID for ZoneOffset, invalid format:  |
| boolean | true | Error — $dateToString timezone must be a string |
| false | false | Error — $dateToString timezone must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $dateToString timezone must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $dateToString timezone must be a string |
| empty array | [] | Error — $dateToString timezone must be a string |
| numeric array | [1,2,3] | Error — $dateToString timezone must be a string |
| mixed array | [1,null,"x",3] | Error — $dateToString timezone must be a string |
| nested array | [[1,2],[3]] | Error — $dateToString timezone must be a string |
| empty object | {} | Error — $dateToString timezone must be a string |
| object | {"x":1} | Error — $dateToString timezone must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Invalid ID for region-based ZoneId, invalid format: 2026-01-15T15:00:00Z |
| omitted named argument | Argument removed | "2024-01-02" |

**Argument: `onNull`**

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


</details>

## Verification

This page records **83 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateToString.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **34 exact BSON matches**, **49 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/dateToString.json).

<!-- END MONGO PARITY -->

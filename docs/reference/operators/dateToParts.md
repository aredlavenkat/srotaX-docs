# $dateToParts

## Definition

Extracts calendar fields into an object.

**Expression operator** · Dates · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$dateToParts": {
    "date": <date>,
    "timezone": <timezone>,
    "iso8601": <iso8601>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `date` | Yes | Expression supplying the date to process. |
| `timezone` | No | Timezone name or offset used for the calendar operation, for example `"America/Toronto"` or `"+05:30"`. Defaults to UTC when omitted. |
| `iso8601` | No | Boolean selecting ISO week-based output fields. Defaults to false. |

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {"year":2026,"month":1,"day":15,"hour":15,"minute":0,"second":0,"millisecond":0} |
| empty array | [] | Error — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error — Expected a date; convert strings with $toDate |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$dateToParts":[]} | Error — Date operator requires named arguments |
| {"$dateToParts":{"unexpected":1}} | null |

## Examples

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
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {"year":2026,"month":1,"day":15,"hour":15,"minute":0,"second":0,"millisecond":0} |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Expected a date; convert strings with $toDate |
| empty array | [] | Error — Expected a date; convert strings with $toDate |
| numeric array | [1,2,3] | Error — Expected a date; convert strings with $toDate |
| mixed array | [1,null,"x",3] | Error — Expected a date; convert strings with $toDate |
| nested array | [[1,2],[3]] | Error — Expected a date; convert strings with $toDate |
| empty object | {} | Error — Expected a date; convert strings with $toDate |
| object | {"x":1} | Error — Expected a date; convert strings with $toDate |
| ISO date string | "2026-01-15T15:00:00Z" | {"year":2026,"month":1,"day":15,"hour":15,"minute":0,"second":0,"millisecond":0} |
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
| omitted named argument | Argument removed | {"year":2024,"month":1,"day":2,"hour":3,"minute":4,"second":5,"millisecond":6} |

**Argument: `iso8601`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — iso8601 must be boolean |
| missing | Field absent | Error — iso8601 must be boolean |
| zero | 0 | Error — iso8601 must be boolean |
| negative | -2 | Error — iso8601 must be boolean |
| decimal | 2.5 | Error — iso8601 must be boolean |
| numeric string | "12" | Error — iso8601 must be boolean |
| text | "hello" | Error — iso8601 must be boolean |
| empty string | "" | Error — iso8601 must be boolean |
| boolean | true | {"isoWeekYear":2024,"isoWeek":1,"isoDayOfWeek":2,"hour":3,"minute":4,"second":5,"millisecond":6} |
| false | false | {"year":2024,"month":1,"day":2,"hour":3,"minute":4,"second":5,"millisecond":6} |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — iso8601 must be boolean |
| decimal128 | {"$numberDecimal":"1.25"} | Error — iso8601 must be boolean |
| empty array | [] | Error — iso8601 must be boolean |
| numeric array | [1,2,3] | Error — iso8601 must be boolean |
| mixed array | [1,null,"x",3] | Error — iso8601 must be boolean |
| nested array | [[1,2],[3]] | Error — iso8601 must be boolean |
| empty object | {} | Error — iso8601 must be boolean |
| object | {"x":1} | Error — iso8601 must be boolean |
| ISO date string | "2026-01-15T15:00:00Z" | Error — iso8601 must be boolean |
| omitted named argument | Argument removed | {"year":2024,"month":1,"day":2,"hour":3,"minute":4,"second":5,"millisecond":6} |


</details>

## Verification

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateToParts.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **10 exact BSON matches**, **48 both rejected**, **5 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| date / ISO date string | {"year":2026,"month":1,"day":15,"hour":15,"minute":0,"second":0,"millisecond":0} | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type string to Date |
| iso8601 / null | Error — iso8601 must be boolean | null |
| iso8601 / missing | Error — iso8601 must be boolean | null |
| date / omitted named argument | null | Error — Invalid $project :: caused by :: Missing 'date' parameter to $dateToParts |
| all / unknown option | null | Error — Invalid $project :: caused by :: Unrecognized argument to $dateToParts: unexpected |

</details>

[Download full comparison evidence](../../downloads/operator-parity/dateToParts.json).

<!-- END MONGO PARITY -->

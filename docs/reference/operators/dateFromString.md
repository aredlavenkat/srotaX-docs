# $dateFromString

## Definition

Parses a date string and returns a date value.

**Expression operator** · Dates · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$dateFromString": {
    "dateString": <dateString>,
    "format": <format>,
    "timezone": <timezone>,
    "onError": <onError>,
    "onNull": <onNull>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `dateString` | Yes | Expression supplying a date string to parse. |
| `format` | No | Date format string. See Supported values below for the tokens implemented by this operator. |
| `timezone` | No | Timezone name or offset used for the calendar operation, for example `"America/Toronto"` or `"+05:30"`. Defaults to UTC when omitted. |
| `onError` | No | Fallback expression for a supported conversion/parsing failure. If omitted, that failure raises an error. |
| `onNull` | No | Fallback expression for null or missing input. If omitted, the null-input result is null. |

## Supported values

Supported `format` tokens: `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`, `%L`, `%j`, `%G`, `%V`, `%u`, `%z`, `%%`. Unsupported tokens raise an error. For example, `%Y-%m-%d` represents year-month-day.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `dateString` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — Invalid date string or format |
| numeric string | "12" | Error — Invalid date string or format |
| text | "hello" | Error — Invalid date string or format |
| boolean | true | Error — Invalid date string or format |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Invalid date string or format |
| empty array | [] | Error — Invalid date string or format |
| numeric array | [1,2,3] | Error — Invalid date string or format |
| object | {"x":1} | Error — Invalid date string or format |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$dateFromString":[]} | Error — $dateFromString requires dateString |
| {"$dateFromString":{"unexpected":1}} | Error — $dateFromString requires dateString |

## Examples

Expression:
```json
{
  "$dateFromString": {
    "dateString": "2024-01-02T00:00:00Z"
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

**Argument: `dateString`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — Invalid date string or format |
| negative | -2 | Error — Invalid date string or format |
| decimal | 2.5 | Error — Invalid date string or format |
| numeric string | "12" | Error — Invalid date string or format |
| text | "hello" | Error — Invalid date string or format |
| empty string | "" | Error — Invalid date string or format |
| boolean | true | Error — Invalid date string or format |
| false | false | Error — Invalid date string or format |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Invalid date string or format |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Invalid date string or format |
| empty array | [] | Error — Invalid date string or format |
| numeric array | [1,2,3] | Error — Invalid date string or format |
| mixed array | [1,null,"x",3] | Error — Invalid date string or format |
| nested array | [[1,2],[3]] | Error — Invalid date string or format |
| empty object | {} | Error — Invalid date string or format |
| object | {"x":1} | Error — Invalid date string or format |
| ISO date string | "2026-01-15T15:00:00Z" | {'$numberLong': '1768489200000'} (date) |
| omitted named argument | Argument removed | Error — $dateFromString requires dateString |

**Argument: `format`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — Invalid date string or format |
| negative | -2 | Error — Invalid date string or format |
| decimal | 2.5 | Error — Invalid date string or format |
| numeric string | "12" | Error — Invalid date string or format |
| text | "hello" | Error — Invalid date string or format |
| empty string | "" | Error — Invalid date string or format |
| boolean | true | Error — Invalid date string or format |
| false | false | Error — Invalid date string or format |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Invalid date string or format |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Invalid date string or format |
| empty array | [] | Error — Invalid date string or format |
| numeric array | [1,2,3] | Error — Invalid date string or format |
| mixed array | [1,null,"x",3] | Error — Invalid date string or format |
| nested array | [[1,2],[3]] | Error — Invalid date string or format |
| empty object | {} | Error — Invalid date string or format |
| object | {"x":1} | Error — Invalid date string or format |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Invalid date string or format |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `timezone`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — Invalid date string or format |
| negative | -2 | Error — Invalid date string or format |
| decimal | 2.5 | Error — Invalid date string or format |
| numeric string | "12" | Error — Invalid date string or format |
| text | "hello" | Error — Invalid date string or format |
| empty string | "" | Error — Invalid date string or format |
| boolean | true | Error — Invalid date string or format |
| false | false | Error — Invalid date string or format |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Invalid date string or format |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Invalid date string or format |
| empty array | [] | Error — Invalid date string or format |
| numeric array | [1,2,3] | Error — Invalid date string or format |
| mixed array | [1,null,"x",3] | Error — Invalid date string or format |
| nested array | [[1,2],[3]] | Error — Invalid date string or format |
| empty object | {} | Error — Invalid date string or format |
| object | {"x":1} | Error — Invalid date string or format |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Invalid date string or format |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

**Argument: `onError`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | {'$numberLong': '1704153600000'} (date) |
| missing | Field absent | {'$numberLong': '1704153600000'} (date) |
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

**Argument: `onNull`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | {'$numberLong': '1704153600000'} (date) |
| missing | Field absent | {'$numberLong': '1704153600000'} (date) |
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

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateFromString.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **50 exact BSON matches**, **53 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/dateFromString.json).

<!-- END MONGO PARITY -->

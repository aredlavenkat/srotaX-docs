# $dateFromString

Parses a date string and returns a date value.

**Category:** Dates. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `dateString` | STRING | Yes | Expression evaluated against the input |
| `format` | STRING | No | Expression evaluated against the input |
| `timezone` | STRING | No | Expression evaluated against the input |
| `onError` | ANY | No | Expression evaluated against the input |
| `onNull` | ANY | No | Expression evaluated against the input |

Argument count: minimum 1; maximum 5.

Declared result types: **ANY, DATE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `dateString`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — Invalid date string or format |
| negative | -2 | Error: IllegalArgumentException — Invalid date string or format |
| decimal | 2.5 | Error: IllegalArgumentException — Invalid date string or format |
| numeric string | "12" | Error: IllegalArgumentException — Invalid date string or format |
| text | "hello" | Error: IllegalArgumentException — Invalid date string or format |
| empty string | "" | Error: IllegalArgumentException — Invalid date string or format |
| boolean | true | Error: IllegalArgumentException — Invalid date string or format |
| false | false | Error: IllegalArgumentException — Invalid date string or format |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Invalid date string or format |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Invalid date string or format |
| empty array | [] | Error: IllegalArgumentException — Invalid date string or format |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Invalid date string or format |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Invalid date string or format |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Invalid date string or format |
| empty object | {} | Error: IllegalArgumentException — Invalid date string or format |
| object | {"x":1} | Error: IllegalArgumentException — Invalid date string or format |
| ISO date string | "2026-01-15T15:00:00Z" | {'$numberLong': '1768489200000'} (date) |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $dateFromString requires dateString |

### Argument: `format`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — Invalid date string or format |
| negative | -2 | Error: IllegalArgumentException — Invalid date string or format |
| decimal | 2.5 | Error: IllegalArgumentException — Invalid date string or format |
| numeric string | "12" | Error: IllegalArgumentException — Invalid date string or format |
| text | "hello" | Error: IllegalArgumentException — Invalid date string or format |
| empty string | "" | Error: IllegalArgumentException — Invalid date string or format |
| boolean | true | Error: IllegalArgumentException — Invalid date string or format |
| false | false | Error: IllegalArgumentException — Invalid date string or format |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Invalid date string or format |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Invalid date string or format |
| empty array | [] | Error: IllegalArgumentException — Invalid date string or format |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Invalid date string or format |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Invalid date string or format |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Invalid date string or format |
| empty object | {} | Error: IllegalArgumentException — Invalid date string or format |
| object | {"x":1} | Error: IllegalArgumentException — Invalid date string or format |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Invalid date string or format |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `timezone`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — Invalid date string or format |
| negative | -2 | Error: IllegalArgumentException — Invalid date string or format |
| decimal | 2.5 | Error: IllegalArgumentException — Invalid date string or format |
| numeric string | "12" | Error: IllegalArgumentException — Invalid date string or format |
| text | "hello" | Error: IllegalArgumentException — Invalid date string or format |
| empty string | "" | Error: IllegalArgumentException — Invalid date string or format |
| boolean | true | Error: IllegalArgumentException — Invalid date string or format |
| false | false | Error: IllegalArgumentException — Invalid date string or format |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Invalid date string or format |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Invalid date string or format |
| empty array | [] | Error: IllegalArgumentException — Invalid date string or format |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Invalid date string or format |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Invalid date string or format |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Invalid date string or format |
| empty object | {} | Error: IllegalArgumentException — Invalid date string or format |
| object | {"x":1} | Error: IllegalArgumentException — Invalid date string or format |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Invalid date string or format |
| omitted named argument | Argument removed | {'$numberLong': '1704153600000'} (date) |

### Argument: `onError`

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

### Argument: `onNull`

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

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$dateFromString":[]} | Error: IllegalArgumentException — $dateFromString requires dateString |
| {"$dateFromString":{"unexpected":1}} | Error: IllegalArgumentException — $dateFromString requires dateString |

## Scope and reproducibility

This page records **103 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/dateFromString.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **50 exact BSON matches**, **53 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/dateFromString.json).

<!-- END MONGO PARITY -->

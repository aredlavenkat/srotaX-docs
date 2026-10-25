# $subtract

Subtracts numbers, subtracts a millisecond offset from a date, or returns the millisecond difference between two dates.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `left` | DATE, NUMBER | Yes | Expression evaluated against the input |
| `right` | DATE, NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **DATE, NULL, NUMBER**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$subtract": [
    5,
    2
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `left[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | -2.0 (double) |
| negative | -2 | -4.0 (double) |
| decimal | 2.5 | 0.5 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $subtract only supports numeric types. |
| text | "hello" | Error: IllegalArgumentException — $subtract only supports numeric types. |
| empty string | "" | Error: IllegalArgumentException — $subtract only supports numeric types. |
| boolean | true | Error: IllegalArgumentException — $subtract only supports numeric types. |
| false | false | Error: IllegalArgumentException — $subtract only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489199998'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | -0.75 (double) |
| empty array | [] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| empty object | {} | Error: IllegalArgumentException — $subtract only supports numeric types. |
| object | {"x":1} | Error: IllegalArgumentException — $subtract only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $subtract only supports numeric types. |

### Argument: `right[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 5.0 (double) |
| negative | -2 | 7.0 (double) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $subtract only supports numeric types. |
| text | "hello" | Error: IllegalArgumentException — $subtract only supports numeric types. |
| empty string | "" | Error: IllegalArgumentException — $subtract only supports numeric types. |
| boolean | true | Error: IllegalArgumentException — $subtract only supports numeric types. |
| false | false | Error: IllegalArgumentException — $subtract only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $subtract only supports numeric types. |
| decimal128 | {"$numberDecimal":"1.25"} | 3.75 (double) |
| empty array | [] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $subtract only supports numeric types. |
| empty object | {} | Error: IllegalArgumentException — $subtract only supports numeric types. |
| object | {"x":1} | Error: IllegalArgumentException — $subtract only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $subtract only supports numeric types. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$subtract":[]} | Error: IllegalArgumentException — $subtract requires exactly two arguments. |
| {"$subtract":{"unexpected":1}} | Error: IllegalArgumentException — $subtract requires exactly two arguments. |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/subtract.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **27 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 3.0 (double) | 3 (int32) |
| left[0] / zero | -2.0 (double) | -2 (int32) |
| left[0] / negative | -4.0 (double) | -4 (int32) |
| left[0] / decimal128 | -0.75 (double) | -0.75 (decimal128) |
| right[1] / zero | 5.0 (double) | 5 (int32) |
| right[1] / negative | 7.0 (double) | 7 (int32) |
| right[1] / decimal128 | 3.75 (double) | 3.75 (decimal128) |

[Download full comparison evidence](../../downloads/operator-parity/subtract.json).

<!-- END MONGO PARITY -->

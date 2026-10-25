# $toDouble

Converts a value to double.

**Category:** Types and conversion. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | NUMBER, STRING | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **DOUBLE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$toDouble": "12.5"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 12.5 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | -2.0 (double) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | 12.0 (double) |
| text | "hello" | Error: IllegalArgumentException — $convert failed for target double |
| empty string | "" | Error: IllegalArgumentException — $convert failed for target double |
| boolean | true | 1.0 (double) |
| false | false | 0.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 1.7684892E12 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (double) |
| empty array | [] | Error: IllegalArgumentException — $convert failed for target double |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $convert failed for target double |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $convert failed for target double |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $convert failed for target double |
| empty object | {} | Error: IllegalArgumentException — $convert failed for target double |
| object | {"x":1} | Error: IllegalArgumentException — $convert failed for target double |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $convert failed for target double |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$toDouble":[]} | Error: IllegalArgumentException — $convert failed for target double |
| {"$toDouble":{"unexpected":1}} | Error: IllegalArgumentException — $convert failed for target double |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toDouble.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **11 exact BSON matches**, **11 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/toDouble.json).

<!-- END MONGO PARITY -->

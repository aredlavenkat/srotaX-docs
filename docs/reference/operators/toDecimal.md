# $toDecimal

Converts a value to decimal.

**Category:** Types and conversion. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | NUMBER, STRING | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **DECIMAL, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$toDecimal": "12.5"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 12.5 (decimal128).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (decimal128) |
| negative | -2 | -2 (decimal128) |
| decimal | 2.5 | 2.5 (decimal128) |
| numeric string | "12" | 12 (decimal128) |
| text | "hello" | Error: IllegalArgumentException — $convert failed for target decimal |
| empty string | "" | Error: IllegalArgumentException — $convert failed for target decimal |
| boolean | true | 1 (decimal128) |
| false | false | 0 (decimal128) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 1768489200000 (decimal128) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| empty array | [] | Error: IllegalArgumentException — $convert failed for target decimal |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $convert failed for target decimal |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $convert failed for target decimal |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $convert failed for target decimal |
| empty object | {} | Error: IllegalArgumentException — $convert failed for target decimal |
| object | {"x":1} | Error: IllegalArgumentException — $convert failed for target decimal |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $convert failed for target decimal |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$toDecimal":[]} | Error: IllegalArgumentException — $convert failed for target decimal |
| {"$toDecimal":{"unexpected":1}} | Error: IllegalArgumentException — $convert failed for target decimal |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toDecimal.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **10 exact BSON matches**, **11 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / decimal | 2.5 (decimal128) | 2.50000000000000 (decimal128) |

[Download full comparison evidence](../../downloads/operator-parity/toDecimal.json).

<!-- END MONGO PARITY -->

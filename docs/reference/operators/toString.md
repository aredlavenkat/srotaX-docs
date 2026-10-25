# $toString

Converts a value to a string.

**Category:** Types and conversion. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | BOOLEAN, NUMBER, STRING | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **NULL, STRING**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$toString": 12
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "12".

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | "0" |
| negative | -2 | "-2" |
| decimal | 2.5 | "2.5" |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | "true" |
| false | false | "false" |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "2026-01-15T15:00:00.000Z" |
| decimal128 | {"$numberDecimal":"1.25"} | "1.25" |
| empty array | [] | Error: IllegalArgumentException — $convert failed for target string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $convert failed for target string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $convert failed for target string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $convert failed for target string |
| empty object | {} | Error: IllegalArgumentException — $convert failed for target string |
| object | {"x":1} | Error: IllegalArgumentException — $convert failed for target string |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$toString":[]} | Error: IllegalArgumentException — $convert failed for target string |
| {"$toString":{"unexpected":1}} | Error: IllegalArgumentException — $convert failed for target string |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toString.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **14 exact BSON matches**, **1 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / empty array | Error: IllegalArgumentException — $convert failed for target string | "[]" |
| input / numeric array | Error: IllegalArgumentException — $convert failed for target string | "[1,2,3]" |
| input / mixed array | Error: IllegalArgumentException — $convert failed for target string | "[1,null,\"x\",3]" |
| input / nested array | Error: IllegalArgumentException — $convert failed for target string | "[[1,2],[3]]" |
| input / empty object | Error: IllegalArgumentException — $convert failed for target string | "{}" |
| input / object | Error: IllegalArgumentException — $convert failed for target string | "{\"x\":1}" |
| all / unknown option | Error: IllegalArgumentException — $convert failed for target string | "{\"unexpected\":1}" |

[Download full comparison evidence](../../downloads/operator-parity/toString.json).

<!-- END MONGO PARITY -->

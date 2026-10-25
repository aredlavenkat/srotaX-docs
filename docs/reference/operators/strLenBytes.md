# $strLenBytes

Counts UTF-8 bytes in a string.

**Category:** Text. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **INT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$strLenBytes": "abc"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $strLenBytes requires a string. |
| missing | Field absent | Error: IllegalArgumentException — $strLenBytes requires a string. |
| zero | 0 | Error: IllegalArgumentException — $strLenBytes requires a string. |
| negative | -2 | Error: IllegalArgumentException — $strLenBytes requires a string. |
| decimal | 2.5 | Error: IllegalArgumentException — $strLenBytes requires a string. |
| numeric string | "12" | 2 (int32) |
| text | "hello" | 5 (int32) |
| empty string | "" | 0 (int32) |
| boolean | true | Error: IllegalArgumentException — $strLenBytes requires a string. |
| false | false | Error: IllegalArgumentException — $strLenBytes requires a string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $strLenBytes requires a string. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $strLenBytes requires a string. |
| empty array | [] | Error: IllegalArgumentException — $strLenBytes requires a string. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $strLenBytes requires a string. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $strLenBytes requires a string. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $strLenBytes requires a string. |
| empty object | {} | Error: IllegalArgumentException — $strLenBytes requires a string. |
| object | {"x":1} | Error: IllegalArgumentException — $strLenBytes requires a string. |
| ISO date string | "2026-01-15T15:00:00Z" | 20 (int32) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$strLenBytes":[]} | Error: IllegalArgumentException — $strLenBytes requires a string. |
| {"$strLenBytes":{"unexpected":1}} | Error: IllegalArgumentException — $strLenBytes requires a string. |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/strLenBytes.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **17 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/strLenBytes.json).

<!-- END MONGO PARITY -->

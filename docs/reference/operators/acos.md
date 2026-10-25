# $acos

Computes inverse cosine.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **DOUBLE**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$acos": 1
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 0.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $acos expects a numeric argument. |
| missing | Field absent | Error: IllegalArgumentException — $acos expects a numeric argument. |
| zero | 0 | 1.5707963267948966 (double) |
| negative | -2 | Error: IllegalArgumentException — $acos domain is [-1, 1] |
| decimal | 2.5 | Error: IllegalArgumentException — $acos domain is [-1, 1] |
| numeric string | "12" | Error: IllegalArgumentException — $acos expects a numeric argument. |
| text | "hello" | Error: IllegalArgumentException — $acos expects a numeric argument. |
| empty string | "" | Error: IllegalArgumentException — $acos expects a numeric argument. |
| boolean | true | Error: IllegalArgumentException — $acos expects a numeric argument. |
| false | false | Error: IllegalArgumentException — $acos expects a numeric argument. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $acos expects a numeric argument. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $acos domain is [-1, 1] |
| empty array | [] | Error: IllegalArgumentException — $acos expects a numeric argument. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $acos expects a numeric argument. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $acos expects a numeric argument. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $acos expects a numeric argument. |
| empty object | {} | Error: IllegalArgumentException — $acos expects a numeric argument. |
| object | {"x":1} | Error: IllegalArgumentException — $acos expects a numeric argument. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $acos expects a numeric argument. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$acos":[]} | Error: IllegalArgumentException — $acos expects a numeric argument. |
| {"$acos":{"unexpected":1}} | Error: IllegalArgumentException — $acos expects a numeric argument. |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/acos.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **18 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error: IllegalArgumentException — $acos expects a numeric argument. | null |
| input / missing | Error: IllegalArgumentException — $acos expects a numeric argument. | null |

[Download full comparison evidence](../../downloads/operator-parity/acos.json).

<!-- END MONGO PARITY -->

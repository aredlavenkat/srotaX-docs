# $abs

Returns absolute magnitude.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **DOUBLE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$abs": -2
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | 2.0 (double) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $abs requires a numeric argument. |
| text | "hello" | Error: IllegalArgumentException — $abs requires a numeric argument. |
| empty string | "" | Error: IllegalArgumentException — $abs requires a numeric argument. |
| boolean | true | Error: IllegalArgumentException — $abs requires a numeric argument. |
| false | false | Error: IllegalArgumentException — $abs requires a numeric argument. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $abs requires a numeric argument. |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (double) |
| empty array | [] | Error: IllegalArgumentException — $abs requires a numeric argument. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $abs requires a numeric argument. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $abs requires a numeric argument. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $abs requires a numeric argument. |
| empty object | {} | Error: IllegalArgumentException — $abs requires a numeric argument. |
| object | {"x":1} | Error: IllegalArgumentException — $abs requires a numeric argument. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $abs requires a numeric argument. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$abs":[]} | Error: IllegalArgumentException — $abs requires a numeric argument. |
| {"$abs":{"unexpected":1}} | Error: IllegalArgumentException — $abs requires a numeric argument. |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/abs.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **15 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 2.0 (double) | 2 (int32) |
| input / zero | 0.0 (double) | 0 (int32) |
| input / negative | 2.0 (double) | 2 (int32) |
| input / decimal128 | 1.25 (double) | 1.25 (decimal128) |

[Download full comparison evidence](../../downloads/operator-parity/abs.json).

<!-- END MONGO PARITY -->

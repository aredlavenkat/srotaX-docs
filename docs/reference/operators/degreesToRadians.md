# $degreesToRadians

Computes conversion from degrees to radians.

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
  "$degreesToRadians": 0
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
| null | null | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| missing | Field absent | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| zero | 0 | 0.0 (double) |
| negative | -2 | -0.03490658503988659 (double) |
| decimal | 2.5 | 0.04363323129985824 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| text | "hello" | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| empty string | "" | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| boolean | true | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| false | false | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| decimal128 | {"$numberDecimal":"1.25"} | 0.02181661564992912 (double) |
| empty array | [] | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| empty object | {} | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| object | {"x":1} | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$degreesToRadians":[]} | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |
| {"$degreesToRadians":{"unexpected":1}} | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/degreesToRadians.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **15 both rejected**, **3 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. | null |
| input / missing | Error: IllegalArgumentException — $degreesToRadians expects a numeric input. | null |
| input / decimal128 | 0.02181661564992912 (double) | 0.02181661564992911971154613460610766 (decimal128) |

[Download full comparison evidence](../../downloads/operator-parity/degreesToRadians.json).

<!-- END MONGO PARITY -->

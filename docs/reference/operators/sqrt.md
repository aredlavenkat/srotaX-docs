# $sqrt

Computes the square root.

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
  "$sqrt": 4
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
| negative | -2 | Error: IllegalArgumentException — $sqrt does not support negative numbers. |
| decimal | 2.5 | 1.5811388300841898 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| text | "hello" | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| empty string | "" | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| boolean | true | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| false | false | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| decimal128 | {"$numberDecimal":"1.25"} | 1.118033988749895 (double) |
| empty array | [] | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| empty object | {} | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| object | {"x":1} | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $sqrt expects a numeric argument. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$sqrt":[]} | Error: IllegalArgumentException — $sqrt expects a numeric argument. |
| {"$sqrt":{"unexpected":1}} | Error: IllegalArgumentException — $sqrt expects a numeric argument. |

## Additional boundary examples

<details>
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$sqrt": -1
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $sqrt does not support negative numbers..

</details>

## Scope and reproducibility

This page records **23 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/sqrt.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **17 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / decimal128 | 1.118033988749895 (double) | 1.118033988749894848204586834365638 (decimal128) |

[Download full comparison evidence](../../downloads/operator-parity/sqrt.json).

<!-- END MONGO PARITY -->

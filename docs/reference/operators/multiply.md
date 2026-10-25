# $multiply

Multiplies numeric operands.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `number` | NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 0; maximum variadic.

Declared result types: **DOUBLE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$multiply": [
    2,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 6.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `number[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | -6.0 (double) |
| decimal | 2.5 | 7.5 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $multiply only supports numeric types. |
| text | "hello" | Error: IllegalArgumentException — $multiply only supports numeric types. |
| empty string | "" | Error: IllegalArgumentException — $multiply only supports numeric types. |
| boolean | true | Error: IllegalArgumentException — $multiply only supports numeric types. |
| false | false | Error: IllegalArgumentException — $multiply only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $multiply only supports numeric types. |
| decimal128 | {"$numberDecimal":"1.25"} | 3.75 (double) |
| empty array | [] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| empty object | {} | Error: IllegalArgumentException — $multiply only supports numeric types. |
| object | {"x":1} | Error: IllegalArgumentException — $multiply only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $multiply only supports numeric types. |

### Argument: `number[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | -4.0 (double) |
| decimal | 2.5 | 5.0 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $multiply only supports numeric types. |
| text | "hello" | Error: IllegalArgumentException — $multiply only supports numeric types. |
| empty string | "" | Error: IllegalArgumentException — $multiply only supports numeric types. |
| boolean | true | Error: IllegalArgumentException — $multiply only supports numeric types. |
| false | false | Error: IllegalArgumentException — $multiply only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $multiply only supports numeric types. |
| decimal128 | {"$numberDecimal":"1.25"} | 2.5 (double) |
| empty array | [] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $multiply only supports numeric types. |
| empty object | {} | Error: IllegalArgumentException — $multiply only supports numeric types. |
| object | {"x":1} | Error: IllegalArgumentException — $multiply only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $multiply only supports numeric types. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$multiply":[]} | 1.0 (double) |
| {"$multiply":{"unexpected":1}} | Error: IllegalArgumentException — $multiply requires an array of values. |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/multiply.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **6 exact BSON matches**, **27 both rejected**, **8 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 6.0 (double) | 6 (int32) |
| number[0] / zero | 0.0 (double) | 0 (int32) |
| number[0] / negative | -6.0 (double) | -6 (int32) |
| number[0] / decimal128 | 3.75 (double) | 3.75 (decimal128) |
| number[1] / zero | 0.0 (double) | 0 (int32) |
| number[1] / negative | -4.0 (double) | -4 (int32) |
| number[1] / decimal128 | 2.5 (double) | 2.50 (decimal128) |
| all / empty arguments | 1.0 (double) | 1 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/multiply.json).

<!-- END MONGO PARITY -->

# $log

Computes a logarithm using the supplied base.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `left` | NUMBER | Yes | Expression evaluated against the input |
| `right` | NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **DOUBLE**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$log": [
    8,
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
| null | null | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| missing | Field absent | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| zero | 0 | Error: IllegalArgumentException — $log requires positive number and base != 1 |
| negative | -2 | Error: IllegalArgumentException — $log requires positive number and base != 1 |
| decimal | 2.5 | 1.3219280948873624 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| text | "hello" | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| empty string | "" | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| boolean | true | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| false | false | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | 0.32192809488736235 (double) |
| empty array | [] | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| empty object | {} | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| object | {"x":1} | Error: IllegalArgumentException — $log number must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $log number must resolve to a numeric value |

### Argument: `right[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| missing | Field absent | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| zero | 0 | Error: IllegalArgumentException — $log requires positive number and base != 1 |
| negative | -2 | Error: IllegalArgumentException — $log requires positive number and base != 1 |
| decimal | 2.5 | 2.26941239209809 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| text | "hello" | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| empty string | "" | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| boolean | true | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| false | false | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| decimal128 | {"$numberDecimal":"1.25"} | 9.318851158516168 (double) |
| empty array | [] | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| empty object | {} | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| object | {"x":1} | Error: IllegalArgumentException — $log base must resolve to a numeric value |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $log base must resolve to a numeric value |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$log":[]} | Error: IllegalArgumentException — $log expects [number, base] |
| {"$log":{"unexpected":1}} | Error: IllegalArgumentException — $log expects [number, base] |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/log.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **32 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| left[0] / null | Error: IllegalArgumentException — $log number must resolve to a numeric value | null |
| left[0] / missing | Error: IllegalArgumentException — $log number must resolve to a numeric value | null |
| left[0] / decimal128 | 0.32192809488736235 (double) | 0.3219280948873623478703194294893902 (decimal128) |
| right[1] / null | Error: IllegalArgumentException — $log base must resolve to a numeric value | null |
| right[1] / missing | Error: IllegalArgumentException — $log base must resolve to a numeric value | null |
| right[1] / decimal128 | 9.318851158516168 (double) | 9.318851158516169628007195475350726 (decimal128) |

[Download full comparison evidence](../../downloads/operator-parity/log.json).

<!-- END MONGO PARITY -->

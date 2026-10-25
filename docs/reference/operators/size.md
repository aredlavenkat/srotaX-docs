# $size

Counts elements of an array.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **INT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$size": {
    "$literal": [
      1,
      2
    ]
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $size requires an array |
| missing | Field absent | Error: IllegalArgumentException — $size requires an array |
| zero | 0 | Error: IllegalArgumentException — $size requires an array |
| negative | -2 | Error: IllegalArgumentException — $size requires an array |
| decimal | 2.5 | Error: IllegalArgumentException — $size requires an array |
| numeric string | "12" | Error: IllegalArgumentException — $size requires an array |
| text | "hello" | Error: IllegalArgumentException — $size requires an array |
| empty string | "" | Error: IllegalArgumentException — $size requires an array |
| boolean | true | Error: IllegalArgumentException — $size requires an array |
| false | false | Error: IllegalArgumentException — $size requires an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $size requires an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $size requires an array |
| empty array | [] | 0 (int32) |
| numeric array | [1,2,3] | 3 (int32) |
| mixed array | [1,null,"x",3] | 4 (int32) |
| nested array | [[1,2],[3]] | 2 (int32) |
| empty object | {} | Error: IllegalArgumentException — $size requires an array |
| object | {"x":1} | Error: IllegalArgumentException — $size requires an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $size requires an array |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$size":[]} | Error: IllegalArgumentException — $size requires one argument |
| {"$size":{"unexpected":1}} | Error: IllegalArgumentException — $size requires an array |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/size.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **17 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/size.json).

<!-- END MONGO PARITY -->

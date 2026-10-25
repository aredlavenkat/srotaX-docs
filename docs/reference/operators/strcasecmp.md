# $strcasecmp

Compares lower-cased strings.

**Category:** Text. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `left` | STRING | Yes | Expression evaluated against the input |
| `right` | STRING | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **INT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$strcasecmp": [
    "CA",
    "ca"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 0 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `left[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $strcasecmp expects two strings |
| missing | Field absent | Error: IllegalArgumentException — $strcasecmp expects two strings |
| zero | 0 | Error: IllegalArgumentException — $strcasecmp expects two strings |
| negative | -2 | Error: IllegalArgumentException — $strcasecmp expects two strings |
| decimal | 2.5 | Error: IllegalArgumentException — $strcasecmp expects two strings |
| numeric string | "12" | -50 (int32) |
| text | "hello" | 5 (int32) |
| empty string | "" | -2 (int32) |
| boolean | true | Error: IllegalArgumentException — $strcasecmp expects two strings |
| false | false | Error: IllegalArgumentException — $strcasecmp expects two strings |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| empty array | [] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| empty object | {} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| object | {"x":1} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| ISO date string | "2026-01-15T15:00:00Z" | -49 (int32) |

### Argument: `right[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $strcasecmp expects two strings |
| missing | Field absent | Error: IllegalArgumentException — $strcasecmp expects two strings |
| zero | 0 | Error: IllegalArgumentException — $strcasecmp expects two strings |
| negative | -2 | Error: IllegalArgumentException — $strcasecmp expects two strings |
| decimal | 2.5 | Error: IllegalArgumentException — $strcasecmp expects two strings |
| numeric string | "12" | 50 (int32) |
| text | "hello" | -5 (int32) |
| empty string | "" | 2 (int32) |
| boolean | true | Error: IllegalArgumentException — $strcasecmp expects two strings |
| false | false | Error: IllegalArgumentException — $strcasecmp expects two strings |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| empty array | [] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $strcasecmp expects two strings |
| empty object | {} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| object | {"x":1} | Error: IllegalArgumentException — $strcasecmp expects two strings |
| ISO date string | "2026-01-15T15:00:00Z" | 49 (int32) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$strcasecmp":[]} | Error: IllegalArgumentException — $strcasecmp expects [string1, string2] |
| {"$strcasecmp":{"unexpected":1}} | Error: IllegalArgumentException — $strcasecmp expects [string1, string2] |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/strcasecmp.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **1 exact BSON matches**, **18 both rejected**, **22 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| left[0] / null | Error: IllegalArgumentException — $strcasecmp expects two strings | -1 (int32) |
| left[0] / missing | Error: IllegalArgumentException — $strcasecmp expects two strings | -1 (int32) |
| left[0] / zero | Error: IllegalArgumentException — $strcasecmp expects two strings | -1 (int32) |
| left[0] / negative | Error: IllegalArgumentException — $strcasecmp expects two strings | -1 (int32) |
| left[0] / decimal | Error: IllegalArgumentException — $strcasecmp expects two strings | -1 (int32) |
| left[0] / numeric string | -50 (int32) | -1 (int32) |
| left[0] / text | 5 (int32) | 1 (int32) |
| left[0] / empty string | -2 (int32) | -1 (int32) |
| left[0] / typed date | Error: IllegalArgumentException — $strcasecmp expects two strings | -1 (int32) |
| left[0] / decimal128 | Error: IllegalArgumentException — $strcasecmp expects two strings | -1 (int32) |
| left[0] / ISO date string | -49 (int32) | -1 (int32) |
| right[1] / null | Error: IllegalArgumentException — $strcasecmp expects two strings | 1 (int32) |
| right[1] / missing | Error: IllegalArgumentException — $strcasecmp expects two strings | 1 (int32) |
| right[1] / zero | Error: IllegalArgumentException — $strcasecmp expects two strings | 1 (int32) |
| right[1] / negative | Error: IllegalArgumentException — $strcasecmp expects two strings | 1 (int32) |
| right[1] / decimal | Error: IllegalArgumentException — $strcasecmp expects two strings | 1 (int32) |
| right[1] / numeric string | 50 (int32) | 1 (int32) |
| right[1] / text | -5 (int32) | -1 (int32) |
| right[1] / empty string | 2 (int32) | 1 (int32) |
| right[1] / typed date | Error: IllegalArgumentException — $strcasecmp expects two strings | 1 (int32) |
| right[1] / decimal128 | Error: IllegalArgumentException — $strcasecmp expects two strings | 1 (int32) |
| right[1] / ISO date string | 49 (int32) | 1 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/strcasecmp.json).

<!-- END MONGO PARITY -->

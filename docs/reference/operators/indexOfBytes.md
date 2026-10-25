# $indexOfBytes

Searches text using byte positions; bounds have known differences.

**Category:** Text. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |
| `search` | STRING | Yes | Expression evaluated against the input |
| `start` | INT | No | Expression evaluated against the input |
| `end` | INT | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 4.

Declared result types: **INT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$indexOfBytes": [
    "hello",
    "ll"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — Expected string. |
| missing | Field absent | Error: IllegalArgumentException — Expected string. |
| zero | 0 | Error: IllegalArgumentException — Expected string. |
| negative | -2 | Error: IllegalArgumentException — Expected string. |
| decimal | 2.5 | Error: IllegalArgumentException — Expected string. |
| numeric string | "12" | -1 (int32) |
| text | "hello" | 2 (int32) |
| empty string | "" | -1 (int32) |
| boolean | true | Error: IllegalArgumentException — Expected string. |
| false | false | Error: IllegalArgumentException — Expected string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Expected string. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected string. |
| empty array | [] | Error: IllegalArgumentException — Expected string. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected string. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected string. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected string. |
| empty object | {} | Error: IllegalArgumentException — Expected string. |
| object | {"x":1} | Error: IllegalArgumentException — Expected string. |
| ISO date string | "2026-01-15T15:00:00Z" | -1 (int32) |

### Argument: `search[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — Expected string. |
| missing | Field absent | Error: IllegalArgumentException — Expected string. |
| zero | 0 | Error: IllegalArgumentException — Expected string. |
| negative | -2 | Error: IllegalArgumentException — Expected string. |
| decimal | 2.5 | Error: IllegalArgumentException — Expected string. |
| numeric string | "12" | -1 (int32) |
| text | "hello" | 0 (int32) |
| empty string | "" | 0 (int32) |
| boolean | true | Error: IllegalArgumentException — Expected string. |
| false | false | Error: IllegalArgumentException — Expected string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Expected string. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected string. |
| empty array | [] | Error: IllegalArgumentException — Expected string. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Expected string. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Expected string. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Expected string. |
| empty object | {} | Error: IllegalArgumentException — Expected string. |
| object | {"x":1} | Error: IllegalArgumentException — Expected string. |
| ISO date string | "2026-01-15T15:00:00Z" | -1 (int32) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$indexOfBytes":[]} | Error: IllegalArgumentException — $indexOfBytes expects [string, substring, [start], [end]] |
| {"$indexOfBytes":{"unexpected":1}} | Error: IllegalArgumentException — $indexOfBytes expects [string, substring, [start], [end]] |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/indexOfBytes.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **9 exact BSON matches**, **30 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input[0] / null | Error: IllegalArgumentException — Expected string. | null |
| input[0] / missing | Error: IllegalArgumentException — Expected string. | null |

[Download full comparison evidence](../../downloads/operator-parity/indexOfBytes.json).

<!-- END MONGO PARITY -->

# $substrBytes

Extracts text from a UTF-8 byte range.

**Category:** Text. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |
| `start` | INT | Yes | Expression evaluated against the input |
| `length` | INT | Yes | Expression evaluated against the input |

Argument count: minimum 3; maximum 3.

Declared result types: **STRING**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$substrBytes": [
    "hello",
    1,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "ell".

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| missing | Field absent | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| zero | 0 | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| negative | -2 | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| decimal | 2.5 | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| numeric string | "12" | "2" |
| text | "hello" | "ell" |
| empty string | "" | "" |
| boolean | true | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| false | false | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| empty array | [] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| empty object | {} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| object | {"x":1} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| ISO date string | "2026-01-15T15:00:00Z" | "026" |

### Argument: `start[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| missing | Field absent | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| zero | 0 | "hel" |
| negative | -2 | "" |
| decimal | 2.5 | "llo" |
| numeric string | "12" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| text | "hello" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| empty string | "" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| boolean | true | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| false | false | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| decimal128 | {"$numberDecimal":"1.25"} | "ell" |
| empty array | [] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| empty object | {} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| object | {"x":1} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |

### Argument: `length[2]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| missing | Field absent | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| zero | 0 | "" |
| negative | -2 | "" |
| decimal | 2.5 | "el" |
| numeric string | "12" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| text | "hello" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| empty string | "" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| boolean | true | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| false | false | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| decimal128 | {"$numberDecimal":"1.25"} | "e" |
| empty array | [] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| empty object | {} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| object | {"x":1} | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $substrBytes expects (string, int, int) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$substrBytes":[]} | Error: IllegalArgumentException — $substrBytes requires [string, start, length] |
| {"$substrBytes":{"unexpected":1}} | Error: IllegalArgumentException — $substrBytes requires [string, start, length] |

## Scope and reproducibility

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/substrBytes.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **11 exact BSON matches**, **40 both rejected**, **9 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input[0] / null | Error: IllegalArgumentException — $substrBytes expects (string, int, int) | "" |
| input[0] / missing | Error: IllegalArgumentException — $substrBytes expects (string, int, int) | "" |
| input[0] / zero | Error: IllegalArgumentException — $substrBytes expects (string, int, int) | "" |
| input[0] / negative | Error: IllegalArgumentException — $substrBytes expects (string, int, int) | "2" |
| input[0] / decimal | Error: IllegalArgumentException — $substrBytes expects (string, int, int) | ".5" |
| input[0] / typed date | Error: IllegalArgumentException — $substrBytes expects (string, int, int) | "026" |
| input[0] / decimal128 | Error: IllegalArgumentException — $substrBytes expects (string, int, int) | ".25" |
| start[1] / negative | "" | Error: Location50752 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $substrBytes:  starting index must be non-negative (got: -2) |
| length[2] / negative | "" | "ello" |

[Download full comparison evidence](../../downloads/operator-parity/substrBytes.json).

<!-- END MONGO PARITY -->

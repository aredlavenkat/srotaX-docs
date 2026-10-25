# $lastN

Returns a new array without changing the source list.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY | Yes | Expression evaluated against the input |
| `n` | NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$lastN": {
    "input": [
      3,
      1,
      2
    ],
    "n": 2
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [1,2].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $lastN input must be an array |
| missing | Field absent | Error: IllegalArgumentException — $lastN input must be an array |
| zero | 0 | Error: IllegalArgumentException — $lastN input must be an array |
| negative | -2 | Error: IllegalArgumentException — $lastN input must be an array |
| decimal | 2.5 | Error: IllegalArgumentException — $lastN input must be an array |
| numeric string | "12" | Error: IllegalArgumentException — $lastN input must be an array |
| text | "hello" | Error: IllegalArgumentException — $lastN input must be an array |
| empty string | "" | Error: IllegalArgumentException — $lastN input must be an array |
| boolean | true | Error: IllegalArgumentException — $lastN input must be an array |
| false | false | Error: IllegalArgumentException — $lastN input must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $lastN input must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $lastN input must be an array |
| empty array | [] | [] |
| numeric array | [1,2,3] | [2,3] |
| mixed array | [1,null,"x",3] | ["x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | Error: IllegalArgumentException — $lastN input must be an array |
| object | {"x":1} | Error: IllegalArgumentException — $lastN input must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $lastN input must be an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $lastN requires input and n |

### Argument: `n`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| missing | Field absent | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| zero | 0 | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| negative | -2 | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| decimal | 2.5 | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| numeric string | "12" | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| text | "hello" | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| empty string | "" | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| boolean | true | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| false | false | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| empty array | [] | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| empty object | {} | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| object | {"x":1} | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $lastN n must be a positive 64-bit integer |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $lastN requires input and n |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$lastN":[]} | Error: IllegalArgumentException — $lastN requires input and n |
| {"$lastN":{"unexpected":1}} | Error: IllegalArgumentException — $lastN requires input and n |

## Scope and reproducibility

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/lastN.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **38 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/lastN.json).

<!-- END MONGO PARITY -->

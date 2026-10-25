# $topN

Sort an array and return its first N items without changing the source.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY, MISSING, NULL | Yes | Expression evaluated against the input |
| `sortBy` | NUMBER, OBJECT | Yes | Literal configuration |
| `n` | NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 3; maximum 3.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$topN": {
    "input": [
      3,
      1,
      2
    ],
    "sortBy": -1,
    "n": 2
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [3,2].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $firstN input must be an array |
| missing | Field absent | Error: IllegalArgumentException — $firstN input must be an array |
| zero | 0 | Error: IllegalArgumentException — $sortArray input must be an array |
| negative | -2 | Error: IllegalArgumentException — $sortArray input must be an array |
| decimal | 2.5 | Error: IllegalArgumentException — $sortArray input must be an array |
| numeric string | "12" | Error: IllegalArgumentException — $sortArray input must be an array |
| text | "hello" | Error: IllegalArgumentException — $sortArray input must be an array |
| empty string | "" | Error: IllegalArgumentException — $sortArray input must be an array |
| boolean | true | Error: IllegalArgumentException — $sortArray input must be an array |
| false | false | Error: IllegalArgumentException — $sortArray input must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $sortArray input must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $sortArray input must be an array |
| empty array | [] | [] |
| numeric array | [1,2,3] | [3,2] |
| mixed array | [1,null,"x",3] | ["x",3] |
| nested array | [[1,2],[3]] | [[3],[1,2]] |
| empty object | {} | Error: IllegalArgumentException — $sortArray input must be an array |
| object | {"x":1} | Error: IllegalArgumentException — $sortArray input must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $sortArray input must be an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $topN requires input, sortBy and n |

### Argument: `sortBy`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| zero | 0 | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| negative | -2 | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| decimal | 2.5 | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| numeric string | "12" | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| text | "hello" | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| empty string | "" | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| boolean | true | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| false | false | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| empty array | [] | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| empty object | {} | Error: IllegalArgumentException — $sortArray sortBy must not be empty |
| object | {"x":1} | [3,1] |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $topN requires input, sortBy and n |

### Argument: `n`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| missing | Field absent | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| zero | 0 | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| negative | -2 | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| decimal | 2.5 | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| numeric string | "12" | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| text | "hello" | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| empty string | "" | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| boolean | true | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| false | false | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| empty array | [] | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| empty object | {} | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| object | {"x":1} | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $topN requires input, sortBy and n |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$topN":[]} | Error: IllegalArgumentException — $topN requires input, sortBy and n |
| {"$topN":{"unexpected":1}} | Error: IllegalArgumentException — $topN requires input, sortBy and n |

## Scope and reproducibility

This page records **62 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/topN.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **6 exact BSON matches**, **50 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error: IllegalArgumentException — $firstN input must be an array | null |
| input / missing | Error: IllegalArgumentException — $firstN input must be an array | null |
| n / null | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer | null |
| n / missing | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer | null |
| n / zero | Error: IllegalArgumentException — $firstN n must be a positive 64-bit integer | [] |
| sortBy / omitted named argument | Error: IllegalArgumentException — $topN requires input, sortBy and n | [1,2] |

[Download full comparison evidence](../../downloads/operator-parity/topN.json).

<!-- END MONGO PARITY -->

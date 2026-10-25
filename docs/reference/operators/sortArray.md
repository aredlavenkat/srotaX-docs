# $sortArray

Returns a new array without changing the source list.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY, MISSING, NULL | Yes | Expression evaluated against the input |
| `sortBy` | NUMBER, OBJECT | Yes | Literal configuration |

Argument count: minimum 2; maximum 2.

Declared result types: **ARRAY, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$sortArray": {
    "input": [
      3,
      1,
      2
    ],
    "sortBy": 1
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [1,2,3].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
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
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [null,1,3,"x"] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | Error: IllegalArgumentException — $sortArray input must be an array |
| object | {"x":1} | Error: IllegalArgumentException — $sortArray input must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $sortArray input must be an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $sortArray requires input and sortBy |

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
| object | {"x":1} | [3,1,2] |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $sortArray sort direction must be 1 or -1 |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $sortArray requires input and sortBy |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$sortArray":[]} | Error: IllegalArgumentException — $sortArray requires input and sortBy |
| {"$sortArray":{"unexpected":1}} | Error: IllegalArgumentException — $sortArray requires input and sortBy |

## Scope and reproducibility

This page records **42 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/sortArray.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **8 exact BSON matches**, **34 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/sortArray.json).

<!-- END MONGO PARITY -->

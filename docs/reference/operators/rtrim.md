# $rtrim

Trims configured characters from the end of text.

**Category:** Text. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |
| `chars` | STRING | No | Expression evaluated against the input |

Argument count: minimum 1; maximum 2.

Declared result types: **NULL, STRING**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$rtrim": {
    "input": "hi  "
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "hi".

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $trim input must be a string |
| negative | -2 | Error: IllegalArgumentException — $trim input must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — $trim input must be a string |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | Error: IllegalArgumentException — $trim input must be a string |
| false | false | Error: IllegalArgumentException — $trim input must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $trim input must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $trim input must be a string |
| empty array | [] | Error: IllegalArgumentException — $trim input must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $trim input must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $trim input must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $trim input must be a string |
| empty object | {} | Error: IllegalArgumentException — $trim input must be a string |
| object | {"x":1} | Error: IllegalArgumentException — $trim input must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $trim requires input and optional chars |

### Argument: `chars`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $trim chars must be a string |
| negative | -2 | Error: IllegalArgumentException — $trim chars must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — $trim chars must be a string |
| numeric string | "12" | "hi  " |
| text | "hello" | "hi  " |
| empty string | "" | "hi  " |
| boolean | true | Error: IllegalArgumentException — $trim chars must be a string |
| false | false | Error: IllegalArgumentException — $trim chars must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $trim chars must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $trim chars must be a string |
| empty array | [] | Error: IllegalArgumentException — $trim chars must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $trim chars must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $trim chars must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $trim chars must be a string |
| empty object | {} | Error: IllegalArgumentException — $trim chars must be a string |
| object | {"x":1} | Error: IllegalArgumentException — $trim chars must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | "hi  " |
| omitted named argument | Argument removed | "hi" |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$rtrim":[]} | Error: IllegalArgumentException — $trim requires input and optional chars |
| {"$rtrim":{"unexpected":1}} | Error: IllegalArgumentException — $trim requires input and optional chars |

## Scope and reproducibility

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/rtrim.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **14 exact BSON matches**, **29 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/rtrim.json).

<!-- END MONGO PARITY -->

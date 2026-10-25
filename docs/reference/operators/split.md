# $split

Splits text using a Java regular-expression delimiter.

**Category:** Text. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |
| `delimiter` | STRING | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$split": [
    "a,b",
    ","
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** ["a","b"].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $split arguments must be strings. |
| missing | Field absent | Error: IllegalArgumentException — $split arguments must be strings. |
| zero | 0 | Error: IllegalArgumentException — $split arguments must be strings. |
| negative | -2 | Error: IllegalArgumentException — $split arguments must be strings. |
| decimal | 2.5 | Error: IllegalArgumentException — $split arguments must be strings. |
| numeric string | "12" | ["12"] |
| text | "hello" | ["hello"] |
| empty string | "" | [""] |
| boolean | true | Error: IllegalArgumentException — $split arguments must be strings. |
| false | false | Error: IllegalArgumentException — $split arguments must be strings. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $split arguments must be strings. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $split arguments must be strings. |
| empty array | [] | Error: IllegalArgumentException — $split arguments must be strings. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $split arguments must be strings. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $split arguments must be strings. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $split arguments must be strings. |
| empty object | {} | Error: IllegalArgumentException — $split arguments must be strings. |
| object | {"x":1} | Error: IllegalArgumentException — $split arguments must be strings. |
| ISO date string | "2026-01-15T15:00:00Z" | ["2026-01-15T15:00:00Z"] |

### Argument: `delimiter[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $split arguments must be strings. |
| missing | Field absent | Error: IllegalArgumentException — $split arguments must be strings. |
| zero | 0 | Error: IllegalArgumentException — $split arguments must be strings. |
| negative | -2 | Error: IllegalArgumentException — $split arguments must be strings. |
| decimal | 2.5 | Error: IllegalArgumentException — $split arguments must be strings. |
| numeric string | "12" | ["a,b"] |
| text | "hello" | ["a,b"] |
| empty string | "" | Error: IllegalArgumentException — $split delimiter must not be empty |
| boolean | true | Error: IllegalArgumentException — $split arguments must be strings. |
| false | false | Error: IllegalArgumentException — $split arguments must be strings. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $split arguments must be strings. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $split arguments must be strings. |
| empty array | [] | Error: IllegalArgumentException — $split arguments must be strings. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $split arguments must be strings. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $split arguments must be strings. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $split arguments must be strings. |
| empty object | {} | Error: IllegalArgumentException — $split arguments must be strings. |
| object | {"x":1} | Error: IllegalArgumentException — $split arguments must be strings. |
| ISO date string | "2026-01-15T15:00:00Z" | ["a,b"] |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$split":[]} | Error: IllegalArgumentException — $split requires [string, delimiter] |
| {"$split":{"unexpected":1}} | Error: IllegalArgumentException — $split requires [string, delimiter] |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/split.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **8 exact BSON matches**, **29 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input[0] / null | Error: IllegalArgumentException — $split arguments must be strings. | null |
| input[0] / missing | Error: IllegalArgumentException — $split arguments must be strings. | null |
| delimiter[1] / null | Error: IllegalArgumentException — $split arguments must be strings. | null |
| delimiter[1] / missing | Error: IllegalArgumentException — $split arguments must be strings. | null |

[Download full comparison evidence](../../downloads/operator-parity/split.json).

<!-- END MONGO PARITY -->

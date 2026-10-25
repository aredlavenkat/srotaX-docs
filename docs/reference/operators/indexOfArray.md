# $indexOfArray

Finds an item using Java equality.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `array` | ARRAY | Yes | Expression evaluated against the input |
| `search` | ANY | Yes | Expression evaluated against the input |
| `start` | INT | No | Expression evaluated against the input |
| `end` | INT | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 4.

Declared result types: **INT, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$indexOfArray": [
    [
      1,
      2
    ],
    2
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 1 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `array[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| negative | -2 | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| decimal | 2.5 | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| numeric string | "12" | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| text | "hello" | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| empty string | "" | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| boolean | true | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| false | false | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| empty array | [] | -1 (int32) |
| numeric array | [1,2,3] | 1 (int32) |
| mixed array | [1,null,"x",3] | -1 (int32) |
| nested array | [[1,2],[3]] | -1 (int32) |
| empty object | {} | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| object | {"x":1} | Error: IllegalArgumentException — $indexOfArray first argument must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $indexOfArray first argument must be an array |

### Argument: `search[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | -1 (int32) |
| missing | Field absent | -1 (int32) |
| zero | 0 | -1 (int32) |
| negative | -2 | -1 (int32) |
| decimal | 2.5 | -1 (int32) |
| numeric string | "12" | -1 (int32) |
| text | "hello" | -1 (int32) |
| empty string | "" | -1 (int32) |
| boolean | true | -1 (int32) |
| false | false | -1 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | -1 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | -1 (int32) |
| empty array | [] | -1 (int32) |
| numeric array | [1,2,3] | -1 (int32) |
| mixed array | [1,null,"x",3] | -1 (int32) |
| nested array | [[1,2],[3]] | -1 (int32) |
| empty object | {} | -1 (int32) |
| object | {"x":1} | -1 (int32) |
| ISO date string | "2026-01-15T15:00:00Z" | -1 (int32) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$indexOfArray":[]} | Error: IllegalArgumentException — $indexOfArray expects 2 to 4 arguments: [array, search, start?, end?] |
| {"$indexOfArray":{"unexpected":1}} | Error: IllegalArgumentException — $indexOfArray expects 2 to 4 arguments: [array, search, start?, end?] |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/indexOfArray.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **26 exact BSON matches**, **15 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/indexOfArray.json).

<!-- END MONGO PARITY -->

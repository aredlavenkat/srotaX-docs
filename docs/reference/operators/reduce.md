# $reduce

Folds an array into an accumulated value.

**Category:** Arrays. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY | Yes | Expression evaluated against the input |
| `initialValue` | ANY | Yes | Expression evaluated against the input |
| `in` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 3; maximum 3.

Declared result types: **ANY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$reduce": {
    "input": [
      1,
      2
    ],
    "initialValue": 0,
    "in": {
      "$add": [
        "$$value",
        "$$this"
      ]
    }
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| missing | Field absent | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| zero | 0 | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| negative | -2 | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| decimal | 2.5 | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| numeric string | "12" | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| text | "hello" | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| empty string | "" | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| boolean | true | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| false | false | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| empty array | [] | 0 (int32) |
| numeric array | [1,2,3] | 6.0 (double) |
| mixed array | [1,null,"x",3] | null |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $add only supports numeric types. |
| empty object | {} | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| object | {"x":1} | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $reduce 'input' must resolve to an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $reduce requires 'input', 'initialValue', and 'in' fields |

### Argument: `initialValue`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 3.0 (double) |
| negative | -2 | 1.0 (double) |
| decimal | 2.5 | 5.5 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $add only supports numeric types. |
| text | "hello" | Error: IllegalArgumentException — $add only supports numeric types. |
| empty string | "" | Error: IllegalArgumentException — $add only supports numeric types. |
| boolean | true | Error: IllegalArgumentException — $add only supports numeric types. |
| false | false | Error: IllegalArgumentException — $add only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200003'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 4.25 (double) |
| empty array | [] | Error: IllegalArgumentException — $add only supports numeric types. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $add only supports numeric types. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $add only supports numeric types. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $add only supports numeric types. |
| empty object | {} | Error: IllegalArgumentException — $add only supports numeric types. |
| object | {"x":1} | Error: IllegalArgumentException — $add only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $add only supports numeric types. |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $reduce requires 'input', 'initialValue', and 'in' fields |

### Argument: `in`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | true |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $reduce requires 'input', 'initialValue', and 'in' fields |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$reduce":[]} | Error: IllegalArgumentException — $reduce expects an object with fields: input, initialValue, in |
| {"$reduce":{"unexpected":1}} | Error: IllegalArgumentException — $reduce requires 'input', 'initialValue', and 'in' fields |

## Additional boundary examples

<details>
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$reduce": {
    "input": [
      1,
      2,
      3
    ],
    "initialValue": 0,
    "in": {
      "$add": [
        "$$value",
        "$$this"
      ]
    }
  }
}
```

Input:
```json
{}
```

**SrotaX:** 6.0 (double).

</details>

## Scope and reproducibility

This page records **64 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/reduce.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **24 exact BSON matches**, **31 both rejected**, **9 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 3.0 (double) | 3 (int32) |
| input / null | Error: IllegalArgumentException — $reduce 'input' must resolve to an array | null |
| input / missing | Error: IllegalArgumentException — $reduce 'input' must resolve to an array | null |
| input / numeric array | 6.0 (double) | 6 (int32) |
| initialValue / zero | 3.0 (double) | 3 (int32) |
| initialValue / negative | 1.0 (double) | 1 (int32) |
| initialValue / decimal128 | 4.25 (double) | 4.25 (decimal128) |
| in / missing | null | Missing (field omitted) |
| all / boundary example | 6.0 (double) | 6 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/reduce.json).

<!-- END MONGO PARITY -->

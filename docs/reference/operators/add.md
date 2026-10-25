# $add

Adds numbers, or adds millisecond offsets to a single date.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `number` | DATE, NUMBER | Yes | Expression evaluated against the input |

Argument count: minimum 0; maximum variadic.

Declared result types: **DATE, NULL, NUMBER**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$add": [
    2,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 5.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `number[0]`

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

### Argument: `number[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 2.0 (double) |
| negative | -2 | 0.0 (double) |
| decimal | 2.5 | 4.5 (double) |
| numeric string | "12" | Error: IllegalArgumentException — $add only supports numeric types. |
| text | "hello" | Error: IllegalArgumentException — $add only supports numeric types. |
| empty string | "" | Error: IllegalArgumentException — $add only supports numeric types. |
| boolean | true | Error: IllegalArgumentException — $add only supports numeric types. |
| false | false | Error: IllegalArgumentException — $add only supports numeric types. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200002'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 3.25 (double) |
| empty array | [] | Error: IllegalArgumentException — $add only supports numeric types. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $add only supports numeric types. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $add only supports numeric types. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $add only supports numeric types. |
| empty object | {} | Error: IllegalArgumentException — $add only supports numeric types. |
| object | {"x":1} | Error: IllegalArgumentException — $add only supports numeric types. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $add only supports numeric types. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$add":[]} | 0.0 (double) |
| {"$add":{"unexpected":1}} | Error: IllegalArgumentException — $add requires an array of values. |

## Additional boundary examples

<details>
<summary>Show 2 tested examples</summary>

Expression:
```json
{
  "$add": [
    2147483647,
    1
  ]
}
```

Input:
```json
{}
```

**SrotaX:** 2.147483648E9 (double).

Expression:
```json
{
  "$add": [
    {
      "$literal": {
        "$numberLong": "9007199254740993"
      }
    },
    1
  ]
}
```

Input:
```json
{}
```

**SrotaX:** 9.007199254740994E15 (double).

</details>

## Scope and reproducibility

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/add.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **8 exact BSON matches**, **25 both rejected**, **10 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 5.0 (double) | 5 (int32) |
| number[0] / zero | 3.0 (double) | 3 (int32) |
| number[0] / negative | 1.0 (double) | 1 (int32) |
| number[0] / decimal128 | 4.25 (double) | 4.25 (decimal128) |
| number[1] / zero | 2.0 (double) | 2 (int32) |
| number[1] / negative | 0.0 (double) | 0 (int32) |
| number[1] / decimal128 | 3.25 (double) | 3.25 (decimal128) |
| all / empty arguments | 0.0 (double) | 0 (int32) |
| all / boundary example | 2.147483648E9 (double) | 2147483648 (int64) |
| all / boundary example | 9.007199254740994E15 (double) | 9007199254740994 (int64) |

[Download full comparison evidence](../../downloads/operator-parity/add.json).

<!-- END MONGO PARITY -->

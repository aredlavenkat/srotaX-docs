# $setDifference

Returns values from the first set absent from the second.

**Category:** Sets. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `array` | ARRAY | Yes | Expression evaluated against the input |
| `other` | ARRAY | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$setDifference": [
    [
      1,
      2
    ],
    [
      2,
      3
    ]
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [1].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `array[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — Expected array. |
| missing | Field absent | Error: IllegalArgumentException — Expected array. |
| zero | 0 | Error: IllegalArgumentException — Expected array. |
| negative | -2 | Error: IllegalArgumentException — Expected array. |
| decimal | 2.5 | Error: IllegalArgumentException — Expected array. |
| numeric string | "12" | Error: IllegalArgumentException — Expected array. |
| text | "hello" | Error: IllegalArgumentException — Expected array. |
| empty string | "" | Error: IllegalArgumentException — Expected array. |
| boolean | true | Error: IllegalArgumentException — Expected array. |
| false | false | Error: IllegalArgumentException — Expected array. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Expected array. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected array. |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1] |
| mixed array | [1,null,"x",3] | [1,null,"x"] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | Error: IllegalArgumentException — Expected array. |
| object | {"x":1} | Error: IllegalArgumentException — Expected array. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Expected array. |

### Argument: `other[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — Expected array. |
| missing | Field absent | Error: IllegalArgumentException — Expected array. |
| zero | 0 | Error: IllegalArgumentException — Expected array. |
| negative | -2 | Error: IllegalArgumentException — Expected array. |
| decimal | 2.5 | Error: IllegalArgumentException — Expected array. |
| numeric string | "12" | Error: IllegalArgumentException — Expected array. |
| text | "hello" | Error: IllegalArgumentException — Expected array. |
| empty string | "" | Error: IllegalArgumentException — Expected array. |
| boolean | true | Error: IllegalArgumentException — Expected array. |
| false | false | Error: IllegalArgumentException — Expected array. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Expected array. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — Expected array. |
| empty array | [] | [1,2] |
| numeric array | [1,2,3] | [] |
| mixed array | [1,null,"x",3] | [2] |
| nested array | [[1,2],[3]] | [1,2] |
| empty object | {} | Error: IllegalArgumentException — Expected array. |
| object | {"x":1} | Error: IllegalArgumentException — Expected array. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Expected array. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$setDifference":[]} | Error: IllegalArgumentException — $setDifference requires exactly two arrays. |
| {"$setDifference":{"unexpected":1}} | Error: IllegalArgumentException — $setDifference requires exactly two arrays. |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setDifference.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **9 exact BSON matches**, **28 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| array[0] / null | Error: IllegalArgumentException — Expected array. | null |
| array[0] / missing | Error: IllegalArgumentException — Expected array. | null |
| other[1] / null | Error: IllegalArgumentException — Expected array. | null |
| other[1] / missing | Error: IllegalArgumentException — Expected array. | null |

[Download full comparison evidence](../../downloads/operator-parity/setDifference.json).

<!-- END MONGO PARITY -->

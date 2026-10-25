# $setEquals

Tests unordered set equality.

**Category:** Sets. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `array` | ARRAY | Yes | Expression evaluated against the input |
| `other` | ARRAY | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum variadic.

Declared result types: **BOOLEAN**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$setEquals": [
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

**Observed SrotaX result:** false.

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `array[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| missing | Field absent | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| zero | 0 | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| negative | -2 | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| decimal | 2.5 | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| numeric string | "12" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| text | "hello" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| empty string | "" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| boolean | true | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| false | false | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| empty array | [] | false |
| numeric array | [1,2,3] | false |
| mixed array | [1,null,"x",3] | false |
| nested array | [[1,2],[3]] | false |
| empty object | {} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| object | {"x":1} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |

### Argument: `other[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| missing | Field absent | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| zero | 0 | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| negative | -2 | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| decimal | 2.5 | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| numeric string | "12" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| text | "hello" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| empty string | "" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| boolean | true | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| false | false | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| empty array | [] | false |
| numeric array | [1,2,3] | false |
| mixed array | [1,null,"x",3] | false |
| nested array | [[1,2],[3]] | false |
| empty object | {} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| object | {"x":1} | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $setEquals arguments must resolve to arrays. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$setEquals":[]} | Error: IllegalArgumentException — $setEquals requires at least two arrays. |
| {"$setEquals":{"unexpected":1}} | Error: IllegalArgumentException — $setEquals requires at least two arrays. |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setEquals.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **9 exact BSON matches**, **32 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/setEquals.json).

<!-- END MONGO PARITY -->

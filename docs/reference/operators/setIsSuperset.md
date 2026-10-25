# $setIsSuperset

Tests whether the first set contains the second.

**Category:** Sets. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `array` | ARRAY | Yes | Expression evaluated against the input |
| `other` | ARRAY | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **BOOLEAN**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$setIsSuperset": [
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
| null | null | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| missing | Field absent | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| zero | 0 | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| negative | -2 | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| decimal | 2.5 | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| numeric string | "12" | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| text | "hello" | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| empty string | "" | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| boolean | true | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| false | false | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| empty array | [] | false |
| numeric array | [1,2,3] | true |
| mixed array | [1,null,"x",3] | false |
| nested array | [[1,2],[3]] | false |
| empty object | {} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| object | {"x":1} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $setIsSuperset expects array operands |

### Argument: `other[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| missing | Field absent | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| zero | 0 | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| negative | -2 | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| decimal | 2.5 | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| numeric string | "12" | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| text | "hello" | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| empty string | "" | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| boolean | true | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| false | false | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| empty array | [] | true |
| numeric array | [1,2,3] | false |
| mixed array | [1,null,"x",3] | false |
| nested array | [[1,2],[3]] | false |
| empty object | {} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| object | {"x":1} | Error: IllegalArgumentException — $setIsSuperset expects array operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $setIsSuperset expects array operands |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$setIsSuperset":[]} | Error: IllegalArgumentException — $setIsSuperset requires exactly two arrays. |
| {"$setIsSuperset":{"unexpected":1}} | Error: IllegalArgumentException — $setIsSuperset requires exactly two arrays. |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setIsSuperset.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

# $nin

Negates array membership.

**Category:** Comparison. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `value` | ANY | Yes | Expression evaluated against the input |
| `array` | ARRAY | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **BOOLEAN**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$nin": [
    2,
    [
      1,
      2
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

### Argument: `value[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | true |
| missing | Field absent | true |
| zero | 0 | true |
| negative | -2 | true |
| decimal | 2.5 | true |
| numeric string | "12" | true |
| text | "hello" | true |
| empty string | "" | true |
| boolean | true | true |
| false | false | true |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | true |
| decimal128 | {"$numberDecimal":"1.25"} | true |
| empty array | [] | true |
| numeric array | [1,2,3] | true |
| mixed array | [1,null,"x",3] | true |
| nested array | [[1,2],[3]] | true |
| empty object | {} | true |
| object | {"x":1} | true |
| ISO date string | "2026-01-15T15:00:00Z" | true |

### Argument: `array[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| missing | Field absent | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| zero | 0 | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| negative | -2 | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| decimal | 2.5 | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| numeric string | "12" | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| text | "hello" | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| empty string | "" | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| boolean | true | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| false | false | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| empty array | [] | true |
| numeric array | [1,2,3] | false |
| mixed array | [1,null,"x",3] | true |
| nested array | [[1,2],[3]] | true |
| empty object | {} | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| object | {"x":1} | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $in requires the second argument to evaluate to an array |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$nin":[]} | Error: IllegalArgumentException — $in expects [searchExpr, candidates] |
| {"$nin":{"unexpected":1}} | Error: IllegalArgumentException — $in expects [searchExpr, candidates] |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/nin.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

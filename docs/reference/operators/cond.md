# $cond

Evaluates Mongo truthiness and lazily returns the selected branch.

**Category:** Conditional. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `if` | ANY | Yes | Expression evaluated against the input |
| `then` | ANY | Yes | Expression evaluated against the input |
| `else` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 3; maximum 3.

Declared result types: **ANY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$cond": [
    true,
    "yes",
    "no"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "yes".

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `if[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | "no" |
| missing | Field absent | "no" |
| zero | 0 | "no" |
| negative | -2 | "yes" |
| decimal | 2.5 | "yes" |
| numeric string | "12" | "yes" |
| text | "hello" | "yes" |
| empty string | "" | "yes" |
| boolean | true | "yes" |
| false | false | "no" |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "yes" |
| decimal128 | {"$numberDecimal":"1.25"} | "yes" |
| empty array | [] | "yes" |
| numeric array | [1,2,3] | "yes" |
| mixed array | [1,null,"x",3] | "yes" |
| nested array | [[1,2],[3]] | "yes" |
| empty object | {} | "yes" |
| object | {"x":1} | "yes" |
| ISO date string | "2026-01-15T15:00:00Z" | "yes" |

### Argument: `then[1]`

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

### Argument: `else[2]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | "yes" |
| missing | Field absent | "yes" |
| zero | 0 | "yes" |
| negative | -2 | "yes" |
| decimal | 2.5 | "yes" |
| numeric string | "12" | "yes" |
| text | "hello" | "yes" |
| empty string | "" | "yes" |
| boolean | true | "yes" |
| false | false | "yes" |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "yes" |
| decimal128 | {"$numberDecimal":"1.25"} | "yes" |
| empty array | [] | "yes" |
| numeric array | [1,2,3] | "yes" |
| mixed array | [1,null,"x",3] | "yes" |
| nested array | [[1,2],[3]] | "yes" |
| empty object | {} | "yes" |
| object | {"x":1} | "yes" |
| ISO date string | "2026-01-15T15:00:00Z" | "yes" |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$cond":[]} | Error: IllegalArgumentException — $cond requires {if, then, else} or an array of three arguments |
| {"$cond":{"unexpected":1}} | Error: IllegalArgumentException — $cond requires exactly if, then and else |

## Additional boundary examples

<details>
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$cond": [
    1,
    "yes",
    {
      "$divide": [
        1,
        0
      ]
    }
  ]
}
```

Input:
```json
{}
```

**SrotaX:** "yes".

</details>

## Scope and reproducibility

This page records **61 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/cond.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **57 exact BSON matches**, **2 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| then[1] / missing | null | Missing (field omitted) |
| all / boundary example | "yes" | Error: BadValue — Failed to optimize pipeline :: caused by :: can't $divide by zero |

[Download full comparison evidence](../../downloads/operator-parity/cond.json).

<!-- END MONGO PARITY -->

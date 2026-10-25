# $max

Returns the maximum non-null value from one array expression or explicit operands.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `value` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum variadic.

Declared result types: **NUMBER**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

A single array-valued expression is also supported, for example `{"$max": "$items"}`. With multiple operands, array arguments are not recursively flattened.

## Example

Expression:
```json
{
  "$max": [
    2,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `value[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 3 (int32) |
| missing | Field absent | 3 (int32) |
| zero | 0 | 3 (int32) |
| negative | -2 | 3 (int32) |
| decimal | 2.5 | 3 (int32) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | true |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 3 (int32) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |

### Argument: `value[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 2 (int32) |
| missing | Field absent | 2 (int32) |
| zero | 0 | 2 (int32) |
| negative | -2 | 2 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | true |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 2 (int32) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |

### Argument: `single array expression`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| single operand null | null | null |
| single operand missing | Field absent | null |
| single operand zero | 0 | 0 (int32) |
| single operand negative | -2 | -2 (int32) |
| single operand decimal | 2.5 | 2.5 (double) |
| single operand numeric string | "12" | "12" |
| single operand text | "hello" | "hello" |
| single operand empty string | "" | "" |
| single operand boolean | true | true |
| single operand false | false | false |
| single operand typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| single operand decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| single operand empty array | [] | null |
| single operand numeric array | [1,2,3] | 3 (int32) |
| single operand mixed array | [1,null,"x",3] | "x" |
| single operand nested array | [[1,2],[3]] | [3] |
| single operand empty object | {} | {} |
| single operand object | {"x":1} | {"x":1} |
| single operand ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$max":[]} | null |
| {"$max":{"unexpected":1}} | {"unexpected":1} |

## Scope and reproducibility

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/max.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **60 exact BSON matches**, **0 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/max.json).

<!-- END MONGO PARITY -->

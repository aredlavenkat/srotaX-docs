# $sum

Sums numeric values from one array expression or explicit operands; ignores nonnumeric values.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `number` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 0; maximum variadic.

Declared result types: **DOUBLE**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

A single array-valued expression is also supported, for example `{"$sum": "$items"}`. With multiple operands, array arguments are not recursively flattened.

## Example

Expression:
```json
{
  "$sum": [
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
| null | null | 3.0 (double) |
| missing | Field absent | 3.0 (double) |
| zero | 0 | 3.0 (double) |
| negative | -2 | 1.0 (double) |
| decimal | 2.5 | 5.5 (double) |
| numeric string | "12" | 3.0 (double) |
| text | "hello" | 3.0 (double) |
| empty string | "" | 3.0 (double) |
| boolean | true | 3.0 (double) |
| false | false | 3.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 3.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 4.25 (double) |
| empty array | [] | 3.0 (double) |
| numeric array | [1,2,3] | 3.0 (double) |
| mixed array | [1,null,"x",3] | 3.0 (double) |
| nested array | [[1,2],[3]] | 3.0 (double) |
| empty object | {} | 3.0 (double) |
| object | {"x":1} | 3.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 3.0 (double) |

### Argument: `number[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 2.0 (double) |
| missing | Field absent | 2.0 (double) |
| zero | 0 | 2.0 (double) |
| negative | -2 | 0.0 (double) |
| decimal | 2.5 | 4.5 (double) |
| numeric string | "12" | 2.0 (double) |
| text | "hello" | 2.0 (double) |
| empty string | "" | 2.0 (double) |
| boolean | true | 2.0 (double) |
| false | false | 2.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 2.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 3.25 (double) |
| empty array | [] | 2.0 (double) |
| numeric array | [1,2,3] | 2.0 (double) |
| mixed array | [1,null,"x",3] | 2.0 (double) |
| nested array | [[1,2],[3]] | 2.0 (double) |
| empty object | {} | 2.0 (double) |
| object | {"x":1} | 2.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 2.0 (double) |

### Argument: `single array expression`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| single operand null | null | 0.0 (double) |
| single operand missing | Field absent | 0.0 (double) |
| single operand zero | 0 | 0.0 (double) |
| single operand negative | -2 | -2.0 (double) |
| single operand decimal | 2.5 | 2.5 (double) |
| single operand numeric string | "12" | 0.0 (double) |
| single operand text | "hello" | 0.0 (double) |
| single operand empty string | "" | 0.0 (double) |
| single operand boolean | true | 0.0 (double) |
| single operand false | false | 0.0 (double) |
| single operand typed date | {"$date":"2026-01-15T15:00:00Z"} | 0.0 (double) |
| single operand decimal128 | {"$numberDecimal":"1.25"} | 1.25 (double) |
| single operand empty array | [] | 0.0 (double) |
| single operand numeric array | [1,2,3] | 6.0 (double) |
| single operand mixed array | [1,null,"x",3] | 4.0 (double) |
| single operand nested array | [[1,2],[3]] | 0.0 (double) |
| single operand empty object | {} | 0.0 (double) |
| single operand object | {"x":1} | 0.0 (double) |
| single operand ISO date string | "2026-01-15T15:00:00Z" | 0.0 (double) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$sum":[]} | 0.0 (double) |
| {"$sum":{"unexpected":1}} | 0.0 (double) |

## Scope and reproducibility

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/sum.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **0 both rejected**, **57 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 5.0 (double) | 5 (int32) |
| number[0] / null | 3.0 (double) | 3 (int32) |
| number[0] / missing | 3.0 (double) | 3 (int32) |
| number[0] / zero | 3.0 (double) | 3 (int32) |
| number[0] / negative | 1.0 (double) | 1 (int32) |
| number[0] / numeric string | 3.0 (double) | 3 (int32) |
| number[0] / text | 3.0 (double) | 3 (int32) |
| number[0] / empty string | 3.0 (double) | 3 (int32) |
| number[0] / boolean | 3.0 (double) | 3 (int32) |
| number[0] / false | 3.0 (double) | 3 (int32) |
| number[0] / typed date | 3.0 (double) | 3 (int32) |
| number[0] / decimal128 | 4.25 (double) | 4.25 (decimal128) |
| number[0] / empty array | 3.0 (double) | 3 (int32) |
| number[0] / numeric array | 3.0 (double) | 3 (int32) |
| number[0] / mixed array | 3.0 (double) | 3 (int32) |
| number[0] / nested array | 3.0 (double) | 3 (int32) |
| number[0] / empty object | 3.0 (double) | 3 (int32) |
| number[0] / object | 3.0 (double) | 3 (int32) |
| number[0] / ISO date string | 3.0 (double) | 3 (int32) |
| number[1] / null | 2.0 (double) | 2 (int32) |
| number[1] / missing | 2.0 (double) | 2 (int32) |
| number[1] / zero | 2.0 (double) | 2 (int32) |
| number[1] / negative | 0.0 (double) | 0 (int32) |
| number[1] / numeric string | 2.0 (double) | 2 (int32) |
| number[1] / text | 2.0 (double) | 2 (int32) |
| number[1] / empty string | 2.0 (double) | 2 (int32) |
| number[1] / boolean | 2.0 (double) | 2 (int32) |
| number[1] / false | 2.0 (double) | 2 (int32) |
| number[1] / typed date | 2.0 (double) | 2 (int32) |
| number[1] / decimal128 | 3.25 (double) | 3.25 (decimal128) |
| number[1] / empty array | 2.0 (double) | 2 (int32) |
| number[1] / numeric array | 2.0 (double) | 2 (int32) |
| number[1] / mixed array | 2.0 (double) | 2 (int32) |
| number[1] / nested array | 2.0 (double) | 2 (int32) |
| number[1] / empty object | 2.0 (double) | 2 (int32) |
| number[1] / object | 2.0 (double) | 2 (int32) |
| number[1] / ISO date string | 2.0 (double) | 2 (int32) |
| single array expression / single operand null | 0.0 (double) | 0 (int32) |
| single array expression / single operand missing | 0.0 (double) | 0 (int32) |
| single array expression / single operand zero | 0.0 (double) | 0 (int32) |
| single array expression / single operand negative | -2.0 (double) | -2 (int32) |
| single array expression / single operand numeric string | 0.0 (double) | 0 (int32) |
| single array expression / single operand text | 0.0 (double) | 0 (int32) |
| single array expression / single operand empty string | 0.0 (double) | 0 (int32) |
| single array expression / single operand boolean | 0.0 (double) | 0 (int32) |
| single array expression / single operand false | 0.0 (double) | 0 (int32) |
| single array expression / single operand typed date | 0.0 (double) | 0 (int32) |
| single array expression / single operand decimal128 | 1.25 (double) | 1.25 (decimal128) |
| single array expression / single operand empty array | 0.0 (double) | 0 (int32) |
| single array expression / single operand numeric array | 6.0 (double) | 6 (int32) |
| single array expression / single operand mixed array | 4.0 (double) | 4 (int32) |
| single array expression / single operand nested array | 0.0 (double) | 0 (int32) |
| single array expression / single operand empty object | 0.0 (double) | 0 (int32) |
| single array expression / single operand object | 0.0 (double) | 0 (int32) |
| single array expression / single operand ISO date string | 0.0 (double) | 0 (int32) |
| all / empty arguments | 0.0 (double) | 0 (int32) |
| all / unknown option | 0.0 (double) | 0 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/sum.json).

<!-- END MONGO PARITY -->

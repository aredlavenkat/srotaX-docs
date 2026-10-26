# $avg

## Definition

Averages numeric values from one array expression or explicit operands; ignores nonnumeric values.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$avg": [ <number>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | See argument count below | Numeric expression. Repeat the argument when the syntax accepts multiple operands. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

A single array-valued expression is also supported, for example `{"$avg": "$items"}`. With multiple operands, array arguments are not recursively flattened.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `number` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | 4.0 (double) |
| missing | Field absent | 4.0 (double) |
| decimal | 2.5 | 3.25 (double) |
| numeric string | "12" | 4.0 (double) |
| text | "hello" | 4.0 (double) |
| boolean | true | 4.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 4.0 (double) |
| empty array | [] | 4.0 (double) |
| numeric array | [1,2,3] | 4.0 (double) |
| object | {"x":1} | 4.0 (double) |
| null | null | 2.0 (double) |
| missing | Field absent | 2.0 (double) |
| decimal | 2.5 | 2.25 (double) |
| numeric string | "12" | 2.0 (double) |
| text | "hello" | 2.0 (double) |
| boolean | true | 2.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 2.0 (double) |
| empty array | [] | 2.0 (double) |
| numeric array | [1,2,3] | 2.0 (double) |
| object | {"x":1} | 2.0 (double) |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$avg":[]} | null |
| {"$avg":{"unexpected":1}} | null |

## Examples

Expression:
```json
{
  "$avg": [
    2,
    4
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 3.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `number[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 4.0 (double) |
| missing | Field absent | 4.0 (double) |
| zero | 0 | 2.0 (double) |
| negative | -2 | 1.0 (double) |
| decimal | 2.5 | 3.25 (double) |
| numeric string | "12" | 4.0 (double) |
| text | "hello" | 4.0 (double) |
| empty string | "" | 4.0 (double) |
| boolean | true | 4.0 (double) |
| false | false | 4.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 4.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 2.625 (double) |
| empty array | [] | 4.0 (double) |
| numeric array | [1,2,3] | 4.0 (double) |
| mixed array | [1,null,"x",3] | 4.0 (double) |
| nested array | [[1,2],[3]] | 4.0 (double) |
| empty object | {} | 4.0 (double) |
| object | {"x":1} | 4.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 4.0 (double) |

**Argument: `number[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 2.0 (double) |
| missing | Field absent | 2.0 (double) |
| zero | 0 | 1.0 (double) |
| negative | -2 | 0.0 (double) |
| decimal | 2.5 | 2.25 (double) |
| numeric string | "12" | 2.0 (double) |
| text | "hello" | 2.0 (double) |
| empty string | "" | 2.0 (double) |
| boolean | true | 2.0 (double) |
| false | false | 2.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 2.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.625 (double) |
| empty array | [] | 2.0 (double) |
| numeric array | [1,2,3] | 2.0 (double) |
| mixed array | [1,null,"x",3] | 2.0 (double) |
| nested array | [[1,2],[3]] | 2.0 (double) |
| empty object | {} | 2.0 (double) |
| object | {"x":1} | 2.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 2.0 (double) |

**Argument: `single array expression`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| single operand null | null | null |
| single operand missing | Field absent | null |
| single operand zero | 0 | 0.0 (double) |
| single operand negative | -2 | -2.0 (double) |
| single operand decimal | 2.5 | 2.5 (double) |
| single operand numeric string | "12" | null |
| single operand text | "hello" | null |
| single operand empty string | "" | null |
| single operand boolean | true | null |
| single operand false | false | null |
| single operand typed date | {"$date":"2026-01-15T15:00:00Z"} | null |
| single operand decimal128 | {"$numberDecimal":"1.25"} | 1.25 (double) |
| single operand empty array | [] | null |
| single operand numeric array | [1,2,3] | 2.0 (double) |
| single operand mixed array | [1,null,"x",3] | 2.0 (double) |
| single operand nested array | [[1,2],[3]] | null |
| single operand empty object | {} | null |
| single operand object | {"x":1} | null |
| single operand ISO date string | "2026-01-15T15:00:00Z" | null |


</details>

## Verification

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/avg.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **57 exact BSON matches**, **0 both rejected**, **3 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| number[0] / decimal128 | 2.625 (double) | 2.625 (decimal128) |
| number[1] / decimal128 | 1.625 (double) | 1.625 (decimal128) |
| single array expression / single operand decimal128 | 1.25 (double) | 1.25 (decimal128) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/avg.json).

<!-- END MONGO PARITY -->

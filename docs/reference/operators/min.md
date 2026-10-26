# $min

## Definition

Returns the minimum non-null value from one array expression or explicit operands.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$min": [ <value>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | See argument count below | Expression supplying the value to evaluate. |

Arguments are positional: keep the order shown. Supply 1 or more arguments.

A single array-valued expression is also supported, for example `{"$min": "$items"}`. With multiple operands, array arguments are not recursively flattened.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `value` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | 3 (int32) |
| missing | Field absent | 3 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | 3 (int32) |
| text | "hello" | 3 (int32) |
| boolean | true | 3 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 3 (int32) |
| empty array | [] | 3 (int32) |
| numeric array | [1,2,3] | 3 (int32) |
| object | {"x":1} | 3 (int32) |
| null | null | 2 (int32) |
| missing | Field absent | 2 (int32) |
| decimal | 2.5 | 2 (int32) |
| numeric string | "12" | 2 (int32) |
| text | "hello" | 2 (int32) |
| boolean | true | 2 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 2 (int32) |
| empty array | [] | 2 (int32) |
| numeric array | [1,2,3] | 2 (int32) |
| object | {"x":1} | 2 (int32) |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$min":[]} | null |
| {"$min":{"unexpected":1}} | {"unexpected":1} |

## Examples

Expression:
```json
{
  "$min": [
    2,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `value[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 3 (int32) |
| missing | Field absent | 3 (int32) |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | 3 (int32) |
| text | "hello" | 3 (int32) |
| empty string | "" | 3 (int32) |
| boolean | true | 3 (int32) |
| false | false | 3 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 3 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| empty array | [] | 3 (int32) |
| numeric array | [1,2,3] | 3 (int32) |
| mixed array | [1,null,"x",3] | 3 (int32) |
| nested array | [[1,2],[3]] | 3 (int32) |
| empty object | {} | 3 (int32) |
| object | {"x":1} | 3 (int32) |
| ISO date string | "2026-01-15T15:00:00Z" | 3 (int32) |

**Argument: `value[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 2 (int32) |
| missing | Field absent | 2 (int32) |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2 (int32) |
| numeric string | "12" | 2 (int32) |
| text | "hello" | 2 (int32) |
| empty string | "" | 2 (int32) |
| boolean | true | 2 (int32) |
| false | false | 2 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 2 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| empty array | [] | 2 (int32) |
| numeric array | [1,2,3] | 2 (int32) |
| mixed array | [1,null,"x",3] | 2 (int32) |
| nested array | [[1,2],[3]] | 2 (int32) |
| empty object | {} | 2 (int32) |
| object | {"x":1} | 2 (int32) |
| ISO date string | "2026-01-15T15:00:00Z" | 2 (int32) |

**Argument: `single array expression`**

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
| single operand numeric array | [1,2,3] | 1 (int32) |
| single operand mixed array | [1,null,"x",3] | 1 (int32) |
| single operand nested array | [[1,2],[3]] | [1,2] |
| single operand empty object | {} | {} |
| single operand object | {"x":1} | {"x":1} |
| single operand ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |


</details>

## Verification

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/min.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **60 exact BSON matches**, **0 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/min.json).

<!-- END MONGO PARITY -->

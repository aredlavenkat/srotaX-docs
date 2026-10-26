# $concat

## Definition

Concatenates strings, skipping null operands.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$concat": [ <text>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | See argument count below | Expression supplying the text value. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `text` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $concat supports only string operands |
| numeric string | "12" | "12b" |
| text | "hello" | "hellob" |
| boolean | true | Error — $concat supports only string operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concat supports only string operands |
| empty array | [] | Error — $concat supports only string operands |
| numeric array | [1,2,3] | Error — $concat supports only string operands |
| object | {"x":1} | Error — $concat supports only string operands |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $concat supports only string operands |
| numeric string | "12" | "a12" |
| text | "hello" | "ahello" |
| boolean | true | Error — $concat supports only string operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concat supports only string operands |
| empty array | [] | Error — $concat supports only string operands |
| numeric array | [1,2,3] | Error — $concat supports only string operands |
| object | {"x":1} | Error — $concat supports only string operands |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$concat":[]} | "" |
| {"$concat":{"unexpected":1}} | Error — $concat expects an array of expressions |

## Examples

Expression:
```json
{
  "$concat": [
    "a",
    "b"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "ab".

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `text[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $concat supports only string operands |
| negative | -2 | Error — $concat supports only string operands |
| decimal | 2.5 | Error — $concat supports only string operands |
| numeric string | "12" | "12b" |
| text | "hello" | "hellob" |
| empty string | "" | "b" |
| boolean | true | Error — $concat supports only string operands |
| false | false | Error — $concat supports only string operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concat supports only string operands |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $concat supports only string operands |
| empty array | [] | Error — $concat supports only string operands |
| numeric array | [1,2,3] | Error — $concat supports only string operands |
| mixed array | [1,null,"x",3] | Error — $concat supports only string operands |
| nested array | [[1,2],[3]] | Error — $concat supports only string operands |
| empty object | {} | Error — $concat supports only string operands |
| object | {"x":1} | Error — $concat supports only string operands |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Zb" |

**Argument: `text[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $concat supports only string operands |
| negative | -2 | Error — $concat supports only string operands |
| decimal | 2.5 | Error — $concat supports only string operands |
| numeric string | "12" | "a12" |
| text | "hello" | "ahello" |
| empty string | "" | "a" |
| boolean | true | Error — $concat supports only string operands |
| false | false | Error — $concat supports only string operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concat supports only string operands |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $concat supports only string operands |
| empty array | [] | Error — $concat supports only string operands |
| numeric array | [1,2,3] | Error — $concat supports only string operands |
| mixed array | [1,null,"x",3] | Error — $concat supports only string operands |
| nested array | [[1,2],[3]] | Error — $concat supports only string operands |
| empty object | {} | Error — $concat supports only string operands |
| object | {"x":1} | Error — $concat supports only string operands |
| ISO date string | "2026-01-15T15:00:00Z" | "a2026-01-15T15:00:00Z" |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/concat.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **14 exact BSON matches**, **27 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/concat.json).

<!-- END MONGO PARITY -->

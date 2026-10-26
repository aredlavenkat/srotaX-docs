# $round

## Definition

Rounds a number to the specified decimal place using ties-to-even rounding (HALF_EVEN); the place defaults to zero.

**Expression operator** · Arithmetic · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$round": [ <number>, <place> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Numeric expression. Repeat the argument when the syntax accepts multiple operands. |
| `place` | No | Decimal position for rounding or truncation. Defaults to `0`; negative positions act to the left of the decimal point. |

Arguments are positional: keep the order shown. The authoring signature accepts 1–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `number` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | 2.0 (double) |
| numeric string | "12" | Error — Number and integer precision required |
| text | "hello" | Error — Number and integer precision required |
| boolean | true | Error — Number and integer precision required |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Number and integer precision required |
| empty array | [] | Error — Number and integer precision required |
| numeric array | [1,2,3] | Error — Number and integer precision required |
| object | {"x":1} | Error — Number and integer precision required |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$round":[]} | Error — $round requires [number, place?] |
| {"$round":{"unexpected":1}} | Error — Number and integer precision required |

## Examples

Expression:
```json
{
  "$round": [
    2.5
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `number[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.0 (double) |
| numeric string | "12" | Error — Number and integer precision required |
| text | "hello" | Error — Number and integer precision required |
| empty string | "" | Error — Number and integer precision required |
| boolean | true | Error — Number and integer precision required |
| false | false | Error — Number and integer precision required |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Number and integer precision required |
| decimal128 | {"$numberDecimal":"1.25"} | 1.0 (double) |
| empty array | [] | Error — Number and integer precision required |
| numeric array | [1,2,3] | Error — Number and integer precision required |
| mixed array | [1,null,"x",3] | Error — Number and integer precision required |
| nested array | [[1,2],[3]] | Error — Number and integer precision required |
| empty object | {} | Error — Number and integer precision required |
| object | {"x":1} | Error — Number and integer precision required |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Number and integer precision required |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 2 tested examples</summary>

Expression:
```json
{
  "$round": [
    2.345,
    2
  ]
}
```

Input:
```json
{}
```

**SrotaX:** 2.34 (double).

Expression:
```json
{
  "$round": [
    2.5,
    0
  ]
}
```

Input:
```json
{}
```

**SrotaX:** 2.0 (double).

</details>

## Verification

This page records **24 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/round.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **15 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| number[0] / decimal128 | 1.0 (double) | 1 (decimal128) |
| all / boundary example | 2.34 (double) | 2.35 (double) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/round.json).

<!-- END MONGO PARITY -->

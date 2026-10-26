# $gte

## Definition

Tests whether the first value is greater or equal.

**Expression operator** · Comparison · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$gte": [ <left>, <right> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `left` | Yes | First expression in the ordered argument list. |
| `right` | Yes | Second expression in the ordered argument list. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `left` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| decimal | 2.5 | false |
| numeric string | "12" | true |
| text | "hello" | true |
| boolean | true | true |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | true |
| empty array | [] | true |
| numeric array | [1,2,3] | true |
| object | {"x":1} | true |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$gte":[]} | Error — $gte requires two arguments |
| {"$gte":{"unexpected":1}} | Error — $gte requires two arguments |

## Examples

Expression:
```json
{
  "$gte": [
    2,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** false.

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `left[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| zero | 0 | false |
| negative | -2 | false |
| decimal | 2.5 | false |
| numeric string | "12" | true |
| text | "hello" | true |
| empty string | "" | true |
| boolean | true | true |
| false | false | true |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | true |
| decimal128 | {"$numberDecimal":"1.25"} | false |
| empty array | [] | true |
| numeric array | [1,2,3] | true |
| mixed array | [1,null,"x",3] | true |
| nested array | [[1,2],[3]] | true |
| empty object | {} | true |
| object | {"x":1} | true |
| ISO date string | "2026-01-15T15:00:00Z" | true |

**Argument: `right[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | true |
| missing | Field absent | true |
| zero | 0 | true |
| negative | -2 | true |
| decimal | 2.5 | false |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | false |
| boolean | true | false |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | false |
| decimal128 | {"$numberDecimal":"1.25"} | true |
| empty array | [] | false |
| numeric array | [1,2,3] | false |
| mixed array | [1,null,"x",3] | false |
| nested array | [[1,2],[3]] | false |
| empty object | {} | false |
| object | {"x":1} | false |
| ISO date string | "2026-01-15T15:00:00Z" | false |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/gte.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **39 exact BSON matches**, **2 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/gte.json).

<!-- END MONGO PARITY -->

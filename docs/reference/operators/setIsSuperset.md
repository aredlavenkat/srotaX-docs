# $setIsSuperset

## Definition

Tests whether the first set contains the second.

**Expression operator** · Sets · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$setIsSuperset": [ <array>, <other> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | Expression supplying the source array. |
| `other` | Yes | Expression supplying the other array for the set operation. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `array` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $setIsSuperset expects array operands |
| missing | Field absent | Error — $setIsSuperset expects array operands |
| decimal | 2.5 | Error — $setIsSuperset expects array operands |
| numeric string | "12" | Error — $setIsSuperset expects array operands |
| text | "hello" | Error — $setIsSuperset expects array operands |
| boolean | true | Error — $setIsSuperset expects array operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setIsSuperset expects array operands |
| empty array | [] | false |
| numeric array | [1,2,3] | true |
| object | {"x":1} | Error — $setIsSuperset expects array operands |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$setIsSuperset":[]} | Error — $setIsSuperset requires exactly two arrays. |
| {"$setIsSuperset":{"unexpected":1}} | Error — $setIsSuperset requires exactly two arrays. |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `array[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $setIsSuperset expects array operands |
| missing | Field absent | Error — $setIsSuperset expects array operands |
| zero | 0 | Error — $setIsSuperset expects array operands |
| negative | -2 | Error — $setIsSuperset expects array operands |
| decimal | 2.5 | Error — $setIsSuperset expects array operands |
| numeric string | "12" | Error — $setIsSuperset expects array operands |
| text | "hello" | Error — $setIsSuperset expects array operands |
| empty string | "" | Error — $setIsSuperset expects array operands |
| boolean | true | Error — $setIsSuperset expects array operands |
| false | false | Error — $setIsSuperset expects array operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setIsSuperset expects array operands |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setIsSuperset expects array operands |
| empty array | [] | false |
| numeric array | [1,2,3] | true |
| mixed array | [1,null,"x",3] | false |
| nested array | [[1,2],[3]] | false |
| empty object | {} | Error — $setIsSuperset expects array operands |
| object | {"x":1} | Error — $setIsSuperset expects array operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $setIsSuperset expects array operands |

**Argument: `other[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $setIsSuperset expects array operands |
| missing | Field absent | Error — $setIsSuperset expects array operands |
| zero | 0 | Error — $setIsSuperset expects array operands |
| negative | -2 | Error — $setIsSuperset expects array operands |
| decimal | 2.5 | Error — $setIsSuperset expects array operands |
| numeric string | "12" | Error — $setIsSuperset expects array operands |
| text | "hello" | Error — $setIsSuperset expects array operands |
| empty string | "" | Error — $setIsSuperset expects array operands |
| boolean | true | Error — $setIsSuperset expects array operands |
| false | false | Error — $setIsSuperset expects array operands |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setIsSuperset expects array operands |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setIsSuperset expects array operands |
| empty array | [] | true |
| numeric array | [1,2,3] | false |
| mixed array | [1,null,"x",3] | false |
| nested array | [[1,2],[3]] | false |
| empty object | {} | Error — $setIsSuperset expects array operands |
| object | {"x":1} | Error — $setIsSuperset expects array operands |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $setIsSuperset expects array operands |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setIsSuperset.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

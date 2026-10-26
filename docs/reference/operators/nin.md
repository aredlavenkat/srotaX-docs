# $nin

## Definition

Negates array membership.

**Expression operator** · Comparison · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$nin": [ <value>, <array> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | Expression supplying the value to evaluate. |
| `array` | Yes | Expression supplying the source array. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `value` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | true |
| missing | Field absent | true |
| decimal | 2.5 | true |
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
| {"$nin":[]} | Error — $in expects [searchExpr, candidates] |
| {"$nin":{"unexpected":1}} | Error — $in expects [searchExpr, candidates] |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `value[0]`**

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

**Argument: `array[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $in requires the second argument to evaluate to an array |
| missing | Field absent | Error — $in requires the second argument to evaluate to an array |
| zero | 0 | Error — $in requires the second argument to evaluate to an array |
| negative | -2 | Error — $in requires the second argument to evaluate to an array |
| decimal | 2.5 | Error — $in requires the second argument to evaluate to an array |
| numeric string | "12" | Error — $in requires the second argument to evaluate to an array |
| text | "hello" | Error — $in requires the second argument to evaluate to an array |
| empty string | "" | Error — $in requires the second argument to evaluate to an array |
| boolean | true | Error — $in requires the second argument to evaluate to an array |
| false | false | Error — $in requires the second argument to evaluate to an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $in requires the second argument to evaluate to an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $in requires the second argument to evaluate to an array |
| empty array | [] | true |
| numeric array | [1,2,3] | false |
| mixed array | [1,null,"x",3] | true |
| nested array | [[1,2],[3]] | true |
| empty object | {} | Error — $in requires the second argument to evaluate to an array |
| object | {"x":1} | Error — $in requires the second argument to evaluate to an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $in requires the second argument to evaluate to an array |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/nin.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

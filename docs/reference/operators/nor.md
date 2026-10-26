# $nor

## Definition

Negates a disjunction.

**Expression operator** · Logic · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$nor": [ <expression>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `expression` | See argument count below | Expression to evaluate as a condition. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `expression` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | true |
| missing | Field absent | true |
| decimal | 2.5 | true |
| numeric string | "12" | true |
| text | "hello" | true |
| boolean | true | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | true |
| empty array | [] | true |
| numeric array | [1,2,3] | true |
| object | {"x":1} | true |
| null | null | false |
| missing | Field absent | false |
| decimal | 2.5 | false |
| numeric string | "12" | false |
| text | "hello" | false |
| boolean | true | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | false |
| empty array | [] | false |
| numeric array | [1,2,3] | false |
| object | {"x":1} | false |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$nor":[]} | true |
| {"$nor":{"unexpected":1}} | Error — class org.bson.Document cannot be cast to class java.util.List (org.bson.Document is in unnamed module of loader 'app'; java.util.List is in module java.base of loader 'bootstrap') |

## Examples

Expression:
```json
{
  "$nor": [
    true,
    false
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

**Argument: `expression[0]`**

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
| boolean | true | false |
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

**Argument: `expression[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| zero | 0 | false |
| negative | -2 | false |
| decimal | 2.5 | false |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | false |
| boolean | true | false |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | false |
| decimal128 | {"$numberDecimal":"1.25"} | false |
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

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/nor.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

# $coalesce

## Definition

Returns the first non-null expression.

**Expression operator** · Conditional · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$coalesce": [ <value>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | See argument count below | Expression supplying the value to evaluate. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `value` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | "x" |
| missing | Field absent | "x" |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| boolean | true | true |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| object | {"x":1} | {"x":1} |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| boolean | true | true |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| object | {"x":1} | {"x":1} |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$coalesce":[]} | null |
| {"$coalesce":{"unexpected":1}} | Error — $coalesce expects an array of expressions |

## Examples

Expression:
```json
{
  "$coalesce": [
    null,
    "x"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "x".

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `value[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | "x" |
| missing | Field absent | "x" |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | true |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |

**Argument: `value[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | true |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/coalesce.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

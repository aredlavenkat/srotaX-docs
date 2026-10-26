# $indexOfArray

## Definition

Finds an item using Java equality.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$indexOfArray": [ <array>, <search>, <start>, <end> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | Expression supplying the source array. |
| `search` | Yes | Value or substring to find in the source. |
| `start` | No | Starting position or lower bound. See the syntax and examples for this operator. |
| `end` | No | Exclusive ending position or upper bound. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–4 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `array` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $indexOfArray first argument must be an array |
| numeric string | "12" | Error — $indexOfArray first argument must be an array |
| text | "hello" | Error — $indexOfArray first argument must be an array |
| boolean | true | Error — $indexOfArray first argument must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $indexOfArray first argument must be an array |
| empty array | [] | -1 (int32) |
| numeric array | [1,2,3] | 1 (int32) |
| object | {"x":1} | Error — $indexOfArray first argument must be an array |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$indexOfArray":[]} | Error — $indexOfArray expects 2 to 4 arguments: [array, search, start?, end?] |
| {"$indexOfArray":{"unexpected":1}} | Error — $indexOfArray expects 2 to 4 arguments: [array, search, start?, end?] |

## Examples

Expression:
```json
{
  "$indexOfArray": [
    [
      1,
      2
    ],
    2
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 1 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `array[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $indexOfArray first argument must be an array |
| negative | -2 | Error — $indexOfArray first argument must be an array |
| decimal | 2.5 | Error — $indexOfArray first argument must be an array |
| numeric string | "12" | Error — $indexOfArray first argument must be an array |
| text | "hello" | Error — $indexOfArray first argument must be an array |
| empty string | "" | Error — $indexOfArray first argument must be an array |
| boolean | true | Error — $indexOfArray first argument must be an array |
| false | false | Error — $indexOfArray first argument must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $indexOfArray first argument must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $indexOfArray first argument must be an array |
| empty array | [] | -1 (int32) |
| numeric array | [1,2,3] | 1 (int32) |
| mixed array | [1,null,"x",3] | -1 (int32) |
| nested array | [[1,2],[3]] | -1 (int32) |
| empty object | {} | Error — $indexOfArray first argument must be an array |
| object | {"x":1} | Error — $indexOfArray first argument must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $indexOfArray first argument must be an array |

**Argument: `search[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | -1 (int32) |
| missing | Field absent | -1 (int32) |
| zero | 0 | -1 (int32) |
| negative | -2 | -1 (int32) |
| decimal | 2.5 | -1 (int32) |
| numeric string | "12" | -1 (int32) |
| text | "hello" | -1 (int32) |
| empty string | "" | -1 (int32) |
| boolean | true | -1 (int32) |
| false | false | -1 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | -1 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | -1 (int32) |
| empty array | [] | -1 (int32) |
| numeric array | [1,2,3] | -1 (int32) |
| mixed array | [1,null,"x",3] | -1 (int32) |
| nested array | [[1,2],[3]] | -1 (int32) |
| empty object | {} | -1 (int32) |
| object | {"x":1} | -1 (int32) |
| ISO date string | "2026-01-15T15:00:00Z" | -1 (int32) |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/indexOfArray.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **26 exact BSON matches**, **15 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/indexOfArray.json).

<!-- END MONGO PARITY -->

# $maxN

## Definition

Returns a new array without changing the source list.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$maxN": {
    "input": <input>,
    "n": <n>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `n` | Yes | Positive integer count of elements to return. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $maxN input must be an array |
| missing | Field absent | Error — $maxN input must be an array |
| decimal | 2.5 | Error — $maxN input must be an array |
| numeric string | "12" | Error — $maxN input must be an array |
| text | "hello" | Error — $maxN input must be an array |
| boolean | true | Error — $maxN input must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $maxN input must be an array |
| empty array | [] | [] |
| numeric array | [1,2,3] | [3,2] |
| object | {"x":1} | Error — $maxN input must be an array |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$maxN":[]} | Error — $maxN requires input and n |
| {"$maxN":{"unexpected":1}} | Error — $maxN requires input and n |

## Examples

Expression:
```json
{
  "$maxN": {
    "input": [
      3,
      1,
      2
    ],
    "n": 2
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [3,2].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $maxN input must be an array |
| missing | Field absent | Error — $maxN input must be an array |
| zero | 0 | Error — $maxN input must be an array |
| negative | -2 | Error — $maxN input must be an array |
| decimal | 2.5 | Error — $maxN input must be an array |
| numeric string | "12" | Error — $maxN input must be an array |
| text | "hello" | Error — $maxN input must be an array |
| empty string | "" | Error — $maxN input must be an array |
| boolean | true | Error — $maxN input must be an array |
| false | false | Error — $maxN input must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $maxN input must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $maxN input must be an array |
| empty array | [] | [] |
| numeric array | [1,2,3] | [3,2] |
| mixed array | [1,null,"x",3] | ["x",3] |
| nested array | [[1,2],[3]] | [[3],[1,2]] |
| empty object | {} | Error — $maxN input must be an array |
| object | {"x":1} | Error — $maxN input must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $maxN input must be an array |
| omitted named argument | Argument removed | Error — $maxN requires input and n |

**Argument: `n`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $maxN n must be a positive 64-bit integer |
| missing | Field absent | Error — $maxN n must be a positive 64-bit integer |
| zero | 0 | Error — $maxN n must be a positive 64-bit integer |
| negative | -2 | Error — $maxN n must be a positive 64-bit integer |
| decimal | 2.5 | Error — $maxN n must be a positive 64-bit integer |
| numeric string | "12" | Error — $maxN n must be a positive 64-bit integer |
| text | "hello" | Error — $maxN n must be a positive 64-bit integer |
| empty string | "" | Error — $maxN n must be a positive 64-bit integer |
| boolean | true | Error — $maxN n must be a positive 64-bit integer |
| false | false | Error — $maxN n must be a positive 64-bit integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $maxN n must be a positive 64-bit integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $maxN n must be a positive 64-bit integer |
| empty array | [] | Error — $maxN n must be a positive 64-bit integer |
| numeric array | [1,2,3] | Error — $maxN n must be a positive 64-bit integer |
| mixed array | [1,null,"x",3] | Error — $maxN n must be a positive 64-bit integer |
| nested array | [[1,2],[3]] | Error — $maxN n must be a positive 64-bit integer |
| empty object | {} | Error — $maxN n must be a positive 64-bit integer |
| object | {"x":1} | Error — $maxN n must be a positive 64-bit integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $maxN n must be a positive 64-bit integer |
| omitted named argument | Argument removed | Error — $maxN requires input and n |


</details>

## Verification

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/maxN.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **5 exact BSON matches**, **38 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/maxN.json).

<!-- END MONGO PARITY -->

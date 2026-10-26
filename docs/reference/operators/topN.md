# $topN

## Definition

Sort an array and return its first N items without changing the source.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$topN": {
    "input": <input>,
    "sortBy": <sortBy>,
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
| `sortBy` | Yes | Literal `1` for ascending or `-1` for descending; for object items, an ordered object of field names and directions. |
| `n` | Yes | Positive integer count of elements to return. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $firstN input must be an array |
| missing | Field absent | Error — $firstN input must be an array |
| decimal | 2.5 | Error — $sortArray input must be an array |
| numeric string | "12" | Error — $sortArray input must be an array |
| text | "hello" | Error — $sortArray input must be an array |
| boolean | true | Error — $sortArray input must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $sortArray input must be an array |
| empty array | [] | [] |
| numeric array | [1,2,3] | [3,2] |
| object | {"x":1} | Error — $sortArray input must be an array |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$topN":[]} | Error — $topN requires input, sortBy and n |
| {"$topN":{"unexpected":1}} | Error — $topN requires input, sortBy and n |

## Examples

Expression:
```json
{
  "$topN": {
    "input": [
      3,
      1,
      2
    ],
    "sortBy": -1,
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
| null | null | Error — $firstN input must be an array |
| missing | Field absent | Error — $firstN input must be an array |
| zero | 0 | Error — $sortArray input must be an array |
| negative | -2 | Error — $sortArray input must be an array |
| decimal | 2.5 | Error — $sortArray input must be an array |
| numeric string | "12" | Error — $sortArray input must be an array |
| text | "hello" | Error — $sortArray input must be an array |
| empty string | "" | Error — $sortArray input must be an array |
| boolean | true | Error — $sortArray input must be an array |
| false | false | Error — $sortArray input must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $sortArray input must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $sortArray input must be an array |
| empty array | [] | [] |
| numeric array | [1,2,3] | [3,2] |
| mixed array | [1,null,"x",3] | ["x",3] |
| nested array | [[1,2],[3]] | [[3],[1,2]] |
| empty object | {} | Error — $sortArray input must be an array |
| object | {"x":1} | Error — $sortArray input must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $sortArray input must be an array |
| omitted named argument | Argument removed | Error — $topN requires input, sortBy and n |

**Argument: `sortBy`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $sortArray sort direction must be 1 or -1 |
| zero | 0 | Error — $sortArray sort direction must be 1 or -1 |
| negative | -2 | Error — $sortArray sort direction must be 1 or -1 |
| decimal | 2.5 | Error — $sortArray sort direction must be 1 or -1 |
| numeric string | "12" | Error — $sortArray sort direction must be 1 or -1 |
| text | "hello" | Error — $sortArray sort direction must be 1 or -1 |
| empty string | "" | Error — $sortArray sort direction must be 1 or -1 |
| boolean | true | Error — $sortArray sort direction must be 1 or -1 |
| false | false | Error — $sortArray sort direction must be 1 or -1 |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $sortArray sort direction must be 1 or -1 |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $sortArray sort direction must be 1 or -1 |
| empty array | [] | Error — $sortArray sort direction must be 1 or -1 |
| numeric array | [1,2,3] | Error — $sortArray sort direction must be 1 or -1 |
| mixed array | [1,null,"x",3] | Error — $sortArray sort direction must be 1 or -1 |
| nested array | [[1,2],[3]] | Error — $sortArray sort direction must be 1 or -1 |
| empty object | {} | Error — $sortArray sortBy must not be empty |
| object | {"x":1} | [3,1] |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $sortArray sort direction must be 1 or -1 |
| omitted named argument | Argument removed | Error — $topN requires input, sortBy and n |

**Argument: `n`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $firstN n must be a positive 64-bit integer |
| missing | Field absent | Error — $firstN n must be a positive 64-bit integer |
| zero | 0 | Error — $firstN n must be a positive 64-bit integer |
| negative | -2 | Error — $firstN n must be a positive 64-bit integer |
| decimal | 2.5 | Error — $firstN n must be a positive 64-bit integer |
| numeric string | "12" | Error — $firstN n must be a positive 64-bit integer |
| text | "hello" | Error — $firstN n must be a positive 64-bit integer |
| empty string | "" | Error — $firstN n must be a positive 64-bit integer |
| boolean | true | Error — $firstN n must be a positive 64-bit integer |
| false | false | Error — $firstN n must be a positive 64-bit integer |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $firstN n must be a positive 64-bit integer |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $firstN n must be a positive 64-bit integer |
| empty array | [] | Error — $firstN n must be a positive 64-bit integer |
| numeric array | [1,2,3] | Error — $firstN n must be a positive 64-bit integer |
| mixed array | [1,null,"x",3] | Error — $firstN n must be a positive 64-bit integer |
| nested array | [[1,2],[3]] | Error — $firstN n must be a positive 64-bit integer |
| empty object | {} | Error — $firstN n must be a positive 64-bit integer |
| object | {"x":1} | Error — $firstN n must be a positive 64-bit integer |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $firstN n must be a positive 64-bit integer |
| omitted named argument | Argument removed | Error — $topN requires input, sortBy and n |


</details>

## Verification

This page records **62 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/topN.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **6 exact BSON matches**, **50 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error — $firstN input must be an array | null |
| input / missing | Error — $firstN input must be an array | null |
| n / null | Error — $firstN n must be a positive 64-bit integer | null |
| n / missing | Error — $firstN n must be a positive 64-bit integer | null |
| n / zero | Error — $firstN n must be a positive 64-bit integer | [] |
| sortBy / omitted named argument | Error — $topN requires input, sortBy and n | [1,2] |

</details>

[Download full comparison evidence](../../downloads/operator-parity/topN.json).

<!-- END MONGO PARITY -->

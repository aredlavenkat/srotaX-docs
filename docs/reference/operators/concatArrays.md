# $concatArrays

## Definition

Concatenates arrays.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$concatArrays": [ <array>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | See argument count below | Expression supplying the source array. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `array` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $concatArrays only works with arrays |
| numeric string | "12" | Error — $concatArrays only works with arrays |
| text | "hello" | Error — $concatArrays only works with arrays |
| boolean | true | Error — $concatArrays only works with arrays |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concatArrays only works with arrays |
| empty array | [] | [2] |
| numeric array | [1,2,3] | [1,2,3,2] |
| object | {"x":1} | Error — $concatArrays only works with arrays |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $concatArrays only works with arrays |
| numeric string | "12" | Error — $concatArrays only works with arrays |
| text | "hello" | Error — $concatArrays only works with arrays |
| boolean | true | Error — $concatArrays only works with arrays |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concatArrays only works with arrays |
| empty array | [] | [1] |
| numeric array | [1,2,3] | [1,1,2,3] |
| object | {"x":1} | Error — $concatArrays only works with arrays |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$concatArrays":[]} | [] |
| {"$concatArrays":{"unexpected":1}} | Error — $concatArrays expects a list of arrays |

## Examples

Expression:
```json
{
  "$concatArrays": [
    [
      1
    ],
    [
      2
    ]
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [1,2].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `array[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $concatArrays only works with arrays |
| negative | -2 | Error — $concatArrays only works with arrays |
| decimal | 2.5 | Error — $concatArrays only works with arrays |
| numeric string | "12" | Error — $concatArrays only works with arrays |
| text | "hello" | Error — $concatArrays only works with arrays |
| empty string | "" | Error — $concatArrays only works with arrays |
| boolean | true | Error — $concatArrays only works with arrays |
| false | false | Error — $concatArrays only works with arrays |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concatArrays only works with arrays |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $concatArrays only works with arrays |
| empty array | [] | [2] |
| numeric array | [1,2,3] | [1,2,3,2] |
| mixed array | [1,null,"x",3] | [1,null,"x",3,2] |
| nested array | [[1,2],[3]] | [[1,2],[3],2] |
| empty object | {} | Error — $concatArrays only works with arrays |
| object | {"x":1} | Error — $concatArrays only works with arrays |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $concatArrays only works with arrays |

**Argument: `array[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $concatArrays only works with arrays |
| negative | -2 | Error — $concatArrays only works with arrays |
| decimal | 2.5 | Error — $concatArrays only works with arrays |
| numeric string | "12" | Error — $concatArrays only works with arrays |
| text | "hello" | Error — $concatArrays only works with arrays |
| empty string | "" | Error — $concatArrays only works with arrays |
| boolean | true | Error — $concatArrays only works with arrays |
| false | false | Error — $concatArrays only works with arrays |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $concatArrays only works with arrays |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $concatArrays only works with arrays |
| empty array | [] | [1] |
| numeric array | [1,2,3] | [1,1,2,3] |
| mixed array | [1,null,"x",3] | [1,1,null,"x",3] |
| nested array | [[1,2],[3]] | [1,[1,2],[3]] |
| empty object | {} | Error — $concatArrays only works with arrays |
| object | {"x":1} | Error — $concatArrays only works with arrays |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $concatArrays only works with arrays |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/concatArrays.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **14 exact BSON matches**, **27 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/concatArrays.json).

<!-- END MONGO PARITY -->

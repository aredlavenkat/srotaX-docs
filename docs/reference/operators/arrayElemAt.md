# $arrayElemAt

## Definition

Reads an array item at a positive or negative index.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$arrayElemAt": [ <array>, <index> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | Expression supplying the source array. |
| `index` | Yes | Zero-based array position. A negative position counts from the end. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `array` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $arrayElemAt requires a List and an integer index |
| numeric string | "12" | Error — $arrayElemAt requires a List and an integer index |
| text | "hello" | Error — $arrayElemAt requires a List and an integer index |
| boolean | true | Error — $arrayElemAt requires a List and an integer index |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $arrayElemAt requires a List and an integer index |
| empty array | [] | null |
| numeric array | [1,2,3] | 3 (int32) |
| object | {"x":1} | Error — $arrayElemAt requires a List and an integer index |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$arrayElemAt":[]} | Error — $arrayElemAt expects [array, index] |
| {"$arrayElemAt":{"unexpected":1}} | Error — $arrayElemAt expects [array, index] |

## Examples

Expression:
```json
{
  "$arrayElemAt": [
    [
      1,
      2
    ],
    -1
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `array[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $arrayElemAt requires a List and an integer index |
| negative | -2 | Error — $arrayElemAt requires a List and an integer index |
| decimal | 2.5 | Error — $arrayElemAt requires a List and an integer index |
| numeric string | "12" | Error — $arrayElemAt requires a List and an integer index |
| text | "hello" | Error — $arrayElemAt requires a List and an integer index |
| empty string | "" | Error — $arrayElemAt requires a List and an integer index |
| boolean | true | Error — $arrayElemAt requires a List and an integer index |
| false | false | Error — $arrayElemAt requires a List and an integer index |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $arrayElemAt requires a List and an integer index |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $arrayElemAt requires a List and an integer index |
| empty array | [] | null |
| numeric array | [1,2,3] | 3 (int32) |
| mixed array | [1,null,"x",3] | 3 (int32) |
| nested array | [[1,2],[3]] | [3] |
| empty object | {} | Error — $arrayElemAt requires a List and an integer index |
| object | {"x":1} | Error — $arrayElemAt requires a List and an integer index |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $arrayElemAt requires a List and an integer index |

**Argument: `index[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $arrayElemAt requires a List and an integer index |
| missing | Field absent | Error — $arrayElemAt requires a List and an integer index |
| zero | 0 | 1 (int32) |
| negative | -2 | 1 (int32) |
| decimal | 2.5 | Error — Index must be an int32 |
| numeric string | "12" | Error — $arrayElemAt requires a List and an integer index |
| text | "hello" | Error — $arrayElemAt requires a List and an integer index |
| empty string | "" | Error — $arrayElemAt requires a List and an integer index |
| boolean | true | Error — $arrayElemAt requires a List and an integer index |
| false | false | Error — $arrayElemAt requires a List and an integer index |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $arrayElemAt requires a List and an integer index |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Index must be an int32 |
| empty array | [] | Error — $arrayElemAt requires a List and an integer index |
| numeric array | [1,2,3] | Error — $arrayElemAt requires a List and an integer index |
| mixed array | [1,null,"x",3] | Error — $arrayElemAt requires a List and an integer index |
| nested array | [[1,2],[3]] | Error — $arrayElemAt requires a List and an integer index |
| empty object | {} | Error — $arrayElemAt requires a List and an integer index |
| object | {"x":1} | Error — $arrayElemAt requires a List and an integer index |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $arrayElemAt requires a List and an integer index |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$arrayElemAt": [
    [
      1
    ],
    5
  ]
}
```

Input:
```json
{}
```

**SrotaX:** null.

</details>

## Verification

This page records **42 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/arrayElemAt.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **8 exact BSON matches**, **30 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| array[0] / empty array | null | Missing (field omitted) |
| index[1] / null | Error — $arrayElemAt requires a List and an integer index | null |
| index[1] / missing | Error — $arrayElemAt requires a List and an integer index | null |
| all / boundary example | null | Missing (field omitted) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/arrayElemAt.json).

<!-- END MONGO PARITY -->

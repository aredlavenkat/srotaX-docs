# $setUnion

## Definition

Returns distinct combined array values.

**Expression operator** · Sets · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$setUnion": [ <array>, <other>, ... ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | See argument count below | Expression supplying the source array. |
| `other` | See argument count below | Expression supplying the other array for the set operation. |

Arguments are positional: keep the order shown. Supply 0 or more arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `array` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $setUnion expects each argument to be an array. |
| missing | Field absent | Error — $setUnion expects each argument to be an array. |
| decimal | 2.5 | Error — $setUnion expects each argument to be an array. |
| numeric string | "12" | Error — $setUnion expects each argument to be an array. |
| text | "hello" | Error — $setUnion expects each argument to be an array. |
| boolean | true | Error — $setUnion expects each argument to be an array. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setUnion expects each argument to be an array. |
| empty array | [] | [2,3] |
| numeric array | [1,2,3] | [1,2,3] |
| object | {"x":1} | Error — $setUnion expects each argument to be an array. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$setUnion":[]} | [] |
| {"$setUnion":{"unexpected":1}} | Error — $setUnion expects an array of arrays. |

## Examples

Expression:
```json
{
  "$setUnion": [
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

**Observed SrotaX result:** [1,2,3].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `array[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $setUnion expects each argument to be an array. |
| missing | Field absent | Error — $setUnion expects each argument to be an array. |
| zero | 0 | Error — $setUnion expects each argument to be an array. |
| negative | -2 | Error — $setUnion expects each argument to be an array. |
| decimal | 2.5 | Error — $setUnion expects each argument to be an array. |
| numeric string | "12" | Error — $setUnion expects each argument to be an array. |
| text | "hello" | Error — $setUnion expects each argument to be an array. |
| empty string | "" | Error — $setUnion expects each argument to be an array. |
| boolean | true | Error — $setUnion expects each argument to be an array. |
| false | false | Error — $setUnion expects each argument to be an array. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setUnion expects each argument to be an array. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setUnion expects each argument to be an array. |
| empty array | [] | [2,3] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3,2] |
| nested array | [[1,2],[3]] | [[1,2],[3],2,3] |
| empty object | {} | Error — $setUnion expects each argument to be an array. |
| object | {"x":1} | Error — $setUnion expects each argument to be an array. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $setUnion expects each argument to be an array. |

**Argument: `other[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $setUnion expects each argument to be an array. |
| missing | Field absent | Error — $setUnion expects each argument to be an array. |
| zero | 0 | Error — $setUnion expects each argument to be an array. |
| negative | -2 | Error — $setUnion expects each argument to be an array. |
| decimal | 2.5 | Error — $setUnion expects each argument to be an array. |
| numeric string | "12" | Error — $setUnion expects each argument to be an array. |
| text | "hello" | Error — $setUnion expects each argument to be an array. |
| empty string | "" | Error — $setUnion expects each argument to be an array. |
| boolean | true | Error — $setUnion expects each argument to be an array. |
| false | false | Error — $setUnion expects each argument to be an array. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setUnion expects each argument to be an array. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setUnion expects each argument to be an array. |
| empty array | [] | [1,2] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,2,null,"x",3] |
| nested array | [[1,2],[3]] | [1,2,[1,2],[3]] |
| empty object | {} | Error — $setUnion expects each argument to be an array. |
| object | {"x":1} | Error — $setUnion expects each argument to be an array. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $setUnion expects each argument to be an array. |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setUnion.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **27 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| array[0] / null | Error — $setUnion expects each argument to be an array. | null |
| array[0] / missing | Error — $setUnion expects each argument to be an array. | null |
| array[0] / mixed array | [1,null,"x",3,2] | [null,1,2,3,"x"] |
| array[0] / nested array | [[1,2],[3],2,3] | [2,3,[1,2],[3]] |
| other[1] / null | Error — $setUnion expects each argument to be an array. | null |
| other[1] / missing | Error — $setUnion expects each argument to be an array. | null |
| other[1] / mixed array | [1,2,null,"x",3] | [null,1,2,3,"x"] |

</details>

[Download full comparison evidence](../../downloads/operator-parity/setUnion.json).

<!-- END MONGO PARITY -->

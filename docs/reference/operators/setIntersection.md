# $setIntersection

## Definition

Returns common distinct array values; zero arguments return an empty array.

**Expression operator** · Sets · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$setIntersection": [ <array>, <other>, ... ] }
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
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $setIntersection arguments must resolve to arrays. |
| numeric string | "12" | Error — $setIntersection arguments must resolve to arrays. |
| text | "hello" | Error — $setIntersection arguments must resolve to arrays. |
| boolean | true | Error — $setIntersection arguments must resolve to arrays. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setIntersection arguments must resolve to arrays. |
| empty array | [] | [] |
| numeric array | [1,2,3] | [2,3] |
| object | {"x":1} | Error — $setIntersection arguments must resolve to arrays. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$setIntersection":[]} | [] |
| {"$setIntersection":{"unexpected":1}} | Error — $setIntersection requires an argument list. |

## Examples

Expression:
```json
{
  "$setIntersection": [
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

**Observed SrotaX result:** [2].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `array[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $setIntersection arguments must resolve to arrays. |
| negative | -2 | Error — $setIntersection arguments must resolve to arrays. |
| decimal | 2.5 | Error — $setIntersection arguments must resolve to arrays. |
| numeric string | "12" | Error — $setIntersection arguments must resolve to arrays. |
| text | "hello" | Error — $setIntersection arguments must resolve to arrays. |
| empty string | "" | Error — $setIntersection arguments must resolve to arrays. |
| boolean | true | Error — $setIntersection arguments must resolve to arrays. |
| false | false | Error — $setIntersection arguments must resolve to arrays. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setIntersection arguments must resolve to arrays. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setIntersection arguments must resolve to arrays. |
| empty array | [] | [] |
| numeric array | [1,2,3] | [2,3] |
| mixed array | [1,null,"x",3] | [3] |
| nested array | [[1,2],[3]] | [] |
| empty object | {} | Error — $setIntersection arguments must resolve to arrays. |
| object | {"x":1} | Error — $setIntersection arguments must resolve to arrays. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $setIntersection arguments must resolve to arrays. |

**Argument: `other[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $setIntersection arguments must resolve to arrays. |
| negative | -2 | Error — $setIntersection arguments must resolve to arrays. |
| decimal | 2.5 | Error — $setIntersection arguments must resolve to arrays. |
| numeric string | "12" | Error — $setIntersection arguments must resolve to arrays. |
| text | "hello" | Error — $setIntersection arguments must resolve to arrays. |
| empty string | "" | Error — $setIntersection arguments must resolve to arrays. |
| boolean | true | Error — $setIntersection arguments must resolve to arrays. |
| false | false | Error — $setIntersection arguments must resolve to arrays. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setIntersection arguments must resolve to arrays. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setIntersection arguments must resolve to arrays. |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2] |
| mixed array | [1,null,"x",3] | [1] |
| nested array | [[1,2],[3]] | [] |
| empty object | {} | Error — $setIntersection arguments must resolve to arrays. |
| object | {"x":1} | Error — $setIntersection arguments must resolve to arrays. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $setIntersection arguments must resolve to arrays. |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 6 tested examples</summary>

Expression:
```json
{
  "$setIntersection": [
    [
      1,
      1,
      2
    ]
  ]
}
```

Input:
```json
{}
```

**SrotaX:** [1,2].

Expression:
```json
{
  "$setIntersection": [
    null,
    3
  ]
}
```

Input:
```json
{}
```

**SrotaX:** null.

Expression:
```json
{
  "$setIntersection": [
    3,
    null
  ]
}
```

Input:
```json
{}
```

**SrotaX:** Error — $setIntersection arguments must resolve to arrays..

Expression:
```json
{
  "$setIntersection": [
    [],
    3
  ]
}
```

Input:
```json
{}
```

**SrotaX:** Error — $setIntersection arguments must resolve to arrays..

Expression:
```json
{
  "$setIntersection": [
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

Input:
```json
{}
```

**SrotaX:** [2].

Expression:
```json
{
  "$setIntersection": [
    [
      [
        1,
        2
      ],
      3
    ],
    [
      [
        1,
        2
      ],
      4
    ]
  ]
}
```

Input:
```json
{}
```

**SrotaX:** [[1,2]].

</details>

## Verification

This page records **47 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setIntersection.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **18 exact BSON matches**, **29 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/setIntersection.json).

<!-- END MONGO PARITY -->

# $minDistance

## Definition

Computes minimum planar or spherical distance to supplied points.

**Expression operator** · Arithmetic · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{
  "$minDistance": {
    "input": <input>,
    "points": <points>,
    "spherical": <spherical>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Origin point as `[longitude, latitude]` or an object with a `coordinates` array. |
| `points` | Yes | Array of candidate points in the same format as input. |
| `spherical` | No | Literal boolean, default false. True returns great-circle distance in meters; false returns Euclidean distance in coordinate units. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| missing | Field absent | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| decimal | 2.5 | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| numeric string | "12" | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| text | "hello" | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| boolean | true | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty array | [] | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| numeric array | [1,2,3] | 2.8284271247461903 (double) |
| object | {"x":1} | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$minDistance":[]} | Error — $minDistance expects an object with 'input' and 'points' |
| {"$minDistance":{"unexpected":1}} | Error — $minDistance requires 'input' and 'points' |

## Examples

Expression:
```json
{
  "$minDistance": {
    "input": [
      0,
      0
    ],
    "points": [
      [
        3,
        4
      ]
    ]
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 5.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| missing | Field absent | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| zero | 0 | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| negative | -2 | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| decimal | 2.5 | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| numeric string | "12" | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| text | "hello" | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty string | "" | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| boolean | true | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| false | false | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty array | [] | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| numeric array | [1,2,3] | 2.8284271247461903 (double) |
| mixed array | [1,null,"x",3] | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| nested array | [[1,2],[3]] | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty object | {} | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| object | {"x":1} | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| omitted named argument | Argument removed | Error — $minDistance requires 'input' and 'points' |

**Argument: `points`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $minDistance 'points' must resolve to an array |
| missing | Field absent | Error — $minDistance 'points' must resolve to an array |
| zero | 0 | Error — $minDistance 'points' must resolve to an array |
| negative | -2 | Error — $minDistance 'points' must resolve to an array |
| decimal | 2.5 | Error — $minDistance 'points' must resolve to an array |
| numeric string | "12" | Error — $minDistance 'points' must resolve to an array |
| text | "hello" | Error — $minDistance 'points' must resolve to an array |
| empty string | "" | Error — $minDistance 'points' must resolve to an array |
| boolean | true | Error — $minDistance 'points' must resolve to an array |
| false | false | Error — $minDistance 'points' must resolve to an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $minDistance 'points' must resolve to an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $minDistance 'points' must resolve to an array |
| empty array | [] | null |
| numeric array | [1,2,3] | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| mixed array | [1,null,"x",3] | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| nested array | [[1,2],[3]] | Error — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty object | {} | Error — $minDistance 'points' must resolve to an array |
| object | {"x":1} | Error — $minDistance 'points' must resolve to an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $minDistance 'points' must resolve to an array |
| omitted named argument | Argument removed | Error — $minDistance requires 'input' and 'points' |

**Argument: `spherical`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 5.0 (double) |
| missing | Field absent | 5.0 (double) |
| zero | 0 | 5.0 (double) |
| negative | -2 | 5.0 (double) |
| decimal | 2.5 | 5.0 (double) |
| numeric string | "12" | 5.0 (double) |
| text | "hello" | 5.0 (double) |
| empty string | "" | 5.0 (double) |
| boolean | true | 5.0 (double) |
| false | false | 5.0 (double) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 5.0 (double) |
| decimal128 | {"$numberDecimal":"1.25"} | 5.0 (double) |
| empty array | [] | 5.0 (double) |
| numeric array | [1,2,3] | 5.0 (double) |
| mixed array | [1,null,"x",3] | 5.0 (double) |
| nested array | [[1,2],[3]] | 5.0 (double) |
| empty object | {} | 5.0 (double) |
| object | {"x":1} | 5.0 (double) |
| ISO date string | "2026-01-15T15:00:00Z" | 5.0 (double) |
| omitted named argument | Argument removed | 5.0 (double) |


</details>

## Verification

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/minDistance.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

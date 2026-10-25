# $minDistance

Computes minimum planar or spherical distance to supplied points.

**Category:** Arithmetic. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY | Yes | Expression evaluated against the input |
| `points` | ARRAY | Yes | Expression evaluated against the input |
| `spherical` | BOOLEAN | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 3.

Declared result types: **DOUBLE, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| missing | Field absent | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| zero | 0 | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| negative | -2 | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| decimal | 2.5 | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| numeric string | "12" | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| text | "hello" | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty string | "" | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| boolean | true | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| false | false | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty array | [] | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| numeric array | [1,2,3] | 2.8284271247461903 (double) |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty object | {} | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| object | {"x":1} | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $minDistance requires 'input' and 'points' |

### Argument: `points`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| missing | Field absent | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| zero | 0 | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| negative | -2 | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| decimal | 2.5 | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| numeric string | "12" | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| text | "hello" | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| empty string | "" | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| boolean | true | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| false | false | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| empty array | [] | null |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $minDistance expects GeoJSON point arrays [longitude, latitude] |
| empty object | {} | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| object | {"x":1} | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $minDistance 'points' must resolve to an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $minDistance requires 'input' and 'points' |

### Argument: `spherical`

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

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$minDistance":[]} | Error: IllegalArgumentException — $minDistance expects an object with 'input' and 'points' |
| {"$minDistance":{"unexpected":1}} | Error: IllegalArgumentException — $minDistance requires 'input' and 'points' |

## Scope and reproducibility

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/minDistance.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

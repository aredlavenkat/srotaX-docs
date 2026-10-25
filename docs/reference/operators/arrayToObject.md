# $arrayToObject

Converts key/value entries into an object.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **NULL, OBJECT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$arrayToObject": {
    "$literal": [
      {
        "k": "a",
        "v": 1
      }
    ]
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {"a":1}.

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| negative | -2 | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| decimal | 2.5 | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| numeric string | "12" | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| text | "hello" | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| empty string | "" | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| boolean | true | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| false | false | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| empty array | [] | {} |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $arrayToObject elements must be objects with 'k' and 'v'. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $arrayToObject elements must be objects with 'k' and 'v'. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Object key must be a string |
| empty object | {} | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| object | {"x":1} | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$arrayToObject":[]} | {} |
| {"$arrayToObject":{"unexpected":1}} | Error: IllegalArgumentException — $arrayToObject expects an array of {k, v} objects. |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/arrayToObject.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **17 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / empty arguments | {} | Error: Location16020 — Invalid $project :: caused by :: Expression $arrayToObject takes exactly 1 arguments. 0 were passed in. |

[Download full comparison evidence](../../downloads/operator-parity/arrayToObject.json).

<!-- END MONGO PARITY -->

# $objectToArray

Converts object fields to key/value entries.

**Category:** Arrays. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | OBJECT | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$objectToArray": {
    "a": 1
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [{"k":"a","v":1}].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $objectToArray requires a document input. |
| missing | Field absent | Error: IllegalArgumentException — $objectToArray requires a document input. |
| zero | 0 | Error: IllegalArgumentException — $objectToArray requires a document input. |
| negative | -2 | Error: IllegalArgumentException — $objectToArray requires a document input. |
| decimal | 2.5 | Error: IllegalArgumentException — $objectToArray requires a document input. |
| numeric string | "12" | Error: IllegalArgumentException — $objectToArray requires a document input. |
| text | "hello" | Error: IllegalArgumentException — $objectToArray requires a document input. |
| empty string | "" | Error: IllegalArgumentException — $objectToArray requires a document input. |
| boolean | true | Error: IllegalArgumentException — $objectToArray requires a document input. |
| false | false | Error: IllegalArgumentException — $objectToArray requires a document input. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $objectToArray requires a document input. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $objectToArray requires a document input. |
| empty array | [] | Error: IllegalArgumentException — $objectToArray requires a document input. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $objectToArray requires a document input. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $objectToArray requires a document input. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $objectToArray requires a document input. |
| empty object | {} | [] |
| object | {"x":1} | [{"k":"x","v":1}] |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $objectToArray requires a document input. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$objectToArray":[]} | Error: IllegalArgumentException — $objectToArray requires a document input. |
| {"$objectToArray":{"unexpected":1}} | [{"k":"unexpected","v":1}] |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/objectToArray.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **16 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error: IllegalArgumentException — $objectToArray requires a document input. | null |
| input / missing | Error: IllegalArgumentException — $objectToArray requires a document input. | null |

[Download full comparison evidence](../../downloads/operator-parity/objectToArray.json).

<!-- END MONGO PARITY -->

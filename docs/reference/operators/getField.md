# $getField

Reads a named field from an explicit object.

**Category:** Objects. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `field` | STRING | Yes | Expression evaluated against the input |
| `input` | OBJECT | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **ANY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$getField": {
    "field": "a",
    "input": {
      "a": 1
    }
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 1 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `field`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $getField requires a document input and string field. |
| missing | Field absent | Error: IllegalArgumentException — $getField requires a document input and string field. |
| zero | 0 | Error: IllegalArgumentException — $getField requires a document input and string field. |
| negative | -2 | Error: IllegalArgumentException — $getField requires a document input and string field. |
| decimal | 2.5 | Error: IllegalArgumentException — $getField requires a document input and string field. |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | null |
| boolean | true | Error: IllegalArgumentException — $getField requires a document input and string field. |
| false | false | Error: IllegalArgumentException — $getField requires a document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $getField requires a document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $getField requires a document input and string field. |
| empty array | [] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| empty object | {} | Error: IllegalArgumentException — $getField requires a document input and string field. |
| object | {"x":1} | Error: IllegalArgumentException — $getField requires a document input and string field. |
| ISO date string | "2026-01-15T15:00:00Z" | null |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $getField requires 'field' and 'input' keys. |

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $getField requires a document input and string field. |
| missing | Field absent | Error: IllegalArgumentException — $getField requires a document input and string field. |
| zero | 0 | Error: IllegalArgumentException — $getField requires a document input and string field. |
| negative | -2 | Error: IllegalArgumentException — $getField requires a document input and string field. |
| decimal | 2.5 | Error: IllegalArgumentException — $getField requires a document input and string field. |
| numeric string | "12" | Error: IllegalArgumentException — $getField requires a document input and string field. |
| text | "hello" | Error: IllegalArgumentException — $getField requires a document input and string field. |
| empty string | "" | Error: IllegalArgumentException — $getField requires a document input and string field. |
| boolean | true | Error: IllegalArgumentException — $getField requires a document input and string field. |
| false | false | Error: IllegalArgumentException — $getField requires a document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $getField requires a document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $getField requires a document input and string field. |
| empty array | [] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $getField requires a document input and string field. |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $getField requires a document input and string field. |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $getField requires 'field' and 'input' keys. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$getField":[]} | Error: IllegalArgumentException — $getField requires 'field' and 'input' keys. |
| {"$getField":{"unexpected":1}} | Error: IllegalArgumentException — $getField requires 'field' and 'input' keys. |

## Additional boundary examples

<details>
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$getField": {
    "field": "b",
    "input": {
      "a": 1
    }
  }
}
```

Input:
```json
{}
```

**SrotaX:** null.

</details>

## Scope and reproducibility

This page records **44 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/getField.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **1 exact BSON matches**, **19 both rejected**, **24 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| field / numeric string | null | Missing (field omitted) |
| field / text | null | Missing (field omitted) |
| field / empty string | null | Missing (field omitted) |
| field / ISO date string | null | Missing (field omitted) |
| input / null | Error: IllegalArgumentException — $getField requires a document input and string field. | null |
| input / missing | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / zero | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / negative | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / decimal | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / numeric string | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / text | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / empty string | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / boolean | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / false | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / typed date | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / decimal128 | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / empty array | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / numeric array | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / mixed array | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / nested array | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| input / empty object | null | Missing (field omitted) |
| input / object | null | Missing (field omitted) |
| input / ISO date string | Error: IllegalArgumentException — $getField requires a document input and string field. | Missing (field omitted) |
| all / boundary example | null | Missing (field omitted) |

[Download full comparison evidence](../../downloads/operator-parity/getField.json).

<!-- END MONGO PARITY -->

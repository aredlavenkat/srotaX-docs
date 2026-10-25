# $setField

Sets a named field on an object copy.

**Category:** Objects. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `field` | STRING | Yes | Expression evaluated against the input |
| `input` | OBJECT | Yes | Expression evaluated against the input |
| `value` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 3; maximum 3.

Declared result types: **OBJECT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$setField": {
    "field": "a",
    "input": {},
    "value": 1
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

### Argument: `field`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $setField requires document input and string field. |
| missing | Field absent | Error: IllegalArgumentException — $setField requires document input and string field. |
| zero | 0 | Error: IllegalArgumentException — $setField requires document input and string field. |
| negative | -2 | Error: IllegalArgumentException — $setField requires document input and string field. |
| decimal | 2.5 | Error: IllegalArgumentException — $setField requires document input and string field. |
| numeric string | "12" | {"12":1} |
| text | "hello" | {"hello":1} |
| empty string | "" | {"":1} |
| boolean | true | Error: IllegalArgumentException — $setField requires document input and string field. |
| false | false | Error: IllegalArgumentException — $setField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $setField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $setField requires document input and string field. |
| empty array | [] | Error: IllegalArgumentException — $setField requires document input and string field. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $setField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $setField requires document input and string field. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $setField requires document input and string field. |
| empty object | {} | Error: IllegalArgumentException — $setField requires document input and string field. |
| object | {"x":1} | Error: IllegalArgumentException — $setField requires document input and string field. |
| ISO date string | "2026-01-15T15:00:00Z" | {"2026-01-15T15:00:00Z":1} |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $setField requires 'field', 'input', and 'value' keys. |

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $setField requires document input and string field. |
| missing | Field absent | Error: IllegalArgumentException — $setField requires document input and string field. |
| zero | 0 | Error: IllegalArgumentException — $setField requires document input and string field. |
| negative | -2 | Error: IllegalArgumentException — $setField requires document input and string field. |
| decimal | 2.5 | Error: IllegalArgumentException — $setField requires document input and string field. |
| numeric string | "12" | Error: IllegalArgumentException — $setField requires document input and string field. |
| text | "hello" | Error: IllegalArgumentException — $setField requires document input and string field. |
| empty string | "" | Error: IllegalArgumentException — $setField requires document input and string field. |
| boolean | true | Error: IllegalArgumentException — $setField requires document input and string field. |
| false | false | Error: IllegalArgumentException — $setField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $setField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $setField requires document input and string field. |
| empty array | [] | Error: IllegalArgumentException — $setField requires document input and string field. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $setField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $setField requires document input and string field. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $setField requires document input and string field. |
| empty object | {} | {"a":1} |
| object | {"x":1} | {"x":1,"a":1} |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $setField requires document input and string field. |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $setField requires 'field', 'input', and 'value' keys. |

### Argument: `value`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | {"a":null} |
| missing | Field absent | {"a":null} |
| zero | 0 | {"a":0} |
| negative | -2 | {"a":-2} |
| decimal | 2.5 | {"a":2.5} |
| numeric string | "12" | {"a":"12"} |
| text | "hello" | {"a":"hello"} |
| empty string | "" | {"a":""} |
| boolean | true | {"a":true} |
| false | false | {"a":false} |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {"a":{"$date":1768489200000}} |
| decimal128 | {"$numberDecimal":"1.25"} | {"a":{"$numberDecimal":"1.25"}} |
| empty array | [] | {"a":[]} |
| numeric array | [1,2,3] | {"a":[1,2,3]} |
| mixed array | [1,null,"x",3] | {"a":[1,null,"x",3]} |
| nested array | [[1,2],[3]] | {"a":[[1,2],[3]]} |
| empty object | {} | {"a":{}} |
| object | {"x":1} | {"a":{"x":1}} |
| ISO date string | "2026-01-15T15:00:00Z" | {"a":"2026-01-15T15:00:00Z"} |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $setField requires 'field', 'input', and 'value' keys. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$setField":[]} | Error: IllegalArgumentException — $setField requires 'field', 'input', and 'value' keys. |
| {"$setField":{"unexpected":1}} | Error: IllegalArgumentException — $setField requires 'field', 'input', and 'value' keys. |

## Scope and reproducibility

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setField.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **21 exact BSON matches**, **35 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| field / numeric string | {"12":1} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / text | {"hello":1} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / empty string | {"":1} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / ISO date string | {"2026-01-15T15:00:00Z":1} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| input / null | Error: IllegalArgumentException — $setField requires document input and string field. | null |
| input / missing | Error: IllegalArgumentException — $setField requires document input and string field. | null |
| value / missing | {"a":null} | {} |

[Download full comparison evidence](../../downloads/operator-parity/setField.json).

<!-- END MONGO PARITY -->

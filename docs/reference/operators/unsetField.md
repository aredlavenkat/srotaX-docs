# $unsetField

Removes a named field from an object copy.

**Category:** Objects. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `field` | STRING | Yes | Expression evaluated against the input |
| `input` | OBJECT | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **OBJECT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$unsetField": {
    "field": "a",
    "input": {
      "a": 1,
      "b": 2
    }
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {"b":2}.

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `field`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| missing | Field absent | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| zero | 0 | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| negative | -2 | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| decimal | 2.5 | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| numeric string | "12" | {"a":1,"b":2} |
| text | "hello" | {"a":1,"b":2} |
| empty string | "" | {"a":1,"b":2} |
| boolean | true | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| false | false | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| empty array | [] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| empty object | {} | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| object | {"x":1} | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| ISO date string | "2026-01-15T15:00:00Z" | {"a":1,"b":2} |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $unsetField requires 'field' and 'input' keys. |

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| missing | Field absent | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| zero | 0 | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| negative | -2 | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| decimal | 2.5 | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| numeric string | "12" | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| text | "hello" | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| empty string | "" | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| boolean | true | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| false | false | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| empty array | [] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $unsetField requires document input and string field. |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $unsetField requires 'field' and 'input' keys. |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$unsetField":[]} | Error: IllegalArgumentException — $unsetField requires 'field' and 'input' keys. |
| {"$unsetField":{"unexpected":1}} | Error: IllegalArgumentException — $unsetField requires 'field' and 'input' keys. |

## Scope and reproducibility

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/unsetField.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **34 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| field / numeric string | {"a":1,"b":2} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / text | {"a":1,"b":2} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / empty string | {"a":1,"b":2} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / ISO date string | {"a":1,"b":2} | Error: Location4161108 — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| input / null | Error: IllegalArgumentException — $unsetField requires document input and string field. | null |
| input / missing | Error: IllegalArgumentException — $unsetField requires document input and string field. | null |

[Download full comparison evidence](../../downloads/operator-parity/unsetField.json).

<!-- END MONGO PARITY -->

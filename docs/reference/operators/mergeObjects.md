# $mergeObjects

Combines objects with later values replacing earlier fields.

**Category:** Objects. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `object` | OBJECT | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum variadic.

Declared result types: **OBJECT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$mergeObjects": [
    {
      "a": 1
    },
    {
      "b": 2
    }
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {"a":1,"b":2}.

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `object[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | {"b":2} |
| missing | Field absent | {"b":2} |
| zero | 0 | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| negative | -2 | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| decimal | 2.5 | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| numeric string | "12" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| text | "hello" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| empty string | "" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| boolean | true | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| false | false | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| empty array | [] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| empty object | {} | {"b":2} |
| object | {"x":1} | {"x":1,"b":2} |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |

### Argument: `object[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | {"a":1} |
| missing | Field absent | {"a":1} |
| zero | 0 | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| negative | -2 | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| decimal | 2.5 | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| numeric string | "12" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| text | "hello" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| empty string | "" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| boolean | true | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| false | false | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| empty array | [] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |
| empty object | {} | {"a":1} |
| object | {"x":1} | {"a":1,"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $mergeObjects only accepts documents (objects). |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$mergeObjects":[]} | {} |
| {"$mergeObjects":{"unexpected":1}} | {"unexpected":1} |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/mergeObjects.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **11 exact BSON matches**, **30 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/mergeObjects.json).

<!-- END MONGO PARITY -->

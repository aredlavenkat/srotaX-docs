# $switch

Selects the first branch with a true boolean condition.

**Category:** Conditional. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `branches` | ARRAY | Yes | Expression evaluated against the input |
| `default` | ANY | No | Expression evaluated against the input |

Argument count: minimum 1; maximum 2.

Declared result types: **ANY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$switch": {
    "branches": [
      {
        "case": true,
        "then": "yes"
      }
    ],
    "default": "no"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "yes".

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `branches`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $switch 'branches' must be a list |
| missing | Field absent | Error: IllegalArgumentException — $switch 'branches' must be a list |
| zero | 0 | Error: IllegalArgumentException — $switch 'branches' must be a list |
| negative | -2 | Error: IllegalArgumentException — $switch 'branches' must be a list |
| decimal | 2.5 | Error: IllegalArgumentException — $switch 'branches' must be a list |
| numeric string | "12" | Error: IllegalArgumentException — $switch 'branches' must be a list |
| text | "hello" | Error: IllegalArgumentException — $switch 'branches' must be a list |
| empty string | "" | Error: IllegalArgumentException — $switch 'branches' must be a list |
| boolean | true | Error: IllegalArgumentException — $switch 'branches' must be a list |
| false | false | Error: IllegalArgumentException — $switch 'branches' must be a list |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $switch 'branches' must be a list |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $switch 'branches' must be a list |
| empty array | [] | Error: IllegalArgumentException — $switch 'branches' must be a list |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $switch 'branches' must be a list |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $switch 'branches' must be a list |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $switch 'branches' must be a list |
| empty object | {} | Error: IllegalArgumentException — $switch 'branches' must be a list |
| object | {"x":1} | Error: IllegalArgumentException — $switch 'branches' must be a list |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $switch 'branches' must be a list |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $switch 'branches' must be a list |

### Argument: `default`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | "yes" |
| missing | Field absent | "yes" |
| zero | 0 | "yes" |
| negative | -2 | "yes" |
| decimal | 2.5 | "yes" |
| numeric string | "12" | "yes" |
| text | "hello" | "yes" |
| empty string | "" | "yes" |
| boolean | true | "yes" |
| false | false | "yes" |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "yes" |
| decimal128 | {"$numberDecimal":"1.25"} | "yes" |
| empty array | [] | "yes" |
| numeric array | [1,2,3] | "yes" |
| mixed array | [1,null,"x",3] | "yes" |
| nested array | [[1,2],[3]] | "yes" |
| empty object | {} | "yes" |
| object | {"x":1} | "yes" |
| ISO date string | "2026-01-15T15:00:00Z" | "yes" |
| omitted named argument | Argument removed | "yes" |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$switch":[]} | Error: IllegalArgumentException — $switch requires a document with 'branches' and optional 'default' |
| {"$switch":{"unexpected":1}} | Error: IllegalArgumentException — $switch 'branches' must be a list |

## Scope and reproducibility

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/switch.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **21 exact BSON matches**, **22 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/switch.json).

<!-- END MONGO PARITY -->

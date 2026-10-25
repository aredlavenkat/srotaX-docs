# $bsonSize

Returns the actual BSON-encoded document size in bytes, or null for null input.

**Category:** Types and conversion. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | OBJECT | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **INT, NULL**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$bsonSize": {}
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 5 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $bsonSize expects a document or object |
| negative | -2 | Error: IllegalArgumentException — $bsonSize expects a document or object |
| decimal | 2.5 | Error: IllegalArgumentException — $bsonSize expects a document or object |
| numeric string | "12" | Error: IllegalArgumentException — $bsonSize expects a document or object |
| text | "hello" | Error: IllegalArgumentException — $bsonSize expects a document or object |
| empty string | "" | Error: IllegalArgumentException — $bsonSize expects a document or object |
| boolean | true | Error: IllegalArgumentException — $bsonSize expects a document or object |
| false | false | Error: IllegalArgumentException — $bsonSize expects a document or object |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $bsonSize expects a document or object |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $bsonSize expects a document or object |
| empty array | [] | Error: IllegalArgumentException — $bsonSize expects a document or object |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $bsonSize expects a document or object |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $bsonSize expects a document or object |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $bsonSize expects a document or object |
| empty object | {} | 5 (int32) |
| object | {"x":1} | 12 (int32) |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $bsonSize expects a document or object |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$bsonSize":[]} | Error: IllegalArgumentException — $bsonSize expects a document or object |
| {"$bsonSize":{"unexpected":1}} | 21 (int32) |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/bsonSize.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **6 exact BSON matches**, **16 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/bsonSize.json).

<!-- END MONGO PARITY -->

# $toObjectId

Converts a value to objectid.

**Category:** Types and conversion. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **NULL, OBJECT_ID**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$toObjectId": "507f1f77bcf86cd799439011"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 507f1f77bcf86cd799439011 (ObjectId).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — $convert failed for target objectId |
| negative | -2 | Error: IllegalArgumentException — $convert failed for target objectId |
| decimal | 2.5 | Error: IllegalArgumentException — $convert failed for target objectId |
| numeric string | "12" | Error: IllegalArgumentException — $convert failed for target objectId |
| text | "hello" | Error: IllegalArgumentException — $convert failed for target objectId |
| empty string | "" | Error: IllegalArgumentException — $convert failed for target objectId |
| boolean | true | Error: IllegalArgumentException — $convert failed for target objectId |
| false | false | Error: IllegalArgumentException — $convert failed for target objectId |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $convert failed for target objectId |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $convert failed for target objectId |
| empty array | [] | Error: IllegalArgumentException — $convert failed for target objectId |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $convert failed for target objectId |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $convert failed for target objectId |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $convert failed for target objectId |
| empty object | {} | Error: IllegalArgumentException — $convert failed for target objectId |
| object | {"x":1} | Error: IllegalArgumentException — $convert failed for target objectId |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $convert failed for target objectId |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$toObjectId":[]} | Error: IllegalArgumentException — $convert failed for target objectId |
| {"$toObjectId":{"unexpected":1}} | Error: IllegalArgumentException — $convert failed for target objectId |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toObjectId.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **19 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/toObjectId.json).

<!-- END MONGO PARITY -->

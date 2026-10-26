# $toObjectId

## Definition

Converts a value to objectid.

**Expression operator** · Types and conversion · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$toObjectId": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $convert failed for target objectId |
| numeric string | "12" | Error — $convert failed for target objectId |
| text | "hello" | Error — $convert failed for target objectId |
| boolean | true | Error — $convert failed for target objectId |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $convert failed for target objectId |
| empty array | [] | Error — $convert failed for target objectId |
| numeric array | [1,2,3] | Error — $convert failed for target objectId |
| object | {"x":1} | Error — $convert failed for target objectId |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$toObjectId":[]} | Error — $convert failed for target objectId |
| {"$toObjectId":{"unexpected":1}} | Error — $convert failed for target objectId |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $convert failed for target objectId |
| negative | -2 | Error — $convert failed for target objectId |
| decimal | 2.5 | Error — $convert failed for target objectId |
| numeric string | "12" | Error — $convert failed for target objectId |
| text | "hello" | Error — $convert failed for target objectId |
| empty string | "" | Error — $convert failed for target objectId |
| boolean | true | Error — $convert failed for target objectId |
| false | false | Error — $convert failed for target objectId |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $convert failed for target objectId |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $convert failed for target objectId |
| empty array | [] | Error — $convert failed for target objectId |
| numeric array | [1,2,3] | Error — $convert failed for target objectId |
| mixed array | [1,null,"x",3] | Error — $convert failed for target objectId |
| nested array | [[1,2],[3]] | Error — $convert failed for target objectId |
| empty object | {} | Error — $convert failed for target objectId |
| object | {"x":1} | Error — $convert failed for target objectId |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $convert failed for target objectId |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toObjectId.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **19 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/toObjectId.json).

<!-- END MONGO PARITY -->

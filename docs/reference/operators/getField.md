# $getField

## Definition

Reads a named field from an explicit object.

**Expression operator** · Objects · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$getField": {
    "field": <field>,
    "input": <input>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `field` | Yes | Expression supplying the field name to read or change. |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `field` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $getField requires a document input and string field. |
| missing | Field absent | Error — $getField requires a document input and string field. |
| decimal | 2.5 | Error — $getField requires a document input and string field. |
| numeric string | "12" | null |
| text | "hello" | null |
| boolean | true | Error — $getField requires a document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $getField requires a document input and string field. |
| empty array | [] | Error — $getField requires a document input and string field. |
| numeric array | [1,2,3] | Error — $getField requires a document input and string field. |
| object | {"x":1} | Error — $getField requires a document input and string field. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$getField":[]} | Error — $getField requires 'field' and 'input' keys. |
| {"$getField":{"unexpected":1}} | Error — $getField requires 'field' and 'input' keys. |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `field`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $getField requires a document input and string field. |
| missing | Field absent | Error — $getField requires a document input and string field. |
| zero | 0 | Error — $getField requires a document input and string field. |
| negative | -2 | Error — $getField requires a document input and string field. |
| decimal | 2.5 | Error — $getField requires a document input and string field. |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | null |
| boolean | true | Error — $getField requires a document input and string field. |
| false | false | Error — $getField requires a document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $getField requires a document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $getField requires a document input and string field. |
| empty array | [] | Error — $getField requires a document input and string field. |
| numeric array | [1,2,3] | Error — $getField requires a document input and string field. |
| mixed array | [1,null,"x",3] | Error — $getField requires a document input and string field. |
| nested array | [[1,2],[3]] | Error — $getField requires a document input and string field. |
| empty object | {} | Error — $getField requires a document input and string field. |
| object | {"x":1} | Error — $getField requires a document input and string field. |
| ISO date string | "2026-01-15T15:00:00Z" | null |
| omitted named argument | Argument removed | Error — $getField requires 'field' and 'input' keys. |

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $getField requires a document input and string field. |
| missing | Field absent | Error — $getField requires a document input and string field. |
| zero | 0 | Error — $getField requires a document input and string field. |
| negative | -2 | Error — $getField requires a document input and string field. |
| decimal | 2.5 | Error — $getField requires a document input and string field. |
| numeric string | "12" | Error — $getField requires a document input and string field. |
| text | "hello" | Error — $getField requires a document input and string field. |
| empty string | "" | Error — $getField requires a document input and string field. |
| boolean | true | Error — $getField requires a document input and string field. |
| false | false | Error — $getField requires a document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $getField requires a document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $getField requires a document input and string field. |
| empty array | [] | Error — $getField requires a document input and string field. |
| numeric array | [1,2,3] | Error — $getField requires a document input and string field. |
| mixed array | [1,null,"x",3] | Error — $getField requires a document input and string field. |
| nested array | [[1,2],[3]] | Error — $getField requires a document input and string field. |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $getField requires a document input and string field. |
| omitted named argument | Argument removed | Error — $getField requires 'field' and 'input' keys. |


</details>

## Additional boundary examples

<details markdown="1">
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

## Verification

This page records **44 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/getField.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **1 exact BSON matches**, **19 both rejected**, **24 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| field / numeric string | null | Missing (field omitted) |
| field / text | null | Missing (field omitted) |
| field / empty string | null | Missing (field omitted) |
| field / ISO date string | null | Missing (field omitted) |
| input / null | Error — $getField requires a document input and string field. | null |
| input / missing | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / zero | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / negative | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / decimal | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / numeric string | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / text | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / empty string | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / boolean | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / false | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / typed date | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / decimal128 | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / empty array | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / numeric array | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / mixed array | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / nested array | Error — $getField requires a document input and string field. | Missing (field omitted) |
| input / empty object | null | Missing (field omitted) |
| input / object | null | Missing (field omitted) |
| input / ISO date string | Error — $getField requires a document input and string field. | Missing (field omitted) |
| all / boundary example | null | Missing (field omitted) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/getField.json).

<!-- END MONGO PARITY -->

# $setField

## Definition

Sets a named field on an object copy.

**Expression operator** · Objects · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$setField": {
    "field": <field>,
    "input": <input>,
    "value": <value>
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
| `value` | Yes | Expression supplying the value to evaluate. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `field` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $setField requires document input and string field. |
| missing | Field absent | Error — $setField requires document input and string field. |
| decimal | 2.5 | Error — $setField requires document input and string field. |
| numeric string | "12" | {"12":1} |
| text | "hello" | {"hello":1} |
| boolean | true | Error — $setField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setField requires document input and string field. |
| empty array | [] | Error — $setField requires document input and string field. |
| numeric array | [1,2,3] | Error — $setField requires document input and string field. |
| object | {"x":1} | Error — $setField requires document input and string field. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$setField":[]} | Error — $setField requires 'field', 'input', and 'value' keys. |
| {"$setField":{"unexpected":1}} | Error — $setField requires 'field', 'input', and 'value' keys. |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `field`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $setField requires document input and string field. |
| missing | Field absent | Error — $setField requires document input and string field. |
| zero | 0 | Error — $setField requires document input and string field. |
| negative | -2 | Error — $setField requires document input and string field. |
| decimal | 2.5 | Error — $setField requires document input and string field. |
| numeric string | "12" | {"12":1} |
| text | "hello" | {"hello":1} |
| empty string | "" | {"":1} |
| boolean | true | Error — $setField requires document input and string field. |
| false | false | Error — $setField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setField requires document input and string field. |
| empty array | [] | Error — $setField requires document input and string field. |
| numeric array | [1,2,3] | Error — $setField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error — $setField requires document input and string field. |
| nested array | [[1,2],[3]] | Error — $setField requires document input and string field. |
| empty object | {} | Error — $setField requires document input and string field. |
| object | {"x":1} | Error — $setField requires document input and string field. |
| ISO date string | "2026-01-15T15:00:00Z" | {"2026-01-15T15:00:00Z":1} |
| omitted named argument | Argument removed | Error — $setField requires 'field', 'input', and 'value' keys. |

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $setField requires document input and string field. |
| missing | Field absent | Error — $setField requires document input and string field. |
| zero | 0 | Error — $setField requires document input and string field. |
| negative | -2 | Error — $setField requires document input and string field. |
| decimal | 2.5 | Error — $setField requires document input and string field. |
| numeric string | "12" | Error — $setField requires document input and string field. |
| text | "hello" | Error — $setField requires document input and string field. |
| empty string | "" | Error — $setField requires document input and string field. |
| boolean | true | Error — $setField requires document input and string field. |
| false | false | Error — $setField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $setField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $setField requires document input and string field. |
| empty array | [] | Error — $setField requires document input and string field. |
| numeric array | [1,2,3] | Error — $setField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error — $setField requires document input and string field. |
| nested array | [[1,2],[3]] | Error — $setField requires document input and string field. |
| empty object | {} | {"a":1} |
| object | {"x":1} | {"x":1,"a":1} |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $setField requires document input and string field. |
| omitted named argument | Argument removed | Error — $setField requires 'field', 'input', and 'value' keys. |

**Argument: `value`**

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
| omitted named argument | Argument removed | Error — $setField requires 'field', 'input', and 'value' keys. |


</details>

## Verification

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/setField.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **21 exact BSON matches**, **35 both rejected**, **7 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| field / numeric string | {"12":1} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / text | {"hello":1} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / empty string | {"":1} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / ISO date string | {"2026-01-15T15:00:00Z":1} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| input / null | Error — $setField requires document input and string field. | null |
| input / missing | Error — $setField requires document input and string field. | null |
| value / missing | {"a":null} | {} |

</details>

[Download full comparison evidence](../../downloads/operator-parity/setField.json).

<!-- END MONGO PARITY -->

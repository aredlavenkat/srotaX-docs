# $unsetField

## Definition

Removes a named field from an object copy.

**Expression operator** · Objects · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$unsetField": {
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
| null | null | Error — $unsetField requires document input and string field. |
| missing | Field absent | Error — $unsetField requires document input and string field. |
| decimal | 2.5 | Error — $unsetField requires document input and string field. |
| numeric string | "12" | {"a":1,"b":2} |
| text | "hello" | {"a":1,"b":2} |
| boolean | true | Error — $unsetField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $unsetField requires document input and string field. |
| empty array | [] | Error — $unsetField requires document input and string field. |
| numeric array | [1,2,3] | Error — $unsetField requires document input and string field. |
| object | {"x":1} | Error — $unsetField requires document input and string field. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$unsetField":[]} | Error — $unsetField requires 'field' and 'input' keys. |
| {"$unsetField":{"unexpected":1}} | Error — $unsetField requires 'field' and 'input' keys. |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `field`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $unsetField requires document input and string field. |
| missing | Field absent | Error — $unsetField requires document input and string field. |
| zero | 0 | Error — $unsetField requires document input and string field. |
| negative | -2 | Error — $unsetField requires document input and string field. |
| decimal | 2.5 | Error — $unsetField requires document input and string field. |
| numeric string | "12" | {"a":1,"b":2} |
| text | "hello" | {"a":1,"b":2} |
| empty string | "" | {"a":1,"b":2} |
| boolean | true | Error — $unsetField requires document input and string field. |
| false | false | Error — $unsetField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $unsetField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $unsetField requires document input and string field. |
| empty array | [] | Error — $unsetField requires document input and string field. |
| numeric array | [1,2,3] | Error — $unsetField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error — $unsetField requires document input and string field. |
| nested array | [[1,2],[3]] | Error — $unsetField requires document input and string field. |
| empty object | {} | Error — $unsetField requires document input and string field. |
| object | {"x":1} | Error — $unsetField requires document input and string field. |
| ISO date string | "2026-01-15T15:00:00Z" | {"a":1,"b":2} |
| omitted named argument | Argument removed | Error — $unsetField requires 'field' and 'input' keys. |

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $unsetField requires document input and string field. |
| missing | Field absent | Error — $unsetField requires document input and string field. |
| zero | 0 | Error — $unsetField requires document input and string field. |
| negative | -2 | Error — $unsetField requires document input and string field. |
| decimal | 2.5 | Error — $unsetField requires document input and string field. |
| numeric string | "12" | Error — $unsetField requires document input and string field. |
| text | "hello" | Error — $unsetField requires document input and string field. |
| empty string | "" | Error — $unsetField requires document input and string field. |
| boolean | true | Error — $unsetField requires document input and string field. |
| false | false | Error — $unsetField requires document input and string field. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $unsetField requires document input and string field. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $unsetField requires document input and string field. |
| empty array | [] | Error — $unsetField requires document input and string field. |
| numeric array | [1,2,3] | Error — $unsetField requires document input and string field. |
| mixed array | [1,null,"x",3] | Error — $unsetField requires document input and string field. |
| nested array | [[1,2],[3]] | Error — $unsetField requires document input and string field. |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $unsetField requires document input and string field. |
| omitted named argument | Argument removed | Error — $unsetField requires 'field' and 'input' keys. |


</details>

## Verification

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/unsetField.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **3 exact BSON matches**, **34 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| field / numeric string | {"a":1,"b":2} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / text | {"a":1,"b":2} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / empty string | {"a":1,"b":2} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| field / ISO date string | {"a":1,"b":2} | Error — Invalid $project :: caused by :: '$CURRENT.probe' is a field path reference which is not allowed in this context. Did you mean {$literal: '$CURRENT.probe'}? |
| input / null | Error — $unsetField requires document input and string field. | null |
| input / missing | Error — $unsetField requires document input and string field. | null |

</details>

[Download full comparison evidence](../../downloads/operator-parity/unsetField.json).

<!-- END MONGO PARITY -->

# $arrayToObject

## Definition

Converts key/value entries into an object.

**Expression operator** · Arrays · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$arrayToObject": <expression> }
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
| decimal | 2.5 | Error — $arrayToObject expects an array of {k, v} objects. |
| numeric string | "12" | Error — $arrayToObject expects an array of {k, v} objects. |
| text | "hello" | Error — $arrayToObject expects an array of {k, v} objects. |
| boolean | true | Error — $arrayToObject expects an array of {k, v} objects. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $arrayToObject expects an array of {k, v} objects. |
| empty array | [] | {} |
| numeric array | [1,2,3] | Error — $arrayToObject elements must be objects with 'k' and 'v'. |
| object | {"x":1} | Error — $arrayToObject expects an array of {k, v} objects. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$arrayToObject":[]} | {} |
| {"$arrayToObject":{"unexpected":1}} | Error — $arrayToObject expects an array of {k, v} objects. |

## Examples

Expression:
```json
{
  "$arrayToObject": {
    "$literal": [
      {
        "k": "a",
        "v": 1
      }
    ]
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

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $arrayToObject expects an array of {k, v} objects. |
| negative | -2 | Error — $arrayToObject expects an array of {k, v} objects. |
| decimal | 2.5 | Error — $arrayToObject expects an array of {k, v} objects. |
| numeric string | "12" | Error — $arrayToObject expects an array of {k, v} objects. |
| text | "hello" | Error — $arrayToObject expects an array of {k, v} objects. |
| empty string | "" | Error — $arrayToObject expects an array of {k, v} objects. |
| boolean | true | Error — $arrayToObject expects an array of {k, v} objects. |
| false | false | Error — $arrayToObject expects an array of {k, v} objects. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $arrayToObject expects an array of {k, v} objects. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $arrayToObject expects an array of {k, v} objects. |
| empty array | [] | {} |
| numeric array | [1,2,3] | Error — $arrayToObject elements must be objects with 'k' and 'v'. |
| mixed array | [1,null,"x",3] | Error — $arrayToObject elements must be objects with 'k' and 'v'. |
| nested array | [[1,2],[3]] | Error — Object key must be a string |
| empty object | {} | Error — $arrayToObject expects an array of {k, v} objects. |
| object | {"x":1} | Error — $arrayToObject expects an array of {k, v} objects. |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $arrayToObject expects an array of {k, v} objects. |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/arrayToObject.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **17 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / empty arguments | {} | Error — Invalid $project :: caused by :: Expression $arrayToObject takes exactly 1 arguments. 0 were passed in. |

</details>

[Download full comparison evidence](../../downloads/operator-parity/arrayToObject.json).

<!-- END MONGO PARITY -->

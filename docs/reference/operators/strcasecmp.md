# $strcasecmp

## Definition

Compares lower-cased strings.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$strcasecmp": [ <left>, <right> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `left` | Yes | First expression in the ordered argument list. |
| `right` | Yes | Second expression in the ordered argument list. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `left` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $strcasecmp expects two strings |
| missing | Field absent | Error — $strcasecmp expects two strings |
| decimal | 2.5 | Error — $strcasecmp expects two strings |
| numeric string | "12" | -50 (int32) |
| text | "hello" | 5 (int32) |
| boolean | true | Error — $strcasecmp expects two strings |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $strcasecmp expects two strings |
| empty array | [] | Error — $strcasecmp expects two strings |
| numeric array | [1,2,3] | Error — $strcasecmp expects two strings |
| object | {"x":1} | Error — $strcasecmp expects two strings |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$strcasecmp":[]} | Error — $strcasecmp expects [string1, string2] |
| {"$strcasecmp":{"unexpected":1}} | Error — $strcasecmp expects [string1, string2] |

## Examples

Expression:
```json
{
  "$strcasecmp": [
    "CA",
    "ca"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 0 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `left[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $strcasecmp expects two strings |
| missing | Field absent | Error — $strcasecmp expects two strings |
| zero | 0 | Error — $strcasecmp expects two strings |
| negative | -2 | Error — $strcasecmp expects two strings |
| decimal | 2.5 | Error — $strcasecmp expects two strings |
| numeric string | "12" | -50 (int32) |
| text | "hello" | 5 (int32) |
| empty string | "" | -2 (int32) |
| boolean | true | Error — $strcasecmp expects two strings |
| false | false | Error — $strcasecmp expects two strings |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $strcasecmp expects two strings |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $strcasecmp expects two strings |
| empty array | [] | Error — $strcasecmp expects two strings |
| numeric array | [1,2,3] | Error — $strcasecmp expects two strings |
| mixed array | [1,null,"x",3] | Error — $strcasecmp expects two strings |
| nested array | [[1,2],[3]] | Error — $strcasecmp expects two strings |
| empty object | {} | Error — $strcasecmp expects two strings |
| object | {"x":1} | Error — $strcasecmp expects two strings |
| ISO date string | "2026-01-15T15:00:00Z" | -49 (int32) |

**Argument: `right[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $strcasecmp expects two strings |
| missing | Field absent | Error — $strcasecmp expects two strings |
| zero | 0 | Error — $strcasecmp expects two strings |
| negative | -2 | Error — $strcasecmp expects two strings |
| decimal | 2.5 | Error — $strcasecmp expects two strings |
| numeric string | "12" | 50 (int32) |
| text | "hello" | -5 (int32) |
| empty string | "" | 2 (int32) |
| boolean | true | Error — $strcasecmp expects two strings |
| false | false | Error — $strcasecmp expects two strings |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $strcasecmp expects two strings |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $strcasecmp expects two strings |
| empty array | [] | Error — $strcasecmp expects two strings |
| numeric array | [1,2,3] | Error — $strcasecmp expects two strings |
| mixed array | [1,null,"x",3] | Error — $strcasecmp expects two strings |
| nested array | [[1,2],[3]] | Error — $strcasecmp expects two strings |
| empty object | {} | Error — $strcasecmp expects two strings |
| object | {"x":1} | Error — $strcasecmp expects two strings |
| ISO date string | "2026-01-15T15:00:00Z" | 49 (int32) |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/strcasecmp.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **1 exact BSON matches**, **18 both rejected**, **22 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| left[0] / null | Error — $strcasecmp expects two strings | -1 (int32) |
| left[0] / missing | Error — $strcasecmp expects two strings | -1 (int32) |
| left[0] / zero | Error — $strcasecmp expects two strings | -1 (int32) |
| left[0] / negative | Error — $strcasecmp expects two strings | -1 (int32) |
| left[0] / decimal | Error — $strcasecmp expects two strings | -1 (int32) |
| left[0] / numeric string | -50 (int32) | -1 (int32) |
| left[0] / text | 5 (int32) | 1 (int32) |
| left[0] / empty string | -2 (int32) | -1 (int32) |
| left[0] / typed date | Error — $strcasecmp expects two strings | -1 (int32) |
| left[0] / decimal128 | Error — $strcasecmp expects two strings | -1 (int32) |
| left[0] / ISO date string | -49 (int32) | -1 (int32) |
| right[1] / null | Error — $strcasecmp expects two strings | 1 (int32) |
| right[1] / missing | Error — $strcasecmp expects two strings | 1 (int32) |
| right[1] / zero | Error — $strcasecmp expects two strings | 1 (int32) |
| right[1] / negative | Error — $strcasecmp expects two strings | 1 (int32) |
| right[1] / decimal | Error — $strcasecmp expects two strings | 1 (int32) |
| right[1] / numeric string | 50 (int32) | 1 (int32) |
| right[1] / text | -5 (int32) | -1 (int32) |
| right[1] / empty string | 2 (int32) | 1 (int32) |
| right[1] / typed date | Error — $strcasecmp expects two strings | 1 (int32) |
| right[1] / decimal128 | Error — $strcasecmp expects two strings | 1 (int32) |
| right[1] / ISO date string | 49 (int32) | 1 (int32) |

</details>

[Download full comparison evidence](../../downloads/operator-parity/strcasecmp.json).

<!-- END MONGO PARITY -->

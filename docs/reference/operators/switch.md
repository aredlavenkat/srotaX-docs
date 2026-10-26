# $switch

## Definition

Selects the first branch with a true boolean condition.

**Expression operator** · Conditional · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{
  "$switch": {
    "branches": <branches>,
    "default": <default>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `branches` | Yes | Array of objects containing `case` and `then` expressions, evaluated in order. |
| `default` | No | Result expression used when no branch matches. The current engine returns null when this is omitted. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `branches` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $switch 'branches' must be a list |
| missing | Field absent | Error — $switch 'branches' must be a list |
| decimal | 2.5 | Error — $switch 'branches' must be a list |
| numeric string | "12" | Error — $switch 'branches' must be a list |
| text | "hello" | Error — $switch 'branches' must be a list |
| boolean | true | Error — $switch 'branches' must be a list |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $switch 'branches' must be a list |
| empty array | [] | Error — $switch 'branches' must be a list |
| numeric array | [1,2,3] | Error — $switch 'branches' must be a list |
| object | {"x":1} | Error — $switch 'branches' must be a list |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$switch":[]} | Error — $switch requires a document with 'branches' and optional 'default' |
| {"$switch":{"unexpected":1}} | Error — $switch 'branches' must be a list |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `branches`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $switch 'branches' must be a list |
| missing | Field absent | Error — $switch 'branches' must be a list |
| zero | 0 | Error — $switch 'branches' must be a list |
| negative | -2 | Error — $switch 'branches' must be a list |
| decimal | 2.5 | Error — $switch 'branches' must be a list |
| numeric string | "12" | Error — $switch 'branches' must be a list |
| text | "hello" | Error — $switch 'branches' must be a list |
| empty string | "" | Error — $switch 'branches' must be a list |
| boolean | true | Error — $switch 'branches' must be a list |
| false | false | Error — $switch 'branches' must be a list |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $switch 'branches' must be a list |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $switch 'branches' must be a list |
| empty array | [] | Error — $switch 'branches' must be a list |
| numeric array | [1,2,3] | Error — $switch 'branches' must be a list |
| mixed array | [1,null,"x",3] | Error — $switch 'branches' must be a list |
| nested array | [[1,2],[3]] | Error — $switch 'branches' must be a list |
| empty object | {} | Error — $switch 'branches' must be a list |
| object | {"x":1} | Error — $switch 'branches' must be a list |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $switch 'branches' must be a list |
| omitted named argument | Argument removed | Error — $switch 'branches' must be a list |

**Argument: `default`**

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


</details>

## Verification

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/switch.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **21 exact BSON matches**, **22 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/switch.json).

<!-- END MONGO PARITY -->

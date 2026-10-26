# $ltrim

## Definition

Trims configured characters from the start of text.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$ltrim": {
    "input": <input>,
    "chars": <chars>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `chars` | No | Characters to remove from the ends of the string. If omitted, the operator uses its whitespace trimming behavior. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — $trim input must be a string |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| boolean | true | Error — $trim input must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $trim input must be a string |
| empty array | [] | Error — $trim input must be a string |
| numeric array | [1,2,3] | Error — $trim input must be a string |
| object | {"x":1} | Error — $trim input must be a string |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$ltrim":[]} | Error — $trim requires input and optional chars |
| {"$ltrim":{"unexpected":1}} | Error — $trim requires input and optional chars |

## Examples

Expression:
```json
{
  "$ltrim": {
    "input": "  hi"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "hi".

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $trim input must be a string |
| negative | -2 | Error — $trim input must be a string |
| decimal | 2.5 | Error — $trim input must be a string |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | Error — $trim input must be a string |
| false | false | Error — $trim input must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $trim input must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $trim input must be a string |
| empty array | [] | Error — $trim input must be a string |
| numeric array | [1,2,3] | Error — $trim input must be a string |
| mixed array | [1,null,"x",3] | Error — $trim input must be a string |
| nested array | [[1,2],[3]] | Error — $trim input must be a string |
| empty object | {} | Error — $trim input must be a string |
| object | {"x":1} | Error — $trim input must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | Error — $trim requires input and optional chars |

**Argument: `chars`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — $trim chars must be a string |
| negative | -2 | Error — $trim chars must be a string |
| decimal | 2.5 | Error — $trim chars must be a string |
| numeric string | "12" | "  hi" |
| text | "hello" | "  hi" |
| empty string | "" | "  hi" |
| boolean | true | Error — $trim chars must be a string |
| false | false | Error — $trim chars must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $trim chars must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $trim chars must be a string |
| empty array | [] | Error — $trim chars must be a string |
| numeric array | [1,2,3] | Error — $trim chars must be a string |
| mixed array | [1,null,"x",3] | Error — $trim chars must be a string |
| nested array | [[1,2],[3]] | Error — $trim chars must be a string |
| empty object | {} | Error — $trim chars must be a string |
| object | {"x":1} | Error — $trim chars must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | "  hi" |
| omitted named argument | Argument removed | "hi" |


</details>

## Verification

This page records **43 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/ltrim.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **14 exact BSON matches**, **29 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/ltrim.json).

<!-- END MONGO PARITY -->

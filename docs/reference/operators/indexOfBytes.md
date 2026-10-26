# $indexOfBytes

## Definition

Searches text using byte positions; bounds have known differences.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$indexOfBytes": [ <input>, <search>, <start>, <end> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `search` | Yes | Value or substring to find in the source. |
| `start` | No | Starting position or lower bound. See the syntax and examples for this operator. |
| `end` | No | Exclusive ending position or upper bound. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–4 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — Expected string. |
| missing | Field absent | Error — Expected string. |
| decimal | 2.5 | Error — Expected string. |
| numeric string | "12" | -1 (int32) |
| text | "hello" | 2 (int32) |
| boolean | true | Error — Expected string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Expected string. |
| empty array | [] | Error — Expected string. |
| numeric array | [1,2,3] | Error — Expected string. |
| object | {"x":1} | Error — Expected string. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$indexOfBytes":[]} | Error — $indexOfBytes expects [string, substring, [start], [end]] |
| {"$indexOfBytes":{"unexpected":1}} | Error — $indexOfBytes expects [string, substring, [start], [end]] |

## Examples

Expression:
```json
{
  "$indexOfBytes": [
    "hello",
    "ll"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2 (int32).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Expected string. |
| missing | Field absent | Error — Expected string. |
| zero | 0 | Error — Expected string. |
| negative | -2 | Error — Expected string. |
| decimal | 2.5 | Error — Expected string. |
| numeric string | "12" | -1 (int32) |
| text | "hello" | 2 (int32) |
| empty string | "" | -1 (int32) |
| boolean | true | Error — Expected string. |
| false | false | Error — Expected string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Expected string. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Expected string. |
| empty array | [] | Error — Expected string. |
| numeric array | [1,2,3] | Error — Expected string. |
| mixed array | [1,null,"x",3] | Error — Expected string. |
| nested array | [[1,2],[3]] | Error — Expected string. |
| empty object | {} | Error — Expected string. |
| object | {"x":1} | Error — Expected string. |
| ISO date string | "2026-01-15T15:00:00Z" | -1 (int32) |

**Argument: `search[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Expected string. |
| missing | Field absent | Error — Expected string. |
| zero | 0 | Error — Expected string. |
| negative | -2 | Error — Expected string. |
| decimal | 2.5 | Error — Expected string. |
| numeric string | "12" | -1 (int32) |
| text | "hello" | 0 (int32) |
| empty string | "" | 0 (int32) |
| boolean | true | Error — Expected string. |
| false | false | Error — Expected string. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Expected string. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Expected string. |
| empty array | [] | Error — Expected string. |
| numeric array | [1,2,3] | Error — Expected string. |
| mixed array | [1,null,"x",3] | Error — Expected string. |
| nested array | [[1,2],[3]] | Error — Expected string. |
| empty object | {} | Error — Expected string. |
| object | {"x":1} | Error — Expected string. |
| ISO date string | "2026-01-15T15:00:00Z" | -1 (int32) |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/indexOfBytes.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **9 exact BSON matches**, **30 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input[0] / null | Error — Expected string. | null |
| input[0] / missing | Error — Expected string. | null |

</details>

[Download full comparison evidence](../../downloads/operator-parity/indexOfBytes.json).

<!-- END MONGO PARITY -->

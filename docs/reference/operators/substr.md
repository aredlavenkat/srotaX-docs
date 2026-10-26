# $substr

## Definition

Extracts a substring using UTF-16 indexes.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$substr": [ <input>, <start>, <length> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `start` | Yes | Starting position or lower bound. See the syntax and examples for this operator. |
| `length` | Yes | Number of bytes or characters to return, depending on the operator. |

Arguments are positional: keep the order shown. The authoring signature accepts 3–3 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $substr expects (string, int, int) |
| missing | Field absent | Error — $substr expects (string, int, int) |
| decimal | 2.5 | Error — $substr expects (string, int, int) |
| numeric string | "12" | "2" |
| text | "hello" | "ell" |
| boolean | true | Error — $substr expects (string, int, int) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $substr expects (string, int, int) |
| empty array | [] | Error — $substr expects (string, int, int) |
| numeric array | [1,2,3] | Error — $substr expects (string, int, int) |
| object | {"x":1} | Error — $substr expects (string, int, int) |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$substr":[]} | Error — $substr requires [string, start, length] |
| {"$substr":{"unexpected":1}} | Error — $substr requires [string, start, length] |

## Examples

Expression:
```json
{
  "$substr": [
    "hello",
    1,
    3
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "ell".

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $substr expects (string, int, int) |
| missing | Field absent | Error — $substr expects (string, int, int) |
| zero | 0 | Error — $substr expects (string, int, int) |
| negative | -2 | Error — $substr expects (string, int, int) |
| decimal | 2.5 | Error — $substr expects (string, int, int) |
| numeric string | "12" | "2" |
| text | "hello" | "ell" |
| empty string | "" | "" |
| boolean | true | Error — $substr expects (string, int, int) |
| false | false | Error — $substr expects (string, int, int) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $substr expects (string, int, int) |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $substr expects (string, int, int) |
| empty array | [] | Error — $substr expects (string, int, int) |
| numeric array | [1,2,3] | Error — $substr expects (string, int, int) |
| mixed array | [1,null,"x",3] | Error — $substr expects (string, int, int) |
| nested array | [[1,2],[3]] | Error — $substr expects (string, int, int) |
| empty object | {} | Error — $substr expects (string, int, int) |
| object | {"x":1} | Error — $substr expects (string, int, int) |
| ISO date string | "2026-01-15T15:00:00Z" | "026" |

**Argument: `start[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $substr expects (string, int, int) |
| missing | Field absent | Error — $substr expects (string, int, int) |
| zero | 0 | "hel" |
| negative | -2 | "" |
| decimal | 2.5 | "llo" |
| numeric string | "12" | Error — $substr expects (string, int, int) |
| text | "hello" | Error — $substr expects (string, int, int) |
| empty string | "" | Error — $substr expects (string, int, int) |
| boolean | true | Error — $substr expects (string, int, int) |
| false | false | Error — $substr expects (string, int, int) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $substr expects (string, int, int) |
| decimal128 | {"$numberDecimal":"1.25"} | "ell" |
| empty array | [] | Error — $substr expects (string, int, int) |
| numeric array | [1,2,3] | Error — $substr expects (string, int, int) |
| mixed array | [1,null,"x",3] | Error — $substr expects (string, int, int) |
| nested array | [[1,2],[3]] | Error — $substr expects (string, int, int) |
| empty object | {} | Error — $substr expects (string, int, int) |
| object | {"x":1} | Error — $substr expects (string, int, int) |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $substr expects (string, int, int) |

**Argument: `length[2]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $substr expects (string, int, int) |
| missing | Field absent | Error — $substr expects (string, int, int) |
| zero | 0 | "" |
| negative | -2 | "" |
| decimal | 2.5 | "el" |
| numeric string | "12" | Error — $substr expects (string, int, int) |
| text | "hello" | Error — $substr expects (string, int, int) |
| empty string | "" | Error — $substr expects (string, int, int) |
| boolean | true | Error — $substr expects (string, int, int) |
| false | false | Error — $substr expects (string, int, int) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $substr expects (string, int, int) |
| decimal128 | {"$numberDecimal":"1.25"} | "e" |
| empty array | [] | Error — $substr expects (string, int, int) |
| numeric array | [1,2,3] | Error — $substr expects (string, int, int) |
| mixed array | [1,null,"x",3] | Error — $substr expects (string, int, int) |
| nested array | [[1,2],[3]] | Error — $substr expects (string, int, int) |
| empty object | {} | Error — $substr expects (string, int, int) |
| object | {"x":1} | Error — $substr expects (string, int, int) |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $substr expects (string, int, int) |


</details>

## Verification

This page records **60 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/substr.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **11 exact BSON matches**, **40 both rejected**, **9 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input[0] / null | Error — $substr expects (string, int, int) | "" |
| input[0] / missing | Error — $substr expects (string, int, int) | "" |
| input[0] / zero | Error — $substr expects (string, int, int) | "" |
| input[0] / negative | Error — $substr expects (string, int, int) | "2" |
| input[0] / decimal | Error — $substr expects (string, int, int) | ".5" |
| input[0] / typed date | Error — $substr expects (string, int, int) | "026" |
| input[0] / decimal128 | Error — $substr expects (string, int, int) | ".25" |
| start[1] / negative | "" | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: $substrBytes:  starting index must be non-negative (got: -2) |
| length[2] / negative | "" | "ello" |

</details>

[Download full comparison evidence](../../downloads/operator-parity/substr.json).

<!-- END MONGO PARITY -->

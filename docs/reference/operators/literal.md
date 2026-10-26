# $literal

## Definition

Returns a value without evaluating it.

**Expression operator** · Types and conversion · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$literal": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Value to return without evaluating field paths or nested operators.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| boolean | true | true |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| object | {"x":1} | {"x":1} |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$literal":[]} | [] |
| {"$literal":{"unexpected":1}} | {"unexpected":1} |

## Examples

Expression:
```json
{
  "$literal": {
    "x": "$field"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {"x":"$field"}.

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | true |
| false | false | false |
| typed date | null | {'$numberLong': '1768489200000'} (date) |
| decimal128 | null | 1.25 (decimal128) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | null | {} |
| object | null | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |


</details>

## Verification

This page records **21 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/literal.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **21 exact BSON matches**, **0 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/literal.json).

<!-- END MONGO PARITY -->

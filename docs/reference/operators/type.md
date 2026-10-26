# $type

## Definition

Returns the BSON-style type name of a value.

**Expression operator** · Types and conversion · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$type": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | "null" |
| missing | Field absent | "missing" |
| decimal | 2.5 | "double" |
| numeric string | "12" | "string" |
| text | "hello" | "string" |
| boolean | true | "bool" |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "date" |
| empty array | [] | "array" |
| numeric array | [1,2,3] | "array" |
| object | {"x":1} | "object" |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$type":[]} | Error — $type requires one argument |
| {"$type":{"unexpected":1}} | "object" |

## Examples

Expression:
```json
{
  "$type": "hello"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "string".

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | "null" |
| missing | Field absent | "missing" |
| zero | 0 | "int" |
| negative | -2 | "int" |
| decimal | 2.5 | "double" |
| numeric string | "12" | "string" |
| text | "hello" | "string" |
| empty string | "" | "string" |
| boolean | true | "bool" |
| false | false | "bool" |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | "date" |
| decimal128 | {"$numberDecimal":"1.25"} | "decimal" |
| empty array | [] | "array" |
| numeric array | [1,2,3] | "array" |
| mixed array | [1,null,"x",3] | "array" |
| nested array | [[1,2],[3]] | "array" |
| empty object | {} | "object" |
| object | {"x":1} | "object" |
| ISO date string | "2026-01-15T15:00:00Z" | "string" |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/type.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **21 exact BSON matches**, **1 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/type.json).

<!-- END MONGO PARITY -->

# $regexMatch

## Definition

Tests whether a Java regular expression matches text.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$regexMatch": {
    "input": <input>,
    "regex": <regex>,
    "options": <options>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `regex` | Yes | Regular-expression pattern to search for. |
| `options` | No | Regex option string. See Supported values below. |

## Supported values

`options` accepts any combination of `i` (case-insensitive), `m` (multiline anchors), `s` (dot matches newlines), and `x` (ignore pattern whitespace/comments). Omit it or use `""` for no flags. Patterns use Java regular-expression behavior.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| decimal | 2.5 | Error — $regexMatch input must be a string |
| numeric string | "12" | false |
| text | "hello" | false |
| boolean | true | Error — $regexMatch input must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $regexMatch input must be a string |
| empty array | [] | Error — $regexMatch input must be a string |
| numeric array | [1,2,3] | Error — $regexMatch input must be a string |
| object | {"x":1} | Error — $regexMatch input must be a string |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$regexMatch":[]} | Error — $regexMatch requires input, regex and optional options |
| {"$regexMatch":{"unexpected":1}} | Error — $regexMatch requires input, regex and optional options |

## Examples

Expression:
```json
{
  "$regexMatch": {
    "input": "abc",
    "regex": "ab"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** true.

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| zero | 0 | Error — $regexMatch input must be a string |
| negative | -2 | Error — $regexMatch input must be a string |
| decimal | 2.5 | Error — $regexMatch input must be a string |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | false |
| boolean | true | Error — $regexMatch input must be a string |
| false | false | Error — $regexMatch input must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $regexMatch input must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $regexMatch input must be a string |
| empty array | [] | Error — $regexMatch input must be a string |
| numeric array | [1,2,3] | Error — $regexMatch input must be a string |
| mixed array | [1,null,"x",3] | Error — $regexMatch input must be a string |
| nested array | [[1,2],[3]] | Error — $regexMatch input must be a string |
| empty object | {} | Error — $regexMatch input must be a string |
| object | {"x":1} | Error — $regexMatch input must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | false |
| omitted named argument | Argument removed | Error — $regexMatch requires input, regex and optional options |

**Argument: `regex`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| zero | 0 | Error — $regexMatch regex must be a string or BSON regex |
| negative | -2 | Error — $regexMatch regex must be a string or BSON regex |
| decimal | 2.5 | Error — $regexMatch regex must be a string or BSON regex |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | true |
| boolean | true | Error — $regexMatch regex must be a string or BSON regex |
| false | false | Error — $regexMatch regex must be a string or BSON regex |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $regexMatch regex must be a string or BSON regex |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $regexMatch regex must be a string or BSON regex |
| empty array | [] | Error — $regexMatch regex must be a string or BSON regex |
| numeric array | [1,2,3] | Error — $regexMatch regex must be a string or BSON regex |
| mixed array | [1,null,"x",3] | Error — $regexMatch regex must be a string or BSON regex |
| nested array | [[1,2],[3]] | Error — $regexMatch regex must be a string or BSON regex |
| empty object | {} | Error — $regexMatch regex must be a string or BSON regex |
| object | {"x":1} | Error — $regexMatch regex must be a string or BSON regex |
| ISO date string | "2026-01-15T15:00:00Z" | false |
| omitted named argument | Argument removed | Error — $regexMatch requires input, regex and optional options |

**Argument: `options`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | true |
| missing | Field absent | true |
| zero | 0 | Error — $regexMatch options must be a string |
| negative | -2 | Error — $regexMatch options must be a string |
| decimal | 2.5 | Error — $regexMatch options must be a string |
| numeric string | "12" | Error — Unsupported regex option: 1 |
| text | "hello" | Error — Unsupported regex option: h |
| empty string | "" | true |
| boolean | true | Error — $regexMatch options must be a string |
| false | false | Error — $regexMatch options must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $regexMatch options must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $regexMatch options must be a string |
| empty array | [] | Error — $regexMatch options must be a string |
| numeric array | [1,2,3] | Error — $regexMatch options must be a string |
| mixed array | [1,null,"x",3] | Error — $regexMatch options must be a string |
| nested array | [[1,2],[3]] | Error — $regexMatch options must be a string |
| empty object | {} | Error — $regexMatch options must be a string |
| object | {"x":1} | Error — $regexMatch options must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Unsupported regex option: 2 |
| omitted named argument | Argument removed | true |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$regexMatch": {
    "input": "a",
    "regex": "["
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error — Unclosed character class near index 0 [ ^.

</details>

## Verification

This page records **64 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/regexMatch.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **17 exact BSON matches**, **47 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/regexMatch.json).

<!-- END MONGO PARITY -->

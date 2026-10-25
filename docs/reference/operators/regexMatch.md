# $regexMatch

Tests whether a Java regular expression matches text.

**Category:** Text. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |
| `regex` | STRING | Yes | Expression evaluated against the input |
| `options` | STRING | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 3.

Declared result types: **BOOLEAN**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| zero | 0 | Error: IllegalArgumentException — $regexMatch input must be a string |
| negative | -2 | Error: IllegalArgumentException — $regexMatch input must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — $regexMatch input must be a string |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | false |
| boolean | true | Error: IllegalArgumentException — $regexMatch input must be a string |
| false | false | Error: IllegalArgumentException — $regexMatch input must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $regexMatch input must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $regexMatch input must be a string |
| empty array | [] | Error: IllegalArgumentException — $regexMatch input must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $regexMatch input must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $regexMatch input must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $regexMatch input must be a string |
| empty object | {} | Error: IllegalArgumentException — $regexMatch input must be a string |
| object | {"x":1} | Error: IllegalArgumentException — $regexMatch input must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | false |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $regexMatch requires input, regex and optional options |

### Argument: `regex`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | false |
| missing | Field absent | false |
| zero | 0 | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| negative | -2 | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| decimal | 2.5 | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | true |
| boolean | true | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| false | false | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| empty array | [] | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| empty object | {} | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| object | {"x":1} | Error: IllegalArgumentException — $regexMatch regex must be a string or BSON regex |
| ISO date string | "2026-01-15T15:00:00Z" | false |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $regexMatch requires input, regex and optional options |

### Argument: `options`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | true |
| missing | Field absent | true |
| zero | 0 | Error: IllegalArgumentException — $regexMatch options must be a string |
| negative | -2 | Error: IllegalArgumentException — $regexMatch options must be a string |
| decimal | 2.5 | Error: IllegalArgumentException — $regexMatch options must be a string |
| numeric string | "12" | Error: IllegalArgumentException — Unsupported regex option: 1 |
| text | "hello" | Error: IllegalArgumentException — Unsupported regex option: h |
| empty string | "" | true |
| boolean | true | Error: IllegalArgumentException — $regexMatch options must be a string |
| false | false | Error: IllegalArgumentException — $regexMatch options must be a string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $regexMatch options must be a string |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $regexMatch options must be a string |
| empty array | [] | Error: IllegalArgumentException — $regexMatch options must be a string |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $regexMatch options must be a string |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $regexMatch options must be a string |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $regexMatch options must be a string |
| empty object | {} | Error: IllegalArgumentException — $regexMatch options must be a string |
| object | {"x":1} | Error: IllegalArgumentException — $regexMatch options must be a string |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Unsupported regex option: 2 |
| omitted named argument | Argument removed | true |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$regexMatch":[]} | Error: IllegalArgumentException — $regexMatch requires input, regex and optional options |
| {"$regexMatch":{"unexpected":1}} | Error: IllegalArgumentException — $regexMatch requires input, regex and optional options |

## Additional boundary examples

<details>
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

**SrotaX:** Error: PatternSyntaxException — Unclosed character class near index 0 [ ^.

</details>

## Scope and reproducibility

This page records **64 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/regexMatch.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **17 exact BSON matches**, **47 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/regexMatch.json).

<!-- END MONGO PARITY -->

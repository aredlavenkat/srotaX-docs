# $convert

Converts input to a named target type with optional fallbacks.

**Category:** Types and conversion. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ANY | Yes | Expression evaluated against the input |
| `to` | INT, STRING | Yes | Expression evaluated against the input |
| `onError` | ANY | No | Expression evaluated against the input |
| `onNull` | ANY | No | Expression evaluated against the input |

Argument count: minimum 2; maximum 4.

Declared result types: **ANY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

Supported `to` target names: `array`, `object`, `bool`, `double`, `string`, `date`, `int`, `long`, `decimal`. Array/object conversion parses a JSON string with the matching root. `onError` supplies a conversion-failure fallback; `onNull` supplies a null/missing fallback. Native ObjectId and UUID authoring remain outside the supported SrotaX scope.

## Example

Expression:
```json
{
  "$convert": {
    "input": "12",
    "to": "int"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 12 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2 (int32) |
| numeric string | "12" | 12 (int32) |
| text | "hello" | Error: IllegalArgumentException — $convert failed for target int |
| empty string | "" | Error: IllegalArgumentException — $convert failed for target int |
| boolean | true | 1 (int32) |
| false | false | 0 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $convert failed for target int |
| decimal128 | {"$numberDecimal":"1.25"} | 1 (int32) |
| empty array | [] | Error: IllegalArgumentException — $convert failed for target int |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $convert failed for target int |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $convert failed for target int |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $convert failed for target int |
| empty object | {} | Error: IllegalArgumentException — $convert failed for target int |
| object | {"x":1} | Error: IllegalArgumentException — $convert failed for target int |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $convert failed for target int |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $convert requires input and to |

### Argument: `to`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error: IllegalArgumentException — Unsupported BSON type code |
| negative | -2 | Error: IllegalArgumentException — Unsupported BSON type code |
| decimal | 2.5 | "12" |
| numeric string | "12" | Error: IllegalArgumentException — $convert failed for target 12 |
| text | "hello" | Error: IllegalArgumentException — $convert failed for target hello |
| empty string | "" | Error: IllegalArgumentException — $convert failed for target  |
| boolean | true | Error: IllegalArgumentException — $convert failed for target true |
| false | false | Error: IllegalArgumentException — $convert failed for target false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $convert failed for target Thu Jan 15 10:00:00 EST 2026 |
| decimal128 | {"$numberDecimal":"1.25"} | 12.0 (double) |
| empty array | [] | Error: IllegalArgumentException — $convert failed for target [] |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $convert failed for target [1, 2, 3] |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $convert failed for target [1, null, x, 3] |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $convert failed for target [[1, 2], [3]] |
| empty object | {} | Error: IllegalArgumentException — $convert failed for target Document{{}} |
| object | {"x":1} | Error: IllegalArgumentException — $convert failed for target Document{{x=1}} |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $convert failed for target 2026-01-15T15:00:00Z |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $convert requires input and to |

### Argument: `onError`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 12 (int32) |
| missing | Field absent | 12 (int32) |
| zero | 0 | 12 (int32) |
| negative | -2 | 12 (int32) |
| decimal | 2.5 | 12 (int32) |
| numeric string | "12" | 12 (int32) |
| text | "hello" | 12 (int32) |
| empty string | "" | 12 (int32) |
| boolean | true | 12 (int32) |
| false | false | 12 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 12 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | 12 (int32) |
| empty array | [] | 12 (int32) |
| numeric array | [1,2,3] | 12 (int32) |
| mixed array | [1,null,"x",3] | 12 (int32) |
| nested array | [[1,2],[3]] | 12 (int32) |
| empty object | {} | 12 (int32) |
| object | {"x":1} | 12 (int32) |
| ISO date string | "2026-01-15T15:00:00Z" | 12 (int32) |
| omitted named argument | Argument removed | 12 (int32) |

### Argument: `onNull`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | 12 (int32) |
| missing | Field absent | 12 (int32) |
| zero | 0 | 12 (int32) |
| negative | -2 | 12 (int32) |
| decimal | 2.5 | 12 (int32) |
| numeric string | "12" | 12 (int32) |
| text | "hello" | 12 (int32) |
| empty string | "" | 12 (int32) |
| boolean | true | 12 (int32) |
| false | false | 12 (int32) |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 12 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | 12 (int32) |
| empty array | [] | 12 (int32) |
| numeric array | [1,2,3] | 12 (int32) |
| mixed array | [1,null,"x",3] | 12 (int32) |
| nested array | [[1,2],[3]] | 12 (int32) |
| empty object | {} | 12 (int32) |
| object | {"x":1} | 12 (int32) |
| ISO date string | "2026-01-15T15:00:00Z" | 12 (int32) |
| omitted named argument | Argument removed | 12 (int32) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$convert":[]} | Error: IllegalArgumentException — $convert requires input and to |
| {"$convert":{"unexpected":1}} | Error: IllegalArgumentException — $convert requires input and to |

## Additional boundary examples

<details>
<summary>Show 40 tested examples</summary>

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "[1,2147483648,9223372036854775808,1.5,null,{\"x\":true}]"
}
```

**SrotaX:** [1,2147483648,9.223372036854776e+18,1.5,null,{"x":true}].

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": null
}
```

**SrotaX:** null.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": ""
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "null"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "123"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "true"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "[]"
}
```

**SrotaX:** [].

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "{}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "[1,]"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "{\"x\":1,}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "/*x*/ []"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "[] {}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "{\"x\\u0000\":1}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "{\"x\":\"a\\u0000b\"}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": "[1e400]"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": 123
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": []
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "array"
  }
}
```

Input:
```json
{
  "value": {}
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target array.

Expression:
```json
{
  "$convert": {
    "input": "broken",
    "to": "array",
    "onError": "fallback"
  }
}
```

Input:
```json
{}
```

**SrotaX:** "fallback".

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "{\"a\":1,\"a\":2,\"nested\":{\"$date\":\"2020\"},\"x\":[1,2]}"
}
```

**SrotaX:** {"a":2,"nested":{"$date":"2020"},"x":[1,2]}.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": null
}
```

**SrotaX:** null.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": ""
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "null"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "123"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "true"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "[]"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "{}"
}
```

**SrotaX:** {}.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "[1,]"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "{\"x\":1,}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "/*x*/ []"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "[] {}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "{\"x\\u0000\":1}"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "{\"x\":\"a\\u0000b\"}"
}
```

**SrotaX:** {"x":"a\u0000b"}.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": "[1e400]"
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": 123
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": []
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "$value",
    "to": "object"
  }
}
```

Input:
```json
{
  "value": {}
}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target object.

Expression:
```json
{
  "$convert": {
    "input": "broken",
    "to": "object",
    "onError": "fallback"
  }
}
```

Input:
```json
{}
```

**SrotaX:** "fallback".

Expression:
```json
{
  "$convert": {
    "input": {
      "a": 1
    },
    "to": {
      "type": "binData",
      "subtype": 0
    }
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target {type=binData, subtype=0}.

Expression:
```json
{
  "$convert": {
    "input": "ff",
    "to": "int",
    "base": 16
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error: IllegalArgumentException — $convert failed for target int.

</details>

## Scope and reproducibility

This page records **123 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/convert.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **61 exact BSON matches**, **58 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| to / decimal | "12" | Error: FailedToParse — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: In $convert, numeric 'to' argument is not an integer |
| to / decimal128 | 12.0 (double) | Error: FailedToParse — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: In $convert, numeric 'to' argument is not an integer |
| all / boundary example | Error: IllegalArgumentException — $convert failed for target {type=binData, subtype=0} | {"$binary":{"base64":"DAAAABBhAAEAAAAA","subType":"00"}} |
| all / boundary example | Error: IllegalArgumentException — $convert failed for target int | 255 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/convert.json).

<!-- END MONGO PARITY -->

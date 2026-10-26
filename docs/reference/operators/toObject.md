# $toObject

## Definition

Parses a strict JSON string into an object.

**Expression operator** · Types and conversion · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$toObject": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

String containing a JSON object. Existing object values are rejected; this operator parses strings.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — Container conversion requires a JSON string |
| numeric string | "12" | Error — JSON root must be object |
| text | "hello" | Error — Invalid JSON container |
| boolean | true | Error — Container conversion requires a JSON string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Container conversion requires a JSON string |
| empty array | [] | Error — Container conversion requires a JSON string |
| numeric array | [1,2,3] | Error — Container conversion requires a JSON string |
| object | {"x":1} | Error — Container conversion requires a JSON string |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$toObject":[]} | Error — Container conversion requires a JSON string |
| {"$toObject":{"unexpected":1}} | Error — Container conversion requires a JSON string |

## Examples

Expression:
```json
{
  "$toObject": "{\"name\":\"Alex\"}"
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {"name":"Alex"}.

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — Container conversion requires a JSON string |
| negative | -2 | Error — Container conversion requires a JSON string |
| decimal | 2.5 | Error — Container conversion requires a JSON string |
| numeric string | "12" | Error — JSON root must be object |
| text | "hello" | Error — Invalid JSON container |
| empty string | "" | Error — Invalid JSON container |
| boolean | true | Error — Container conversion requires a JSON string |
| false | false | Error — Container conversion requires a JSON string |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Container conversion requires a JSON string |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Container conversion requires a JSON string |
| empty array | [] | Error — Container conversion requires a JSON string |
| numeric array | [1,2,3] | Error — Container conversion requires a JSON string |
| mixed array | [1,null,"x",3] | Error — Container conversion requires a JSON string |
| nested array | [[1,2],[3]] | Error — Container conversion requires a JSON string |
| empty object | {} | Error — Container conversion requires a JSON string |
| object | {"x":1} | Error — Container conversion requires a JSON string |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Invalid JSON container |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 19 tested examples</summary>

Expression:
```json
{
  "$toObject": "$value"
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
  "$toObject": "$value"
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
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": ""
}
```

**SrotaX:** Error — Invalid JSON container.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "null"
}
```

**SrotaX:** Error — JSON root must be object.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "123"
}
```

**SrotaX:** Error — JSON root must be object.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "true"
}
```

**SrotaX:** Error — JSON root must be object.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "[]"
}
```

**SrotaX:** Error — JSON root must be object.

Expression:
```json
{
  "$toObject": "$value"
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
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "[1,]"
}
```

**SrotaX:** Error — Invalid JSON container.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "{\"x\":1,}"
}
```

**SrotaX:** Error — Invalid JSON container.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "/*x*/ []"
}
```

**SrotaX:** Error — Invalid JSON container.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "[] {}"
}
```

**SrotaX:** Error — Invalid JSON container.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "{\"x\\u0000\":1}"
}
```

**SrotaX:** Error — JSON field names cannot contain null bytes.

Expression:
```json
{
  "$toObject": "$value"
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
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": "[1e400]"
}
```

**SrotaX:** Error — JSON root must be object.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": 123
}
```

**SrotaX:** Error — Container conversion requires a JSON string.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": []
}
```

**SrotaX:** Error — Container conversion requires a JSON string.

Expression:
```json
{
  "$toObject": "$value"
}
```

Input:
```json
{
  "value": {}
}
```

**SrotaX:** Error — Container conversion requires a JSON string.

Expression:
```json
{
  "$toObject": "$missing"
}
```

Input:
```json
{}
```

**SrotaX:** null.

</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/toObject.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **8 exact BSON matches**, **33 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/toObject.json).

<!-- END MONGO PARITY -->

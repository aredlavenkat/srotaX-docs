# $function

## Definition

Executes a JavaScript function in a restricted GraalJS context.

**Expression operator** · Advanced · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{
  "$function": {
    "body": <body>,
    "args": <args>,
    "lang": <lang>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `body` | Yes | Literal function body understood by the engine function implementation. |
| `args` | Yes | Array of expressions passed as function arguments. |
| `lang` | Yes | Literal function-language selector. |

## Supported values

`lang` must be `"js"` (case-insensitive). `body` is a JavaScript function string, for example `"function(x) { return x + 1; }"`. Arguments are evaluated before invocation. The engine applies a two-second execution timeout.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `body` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | {"body":null,"args":[1],"lang":"js"} | Error — $function 'body' must be a JavaScript function body |
| decimal | {"body":2.5,"args":[1],"lang":"js"} | Error — $function 'body' must be a JavaScript function body |
| numeric string | {"body":"12","args":[1],"lang":"js"} | Error — JavaScript function execution failed |
| text | {"body":"hello","args":[1],"lang":"js"} | Error — JavaScript function execution failed |
| boolean | {"body":true,"args":[1],"lang":"js"} | Error — $function 'body' must be a JavaScript function body |
| typed date | {"body":{"$date":"2026-01-15T15:00:00Z"},"args":[1],"lang":"js"} | Error — $function 'body' must be a JavaScript function body |
| empty array | {"body":[],"args":[1],"lang":"js"} | Error — $function 'body' must be a JavaScript function body |
| numeric array | {"body":[1,2,3],"args":[1],"lang":"js"} | Error — $function 'body' must be a JavaScript function body |
| object | {"body":{"x":1},"args":[1],"lang":"js"} | Error — $function 'body' must be a JavaScript function body |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$function":[]} | Error — $function expects a document with 'body', 'args', and 'lang' |
| {"$function":{"unexpected":1}} | Error — $function 'lang' must be specified and set to 'js' |

## Examples

Expression:
```json
{
  "$function": {
    "body": "function(a) { return a + 1; }",
    "args": [
      1
    ],
    "lang": "js"
  }
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

**Argument: `body`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $function 'body' must be a JavaScript function body |
| zero | 0 | Error — $function 'body' must be a JavaScript function body |
| negative | -2 | Error — $function 'body' must be a JavaScript function body |
| decimal | 2.5 | Error — $function 'body' must be a JavaScript function body |
| numeric string | "12" | Error — JavaScript function execution failed |
| text | "hello" | Error — JavaScript function execution failed |
| empty string | "" | Error — JavaScript function execution failed |
| boolean | true | Error — $function 'body' must be a JavaScript function body |
| false | false | Error — $function 'body' must be a JavaScript function body |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $function 'body' must be a JavaScript function body |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $function 'body' must be a JavaScript function body |
| empty array | [] | Error — $function 'body' must be a JavaScript function body |
| numeric array | [1,2,3] | Error — $function 'body' must be a JavaScript function body |
| mixed array | [1,null,"x",3] | Error — $function 'body' must be a JavaScript function body |
| nested array | [[1,2],[3]] | Error — $function 'body' must be a JavaScript function body |
| empty object | {} | Error — $function 'body' must be a JavaScript function body |
| object | {"x":1} | Error — $function 'body' must be a JavaScript function body |
| ISO date string | "2026-01-15T15:00:00Z" | Error — JavaScript function execution failed |
| omitted named argument | Argument removed | Error — $function 'body' must be a JavaScript function body |

**Argument: `args`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $function 'args' must be an array |
| missing | Field absent | Error — $function 'args' must be an array |
| zero | 0 | Error — $function 'args' must be an array |
| negative | -2 | Error — $function 'args' must be an array |
| decimal | 2.5 | Error — $function 'args' must be an array |
| numeric string | "12" | Error — $function 'args' must be an array |
| text | "hello" | Error — $function 'args' must be an array |
| empty string | "" | Error — $function 'args' must be an array |
| boolean | true | Error — $function 'args' must be an array |
| false | false | Error — $function 'args' must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $function 'args' must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $function 'args' must be an array |
| empty array | [] | Error — $function 'args' must be an array |
| numeric array | [1,2,3] | Error — $function 'args' must be an array |
| mixed array | [1,null,"x",3] | Error — $function 'args' must be an array |
| nested array | [[1,2],[3]] | Error — $function 'args' must be an array |
| empty object | {} | Error — $function 'args' must be an array |
| object | {"x":1} | Error — $function 'args' must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $function 'args' must be an array |
| omitted named argument | Argument removed | Error — $function 'args' must be an array |

**Argument: `lang`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $function 'lang' must be specified and set to 'js' |
| zero | 0 | Error — $function 'lang' must be specified and set to 'js' |
| negative | -2 | Error — $function 'lang' must be specified and set to 'js' |
| decimal | 2.5 | Error — $function 'lang' must be specified and set to 'js' |
| numeric string | "12" | Error — $function 'lang' must be specified and set to 'js' |
| text | "hello" | Error — $function 'lang' must be specified and set to 'js' |
| empty string | "" | Error — $function 'lang' must be specified and set to 'js' |
| boolean | true | Error — $function 'lang' must be specified and set to 'js' |
| false | false | Error — $function 'lang' must be specified and set to 'js' |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $function 'lang' must be specified and set to 'js' |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $function 'lang' must be specified and set to 'js' |
| empty array | [] | Error — $function 'lang' must be specified and set to 'js' |
| numeric array | [1,2,3] | Error — $function 'lang' must be specified and set to 'js' |
| mixed array | [1,null,"x",3] | Error — $function 'lang' must be specified and set to 'js' |
| nested array | [[1,2],[3]] | Error — $function 'lang' must be specified and set to 'js' |
| empty object | {} | Error — $function 'lang' must be specified and set to 'js' |
| object | {"x":1} | Error — $function 'lang' must be specified and set to 'js' |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $function 'lang' must be specified and set to 'js' |
| omitted named argument | Argument removed | Error — $function 'lang' must be specified and set to 'js' |


</details>

## Verification

This page records **61 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/function.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **0 exact BSON matches**, **55 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 2 (int32) | 2.0 (double) |
| body / numeric string | Error — JavaScript function execution failed | 12.0 (double) |
| args / empty array | Error — $function 'args' must be an array | NaN (double) |
| args / numeric array | Error — $function 'args' must be an array | 2.0 (double) |
| args / mixed array | Error — $function 'args' must be an array | 2.0 (double) |
| args / nested array | Error — $function 'args' must be an array | "1,21" |

</details>

[Download full comparison evidence](../../downloads/operator-parity/function.json).

<!-- END MONGO PARITY -->

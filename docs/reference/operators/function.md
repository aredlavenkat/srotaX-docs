# $function

Executes a JavaScript function in a restricted GraalJS context.

**Category:** Advanced. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `body` | STRING | Yes | Literal configuration |
| `args` | ARRAY | Yes | Expression evaluated against the input |
| `lang` | STRING | Yes | Literal configuration |

Argument count: minimum 3; maximum 3.

Declared result types: **ANY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `body`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| zero | 0 | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| negative | -2 | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| decimal | 2.5 | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| numeric string | "12" | Error: RuntimeException — JavaScript function execution failed |
| text | "hello" | Error: RuntimeException — JavaScript function execution failed |
| empty string | "" | Error: RuntimeException — JavaScript function execution failed |
| boolean | true | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| false | false | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| empty array | [] | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| empty object | {} | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| object | {"x":1} | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |
| ISO date string | "2026-01-15T15:00:00Z" | Error: RuntimeException — JavaScript function execution failed |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $function 'body' must be a JavaScript function body |

### Argument: `args`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $function 'args' must be an array |
| missing | Field absent | Error: IllegalArgumentException — $function 'args' must be an array |
| zero | 0 | Error: IllegalArgumentException — $function 'args' must be an array |
| negative | -2 | Error: IllegalArgumentException — $function 'args' must be an array |
| decimal | 2.5 | Error: IllegalArgumentException — $function 'args' must be an array |
| numeric string | "12" | Error: IllegalArgumentException — $function 'args' must be an array |
| text | "hello" | Error: IllegalArgumentException — $function 'args' must be an array |
| empty string | "" | Error: IllegalArgumentException — $function 'args' must be an array |
| boolean | true | Error: IllegalArgumentException — $function 'args' must be an array |
| false | false | Error: IllegalArgumentException — $function 'args' must be an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $function 'args' must be an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $function 'args' must be an array |
| empty array | [] | Error: IllegalArgumentException — $function 'args' must be an array |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $function 'args' must be an array |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $function 'args' must be an array |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $function 'args' must be an array |
| empty object | {} | Error: IllegalArgumentException — $function 'args' must be an array |
| object | {"x":1} | Error: IllegalArgumentException — $function 'args' must be an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $function 'args' must be an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $function 'args' must be an array |

### Argument: `lang`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| zero | 0 | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| negative | -2 | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| decimal | 2.5 | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| numeric string | "12" | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| text | "hello" | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| empty string | "" | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| boolean | true | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| false | false | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| empty array | [] | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| empty object | {} | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| object | {"x":1} | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$function":[]} | Error: IllegalArgumentException — $function expects a document with 'body', 'args', and 'lang' |
| {"$function":{"unexpected":1}} | Error: IllegalArgumentException — $function 'lang' must be specified and set to 'js' |

## Scope and reproducibility

This page records **61 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/function.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **0 exact BSON matches**, **55 both rejected**, **6 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 2 (int32) | 2.0 (double) |
| body / numeric string | Error: RuntimeException — JavaScript function execution failed | 12.0 (double) |
| args / empty array | Error: IllegalArgumentException — $function 'args' must be an array | NaN (double) |
| args / numeric array | Error: IllegalArgumentException — $function 'args' must be an array | 2.0 (double) |
| args / mixed array | Error: IllegalArgumentException — $function 'args' must be an array | 2.0 (double) |
| args / nested array | Error: IllegalArgumentException — $function 'args' must be an array | "1,21" |

[Download full comparison evidence](../../downloads/operator-parity/function.json).

<!-- END MONGO PARITY -->

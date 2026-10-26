# $split

## Definition

Splits text using a Java regular-expression delimiter.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{ "$split": [ <input>, <delimiter> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `delimiter` | Yes | String separating the output parts. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $split arguments must be strings. |
| missing | Field absent | Error — $split arguments must be strings. |
| decimal | 2.5 | Error — $split arguments must be strings. |
| numeric string | "12" | ["12"] |
| text | "hello" | ["hello"] |
| boolean | true | Error — $split arguments must be strings. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $split arguments must be strings. |
| empty array | [] | Error — $split arguments must be strings. |
| numeric array | [1,2,3] | Error — $split arguments must be strings. |
| object | {"x":1} | Error — $split arguments must be strings. |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$split":[]} | Error — $split requires [string, delimiter] |
| {"$split":{"unexpected":1}} | Error — $split requires [string, delimiter] |

## Examples

Expression:
```json
{
  "$split": [
    "a,b",
    ","
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** ["a","b"].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $split arguments must be strings. |
| missing | Field absent | Error — $split arguments must be strings. |
| zero | 0 | Error — $split arguments must be strings. |
| negative | -2 | Error — $split arguments must be strings. |
| decimal | 2.5 | Error — $split arguments must be strings. |
| numeric string | "12" | ["12"] |
| text | "hello" | ["hello"] |
| empty string | "" | [""] |
| boolean | true | Error — $split arguments must be strings. |
| false | false | Error — $split arguments must be strings. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $split arguments must be strings. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $split arguments must be strings. |
| empty array | [] | Error — $split arguments must be strings. |
| numeric array | [1,2,3] | Error — $split arguments must be strings. |
| mixed array | [1,null,"x",3] | Error — $split arguments must be strings. |
| nested array | [[1,2],[3]] | Error — $split arguments must be strings. |
| empty object | {} | Error — $split arguments must be strings. |
| object | {"x":1} | Error — $split arguments must be strings. |
| ISO date string | "2026-01-15T15:00:00Z" | ["2026-01-15T15:00:00Z"] |

**Argument: `delimiter[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $split arguments must be strings. |
| missing | Field absent | Error — $split arguments must be strings. |
| zero | 0 | Error — $split arguments must be strings. |
| negative | -2 | Error — $split arguments must be strings. |
| decimal | 2.5 | Error — $split arguments must be strings. |
| numeric string | "12" | ["a,b"] |
| text | "hello" | ["a,b"] |
| empty string | "" | Error — $split delimiter must not be empty |
| boolean | true | Error — $split arguments must be strings. |
| false | false | Error — $split arguments must be strings. |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $split arguments must be strings. |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $split arguments must be strings. |
| empty array | [] | Error — $split arguments must be strings. |
| numeric array | [1,2,3] | Error — $split arguments must be strings. |
| mixed array | [1,null,"x",3] | Error — $split arguments must be strings. |
| nested array | [[1,2],[3]] | Error — $split arguments must be strings. |
| empty object | {} | Error — $split arguments must be strings. |
| object | {"x":1} | Error — $split arguments must be strings. |
| ISO date string | "2026-01-15T15:00:00Z" | ["a,b"] |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/split.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **8 exact BSON matches**, **29 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input[0] / null | Error — $split arguments must be strings. | null |
| input[0] / missing | Error — $split arguments must be strings. | null |
| delimiter[1] / null | Error — $split arguments must be strings. | null |
| delimiter[1] / missing | Error — $split arguments must be strings. | null |

</details>

[Download full comparison evidence](../../downloads/operator-parity/split.json).

<!-- END MONGO PARITY -->

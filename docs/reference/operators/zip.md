# $zip

## Definition

Combines corresponding elements of input arrays.

**Expression operator** · Arrays · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{
  "$zip": {
    "inputs": <inputs>,
    "useLongestLength": <useLongestLength>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inputs` | Yes | Array of expressions, each resolving to an array to combine by position. |
| `useLongestLength` | No | Literal boolean. Defaults to `false` (shortest input); `true` uses the longest input and pads shorter inputs. |

`defaults` is also accepted by Core as a literal array of padding values, one per input array. It is used only with `useLongestLength: true`; missing padding entries use null. This option is not listed by the current Visual catalog.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `inputs` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| missing | Field absent | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal | 2.5 | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| numeric string | "12" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| text | "hello" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| boolean | true | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty array | [] | Error — Index 0 out of bounds for length 0 |
| numeric array | [1,2,3] | Error — class java.lang.Integer cannot be cast to class java.util.List (java.lang.Integer and java.util.List are in module java.base of loader 'bootstrap') |
| object | {"x":1} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$zip":[]} | Error — $zip expects an object with 'inputs', optional 'useLongestLength' |
| {"$zip":{"unexpected":1}} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |

## Examples

Expression:
```json
{
  "$zip": {
    "inputs": [
      [
        1
      ],
      [
        2
      ]
    ]
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [[1,2]].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `inputs`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| missing | Field absent | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| zero | 0 | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| negative | -2 | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal | 2.5 | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| numeric string | "12" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| text | "hello" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty string | "" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| boolean | true | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| false | false | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty array | [] | Error — Index 0 out of bounds for length 0 |
| numeric array | [1,2,3] | Error — class java.lang.Integer cannot be cast to class java.util.List (java.lang.Integer and java.util.List are in module java.base of loader 'bootstrap') |
| mixed array | [1,null,"x",3] | Error — class java.lang.Integer cannot be cast to class java.util.List (java.lang.Integer and java.util.List are in module java.base of loader 'bootstrap') |
| nested array | [[1,2],[3]] | [[1,3]] |
| empty object | {} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| object | {"x":1} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| omitted named argument | Argument removed | Error — $zip inputs must be array of arrays and useLongestLength a boolean |

**Argument: `useLongestLength`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| zero | 0 | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| negative | -2 | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal | 2.5 | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| numeric string | "12" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| text | "hello" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty string | "" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| boolean | true | [[1,2]] |
| false | false | [[1,2]] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty array | [] | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| numeric array | [1,2,3] | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| mixed array | [1,null,"x",3] | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| nested array | [[1,2],[3]] | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty object | {} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| object | {"x":1} | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $zip inputs must be array of arrays and useLongestLength a boolean |
| omitted named argument | Argument removed | [[1,2]] |


</details>

## Verification

This page records **42 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/zip.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **37 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| inputs / nested array | [[1,3]] | Error — Invalid $project :: caused by :: inputs must be an array of expressions, found string |

</details>

[Download full comparison evidence](../../downloads/operator-parity/zip.json).

<!-- END MONGO PARITY -->

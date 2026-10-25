# $zip

Combines corresponding elements of input arrays.

**Category:** Arrays. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `inputs` | ARRAY | Yes | Expression evaluated against the input |
| `useLongestLength` | BOOLEAN | No | Literal configuration |

Argument count: minimum 1; maximum 2.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `inputs`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| missing | Field absent | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| zero | 0 | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| negative | -2 | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal | 2.5 | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| numeric string | "12" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| text | "hello" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty string | "" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| boolean | true | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| false | false | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty array | [] | Error: IndexOutOfBoundsException — Index 0 out of bounds for length 0 |
| numeric array | [1,2,3] | Error: ClassCastException — class java.lang.Integer cannot be cast to class java.util.List (java.lang.Integer and java.util.List are in module java.base of loader 'bootstrap') |
| mixed array | [1,null,"x",3] | Error: ClassCastException — class java.lang.Integer cannot be cast to class java.util.List (java.lang.Integer and java.util.List are in module java.base of loader 'bootstrap') |
| nested array | [[1,2],[3]] | [[1,3]] |
| empty object | {} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| object | {"x":1} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |

### Argument: `useLongestLength`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| zero | 0 | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| negative | -2 | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal | 2.5 | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| numeric string | "12" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| text | "hello" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty string | "" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| boolean | true | [[1,2]] |
| false | false | [[1,2]] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty array | [] | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| empty object | {} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| object | {"x":1} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |
| omitted named argument | Argument removed | [[1,2]] |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$zip":[]} | Error: IllegalArgumentException — $zip expects an object with 'inputs', optional 'useLongestLength' |
| {"$zip":{"unexpected":1}} | Error: IllegalArgumentException — $zip inputs must be array of arrays and useLongestLength a boolean |

## Scope and reproducibility

This page records **42 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/zip.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **4 exact BSON matches**, **37 both rejected**, **1 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| inputs / nested array | [[1,3]] | Error: Location34461 — Invalid $project :: caused by :: inputs must be an array of expressions, found string |

[Download full comparison evidence](../../downloads/operator-parity/zip.json).

<!-- END MONGO PARITY -->

# $map

Evaluates an expression for each array element.

**Category:** Arrays. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | ARRAY | Yes | Expression evaluated against the input |
| `as` | STRING | No | Literal configuration |
| `in` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 3.

Declared result types: **ARRAY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$map": {
    "input": [
      1,
      2
    ],
    "as": "x",
    "in": "$$x"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [1,2].

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| missing | Field absent | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| zero | 0 | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| negative | -2 | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| decimal | 2.5 | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| numeric string | "12" | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| text | "hello" | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| empty string | "" | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| boolean | true | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| false | false | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| object | {"x":1} | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $map 'input' must resolve to an array |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $map requires 'input' and 'in' fields |

### Argument: `as`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: NullPointerException — Cannot invoke "Object.toString()" because the return value of "java.util.Map.get(Object)" is null |
| zero | 0 | [null,null] |
| negative | -2 | [null,null] |
| decimal | 2.5 | [null,null] |
| numeric string | "12" | [null,null] |
| text | "hello" | [null,null] |
| empty string | "" | [null,null] |
| boolean | true | [null,null] |
| false | false | [null,null] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | [null,null] |
| decimal128 | {"$numberDecimal":"1.25"} | [null,null] |
| empty array | [] | [null,null] |
| numeric array | [1,2,3] | [null,null] |
| mixed array | [1,null,"x",3] | [null,null] |
| nested array | [[1,2],[3]] | [null,null] |
| empty object | {} | [null,null] |
| object | {"x":1} | [null,null] |
| ISO date string | "2026-01-15T15:00:00Z" | [null,null] |
| omitted named argument | Argument removed | [null,null] |

### Argument: `in`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | [null,null] |
| missing | Field absent | [null,null] |
| zero | 0 | [0,0] |
| negative | -2 | [-2,-2] |
| decimal | 2.5 | [2.5,2.5] |
| numeric string | "12" | ["12","12"] |
| text | "hello" | ["hello","hello"] |
| empty string | "" | ["",""] |
| boolean | true | [true,true] |
| false | false | [false,false] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | [{"$date":1768489200000},{"$date":1768489200000}] |
| decimal128 | {"$numberDecimal":"1.25"} | [{"$numberDecimal":"1.25"},{"$numberDecimal":"1.25"}] |
| empty array | [] | [[],[]] |
| numeric array | [1,2,3] | [[1,2,3],[1,2,3]] |
| mixed array | [1,null,"x",3] | [[1,null,"x",3],[1,null,"x",3]] |
| nested array | [[1,2],[3]] | [[[1,2],[3]],[[1,2],[3]]] |
| empty object | {} | [{},{}] |
| object | {"x":1} | [{"x":1},{"x":1}] |
| ISO date string | "2026-01-15T15:00:00Z" | ["2026-01-15T15:00:00Z","2026-01-15T15:00:00Z"] |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $map requires 'input' and 'in' fields |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$map":[]} | Error: IllegalArgumentException — $map expects an object with fields: input, as, in |
| {"$map":{"unexpected":1}} | Error: IllegalArgumentException — $map requires 'input' and 'in' fields |

## Additional boundary examples

<details>
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$map": {
    "input": [
      {
        "price": 2
      }
    ],
    "as": "item",
    "in": {
      "$multiply": [
        "$$item.price",
        3
      ]
    }
  }
}
```

Input:
```json
{}
```

**SrotaX:** [6.0].

</details>

## Scope and reproducibility

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/map.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **24 exact BSON matches**, **18 both rejected**, **21 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error: IllegalArgumentException — $map 'input' must resolve to an array | null |
| input / missing | Error: IllegalArgumentException — $map 'input' must resolve to an array | null |
| as / zero | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / negative | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / decimal | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / numeric string | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: '12' starts with an invalid character for a user variable name |
| as / text | [null,null] | Error: Location17276 — Invalid $project :: caused by :: Use of undefined variable: x |
| as / empty string | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / boolean | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / false | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / typed date | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / decimal128 | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / empty array | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / numeric array | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / mixed array | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / nested array | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / empty object | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / object | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: empty variable names are not allowed |
| as / ISO date string | [null,null] | Error: FailedToParse — Invalid $project :: caused by :: '2026-01-15T15:00:00Z' starts with an invalid character for a user variable name |
| as / omitted named argument | [null,null] | Error: Location17276 — Invalid $project :: caused by :: Use of undefined variable: x |
| all / boundary example | [6.0] | [6] |

[Download full comparison evidence](../../downloads/operator-parity/map.json).

<!-- END MONGO PARITY -->

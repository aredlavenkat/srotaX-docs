# $let

Evaluates an expression with locally bound variables.

**Category:** Conditional. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an object with the named arguments below.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `vars` | OBJECT | Yes | Expression evaluated against the input |
| `in` | ANY | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **ANY**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$let": {
    "vars": {
      "a": 2
    },
    "in": "$$a"
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

### Argument: `vars`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | null |
| negative | -2 | null |
| decimal | 2.5 | null |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | null |
| boolean | true | null |
| false | false | null |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | null |
| decimal128 | {"$numberDecimal":"1.25"} | null |
| empty array | [] | null |
| numeric array | [1,2,3] | null |
| mixed array | [1,null,"x",3] | null |
| nested array | [[1,2],[3]] | null |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | null |
| omitted named argument | Argument removed | null |

### Argument: `in`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | true |
| false | false | false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | {'$numberLong': '1768489200000'} (date) |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (decimal128) |
| empty array | [] | [] |
| numeric array | [1,2,3] | [1,2,3] |
| mixed array | [1,null,"x",3] | [1,null,"x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | {} |
| object | {"x":1} | {"x":1} |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | Error: IllegalArgumentException — $let requires an 'in' expression |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$let":[]} | Error: IllegalArgumentException — $let expects an object with 'vars' and 'in' |
| {"$let":{"unexpected":1}} | Error: IllegalArgumentException — $let requires an 'in' expression |

## Additional boundary examples

<details>
<summary>Show 1 tested examples</summary>

Expression:
```json
{
  "$let": {
    "vars": {
      "total": 5
    },
    "in": {
      "$add": [
        "$$total",
        2
      ]
    }
  }
}
```

Input:
```json
{}
```

**SrotaX:** 7.0 (double).

</details>

## Scope and reproducibility

This page records **44 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/let.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **19 exact BSON matches**, **3 both rejected**, **22 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| vars / null | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / missing | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / zero | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / negative | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / decimal | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / numeric string | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / text | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / empty string | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / boolean | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / false | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / typed date | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / decimal128 | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / empty array | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / numeric array | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / mixed array | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / nested array | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / empty object | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / object | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| vars / ISO date string | null | Error: Location10065 — Invalid $project :: caused by :: invalid parameter: expected an object (vars) |
| in / missing | null | Missing (field omitted) |
| vars / omitted named argument | null | Error: Location16876 — Invalid $project :: caused by :: Missing 'vars' parameter to $let |
| all / boundary example | 7.0 (double) | 7 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/let.json).

<!-- END MONGO PARITY -->

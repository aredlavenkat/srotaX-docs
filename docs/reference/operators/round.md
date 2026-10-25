# $round

Rounds a number to the specified decimal place using ties-to-even rounding (HALF_EVEN); the place defaults to zero.

**Category:** Arithmetic. **Studio Visual entry:** Available. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `number` | NUMBER | Yes | Expression evaluated against the input |
| `place` | INT | No | Expression evaluated against the input |

Argument count: minimum 1; maximum 2.

Declared result types: **NULL, NUMBER**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

Expression:
```json
{
  "$round": [
    2.5
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 2.0 (double).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `number[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0 (int32) |
| negative | -2 | -2 (int32) |
| decimal | 2.5 | 2.0 (double) |
| numeric string | "12" | Error: IllegalArgumentException — Number and integer precision required |
| text | "hello" | Error: IllegalArgumentException — Number and integer precision required |
| empty string | "" | Error: IllegalArgumentException — Number and integer precision required |
| boolean | true | Error: IllegalArgumentException — Number and integer precision required |
| false | false | Error: IllegalArgumentException — Number and integer precision required |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: IllegalArgumentException — Number and integer precision required |
| decimal128 | {"$numberDecimal":"1.25"} | 1.0 (double) |
| empty array | [] | Error: IllegalArgumentException — Number and integer precision required |
| numeric array | [1,2,3] | Error: IllegalArgumentException — Number and integer precision required |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — Number and integer precision required |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — Number and integer precision required |
| empty object | {} | Error: IllegalArgumentException — Number and integer precision required |
| object | {"x":1} | Error: IllegalArgumentException — Number and integer precision required |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — Number and integer precision required |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$round":[]} | Error: IllegalArgumentException — $round requires [number, place?] |
| {"$round":{"unexpected":1}} | Error: IllegalArgumentException — Number and integer precision required |

## Additional boundary examples

<details>
<summary>Show 2 tested examples</summary>

Expression:
```json
{
  "$round": [
    2.345,
    2
  ]
}
```

Input:
```json
{}
```

**SrotaX:** 2.34 (double).

Expression:
```json
{
  "$round": [
    2.5,
    0
  ]
}
```

Input:
```json
{}
```

**SrotaX:** 2.0 (double).

</details>

## Scope and reproducibility

This page records **24 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/round.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **15 both rejected**, **2 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| number[0] / decimal128 | 1.0 (double) | 1 (decimal128) |
| all / boundary example | 2.34 (double) | 2.35 (double) |

[Download full comparison evidence](../../downloads/operator-parity/round.json).

<!-- END MONGO PARITY -->

# $week

Extracts week using the host calendar.

**Category:** Dates. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply one expression as the operator value.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | DATE | Yes | Expression evaluated against the input |

Argument count: minimum 1; maximum 1.

Declared result types: **INT**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

**Test environment:** JVM timezone `America/Toronto`, locale `en-IN`. Some calendar operators use the JVM default timezone; results without an explicit timezone must not be assumed to use UTC. The tables record this environment.

## Example

Expression:
```json
{
  "$week": {
    "$toDate": "2024-01-02T03:04:05.006Z"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 1 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: IllegalArgumentException — $week requires a Date input |
| missing | Field absent | Error: IllegalArgumentException — $week requires a Date input |
| zero | 0 | Error: IllegalArgumentException — $week requires a Date input |
| negative | -2 | Error: IllegalArgumentException — $week requires a Date input |
| decimal | 2.5 | Error: IllegalArgumentException — $week requires a Date input |
| numeric string | "12" | Error: IllegalArgumentException — $week requires a Date input |
| text | "hello" | Error: IllegalArgumentException — $week requires a Date input |
| empty string | "" | Error: IllegalArgumentException — $week requires a Date input |
| boolean | true | Error: IllegalArgumentException — $week requires a Date input |
| false | false | Error: IllegalArgumentException — $week requires a Date input |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 3 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | Error: IllegalArgumentException — $week requires a Date input |
| empty array | [] | Error: IllegalArgumentException — $week requires a Date input |
| numeric array | [1,2,3] | Error: IllegalArgumentException — $week requires a Date input |
| mixed array | [1,null,"x",3] | Error: IllegalArgumentException — $week requires a Date input |
| nested array | [[1,2],[3]] | Error: IllegalArgumentException — $week requires a Date input |
| empty object | {} | Error: IllegalArgumentException — $week requires a Date input |
| object | {"x":1} | Error: IllegalArgumentException — $week requires a Date input |
| ISO date string | "2026-01-15T15:00:00Z" | Error: IllegalArgumentException — $week requires a Date input |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$week":[]} | Error: IllegalArgumentException — $week requires a Date input |
| {"$week":{"unexpected":1}} | Error: IllegalArgumentException — $week requires a Date input |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/week.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **0 exact BSON matches**, **18 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | 1 (int32) | 0 (int32) |
| input / null | Error: IllegalArgumentException — $week requires a Date input | null |
| input / missing | Error: IllegalArgumentException — $week requires a Date input | null |
| input / typed date | 3 (int32) | 2 (int32) |

[Download full comparison evidence](../../downloads/operator-parity/week.json).

<!-- END MONGO PARITY -->

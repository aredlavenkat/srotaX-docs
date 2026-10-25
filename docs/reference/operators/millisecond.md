# $millisecond

Extracts millisecond using the host calendar.

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
  "$millisecond": {
    "$toDate": "2024-01-02T03:04:05.006Z"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 6 (int32).

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null |
| missing | Field absent | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null |
| zero | 0 | 0 (int32) |
| negative | -2 | 0 (int32) |
| decimal | 2.5 | 0 (int32) |
| numeric string | "12" | 0 (int32) |
| text | "hello" | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: hello |
| empty string | "" | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got:  |
| boolean | true | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: true |
| false | false | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | 0 (int32) |
| empty array | [] | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [] |
| numeric array | [1,2,3] | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [1, 2, 3] |
| mixed array | [1,null,"x",3] | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [1, null, x, 3] |
| nested array | [[1,2],[3]] | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [[1, 2], [3]] |
| empty object | {} | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: Document{{}} |
| object | {"x":1} | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: Document{{x=1}} |
| ISO date string | "2026-01-15T15:00:00Z" | 0 (int32) |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$millisecond":[]} | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '[]', but got: [] |
| {"$millisecond":{"unexpected":1}} | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field 'Document{{unexpected=1}}', but got: {unexpected=1} |

## Scope and reproducibility

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/millisecond.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **12 both rejected**, **8 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null | null |
| input / missing | Error: RuntimeException — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null | null |
| input / zero | 0 (int32) | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type int to Date |
| input / negative | 0 (int32) | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type int to Date |
| input / decimal | 0 (int32) | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type double to Date |
| input / numeric string | 0 (int32) | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type string to Date |
| input / decimal128 | 0 (int32) | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type decimal to Date |
| input / ISO date string | 0 (int32) | Error: Location16006 — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type string to Date |

[Download full comparison evidence](../../downloads/operator-parity/millisecond.json).

<!-- END MONGO PARITY -->

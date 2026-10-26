# $millisecond

## Definition

Extracts millisecond using the host calendar.

**Expression operator** · Dates · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$millisecond": <expression> }
```

Replace angle-bracket placeholders with expressions or values.

Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.

The value goes directly after the operator name; do not add an `input` wrapper.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

Date cases use JVM timezone `America/Toronto` and locale `en-IN`. Named date operators with timezone support generally default to UTC; older single-date extraction operators can use the JVM timezone.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null |
| missing | Field absent | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null |
| decimal | 2.5 | 0 (int32) |
| numeric string | "12" | 0 (int32) |
| text | "hello" | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: hello |
| boolean | true | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: true |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0 (int32) |
| empty array | [] | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [] |
| numeric array | [1,2,3] | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [1, 2, 3] |
| object | {"x":1} | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: Document{{x=1}} |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$millisecond":[]} | Error — $millisecond: expected date, date-string, or timestamp for field '[]', but got: [] |
| {"$millisecond":{"unexpected":1}} | Error — $millisecond: expected date, date-string, or timestamp for field 'Document{{unexpected=1}}', but got: {unexpected=1} |

## Examples

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

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null |
| missing | Field absent | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null |
| zero | 0 | 0 (int32) |
| negative | -2 | 0 (int32) |
| decimal | 2.5 | 0 (int32) |
| numeric string | "12" | 0 (int32) |
| text | "hello" | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: hello |
| empty string | "" | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got:  |
| boolean | true | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: true |
| false | false | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: false |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | 0 (int32) |
| decimal128 | {"$numberDecimal":"1.25"} | 0 (int32) |
| empty array | [] | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [] |
| numeric array | [1,2,3] | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [1, 2, 3] |
| mixed array | [1,null,"x",3] | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [1, null, x, 3] |
| nested array | [[1,2],[3]] | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: [[1, 2], [3]] |
| empty object | {} | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: Document{{}} |
| object | {"x":1} | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: Document{{x=1}} |
| ISO date string | "2026-01-15T15:00:00Z" | 0 (int32) |


</details>

## Verification

This page records **22 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/millisecond.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **2 exact BSON matches**, **12 both rejected**, **8 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null | null |
| input / missing | Error — $millisecond: expected date, date-string, or timestamp for field '$probe', but got: null | null |
| input / zero | 0 (int32) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type int to Date |
| input / negative | 0 (int32) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type int to Date |
| input / decimal | 0 (int32) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type double to Date |
| input / numeric string | 0 (int32) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type string to Date |
| input / decimal128 | 0 (int32) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type decimal to Date |
| input / ISO date string | 0 (int32) | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: can't convert from BSON type string to Date |

</details>

[Download full comparison evidence](../../downloads/operator-parity/millisecond.json).

<!-- END MONGO PARITY -->

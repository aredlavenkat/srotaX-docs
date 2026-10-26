# $filter

## Definition

Keeps array elements satisfying a boolean condition.

**Expression operator** · Arrays · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{
  "$filter": {
    "input": <input>,
    "as": <as>,
    "cond": <cond>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `as` | No | Literal variable name for the current array item; defaults to `"this"`. Refer to it as `$$name` in the nested expression. |
| `cond` | Yes | Condition evaluated for each array item. Items with a matching condition are retained. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | [] |
| missing | Field absent | [] |
| decimal | 2.5 | [] |
| numeric string | "12" | [] |
| text | "hello" | [] |
| boolean | true | [] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | [] |
| empty array | [] | [] |
| numeric array | [1,2,3] | [2,3] |
| object | {"x":1} | [] |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$filter":[]} | Error — $filter expects an object |
| {"$filter":{"unexpected":1}} | [] |

## Examples

Expression:
```json
{
  "$filter": {
    "input": [
      1,
      2
    ],
    "as": "x",
    "cond": {
      "$gt": [
        "$$x",
        1
      ]
    }
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** [2].

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | [] |
| missing | Field absent | [] |
| zero | 0 | [] |
| negative | -2 | [] |
| decimal | 2.5 | [] |
| numeric string | "12" | [] |
| text | "hello" | [] |
| empty string | "" | [] |
| boolean | true | [] |
| false | false | [] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | [] |
| decimal128 | {"$numberDecimal":"1.25"} | [] |
| empty array | [] | [] |
| numeric array | [1,2,3] | [2,3] |
| mixed array | [1,null,"x",3] | ["x",3] |
| nested array | [[1,2],[3]] | [[1,2],[3]] |
| empty object | {} | [] |
| object | {"x":1} | [] |
| ISO date string | "2026-01-15T15:00:00Z" | [] |
| omitted named argument | Argument removed | [] |

**Argument: `as`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "Object.toString()" because the return value of "java.util.Map.get(Object)" is null |
| zero | 0 | Error — Undefined variable: $$x |
| negative | -2 | Error — Undefined variable: $$x |
| decimal | 2.5 | Error — Undefined variable: $$x |
| numeric string | "12" | Error — Undefined variable: $$x |
| text | "hello" | Error — Undefined variable: $$x |
| empty string | "" | Error — Undefined variable: $$x |
| boolean | true | Error — Undefined variable: $$x |
| false | false | Error — Undefined variable: $$x |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — Undefined variable: $$x |
| decimal128 | {"$numberDecimal":"1.25"} | Error — Undefined variable: $$x |
| empty array | [] | Error — Undefined variable: $$x |
| numeric array | [1,2,3] | Error — Undefined variable: $$x |
| mixed array | [1,null,"x",3] | Error — Undefined variable: $$x |
| nested array | [[1,2],[3]] | Error — Undefined variable: $$x |
| empty object | {} | Error — Undefined variable: $$x |
| object | {"x":1} | Error — Undefined variable: $$x |
| ISO date string | "2026-01-15T15:00:00Z" | Error — Undefined variable: $$x |
| omitted named argument | Argument removed | Error — Undefined variable: $$x |

**Argument: `cond`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | [] |
| missing | Field absent | [] |
| zero | 0 | [] |
| negative | -2 | [] |
| decimal | 2.5 | [] |
| numeric string | "12" | [] |
| text | "hello" | [] |
| empty string | "" | [] |
| boolean | true | [1,2] |
| false | false | [] |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | [] |
| decimal128 | {"$numberDecimal":"1.25"} | [] |
| empty array | [] | [] |
| numeric array | [1,2,3] | [] |
| mixed array | [1,null,"x",3] | [] |
| nested array | [[1,2],[3]] | [] |
| empty object | {} | [] |
| object | {"x":1} | [] |
| ISO date string | "2026-01-15T15:00:00Z" | [] |
| omitted named argument | Argument removed | [] |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 2 tested examples</summary>

Expression:
```json
{
  "$filter": {
    "input": [
      1,
      2,
      3
    ],
    "as": "item",
    "cond": true,
    "limit": 1
  }
}
```

Input:
```json
{}
```

**SrotaX:** [1,2,3].

Expression:
```json
{
  "$filter": {
    "input": null,
    "cond": true
  }
}
```

Input:
```json
{}
```

**SrotaX:** [].

</details>

## Verification

This page records **64 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/filter.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **10 exact BSON matches**, **20 both rejected**, **34 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / null | [] | null |
| input / missing | [] | null |
| input / zero | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not int |
| input / negative | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not int |
| input / decimal | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not double |
| input / numeric string | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not string |
| input / text | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not string |
| input / empty string | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not string |
| input / boolean | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not bool |
| input / false | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not bool |
| input / typed date | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not date |
| input / decimal128 | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not decimal |
| input / empty object | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not object |
| input / object | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not object |
| input / ISO date string | [] | Error — Executor error during aggregate command on namespace: fluxion_operator_parity_disposable.$cmd.aggregate :: caused by :: input to $filter must be an array not string |
| cond / negative | [] | [1,2] |
| cond / decimal | [] | [1,2] |
| cond / numeric string | [] | [1,2] |
| cond / text | [] | [1,2] |
| cond / empty string | [] | [1,2] |
| cond / typed date | [] | [1,2] |
| cond / decimal128 | [] | [1,2] |
| cond / empty array | [] | [1,2] |
| cond / numeric array | [] | [1,2] |
| cond / mixed array | [] | [1,2] |
| cond / nested array | [] | [1,2] |
| cond / empty object | [] | [1,2] |
| cond / object | [] | [1,2] |
| cond / ISO date string | [] | [1,2] |
| input / omitted named argument | [] | Error — Invalid $project :: caused by :: Missing 'input' parameter to $filter |
| cond / omitted named argument | [] | Error — Invalid $project :: caused by :: Missing 'cond' parameter to $filter |
| all / unknown option | [] | Error — Invalid $project :: caused by :: Unrecognized parameter to $filter: unexpected |
| all / boundary example | [1,2,3] | [1] |
| all / boundary example | [] | null |

</details>

[Download full comparison evidence](../../downloads/operator-parity/filter.json).

<!-- END MONGO PARITY -->

# $replaceAll

## Definition

Replaces all literal text occurrences.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$replaceAll": {
    "input": <input>,
    "find": <find>,
    "replacement": <replacement>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `find` | Yes | Substring to replace. |
| `replacement` | Yes | Replacement text. |

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| boolean | true | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| empty array | [] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| object | {"x":1} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$replaceAll":[]} | Error — class java.util.ArrayList cannot be cast to class java.util.Map (java.util.ArrayList and java.util.Map are in module java.base of loader 'bootstrap') |
| {"$replaceAll":{"unexpected":1}} | null |

## Examples

Expression:
```json
{
  "$replaceAll": {
    "input": "aba",
    "find": "a",
    "replacement": "x"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** "xbx".

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | "12" |
| text | "hello" | "hello" |
| empty string | "" | "" |
| boolean | true | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| false | false | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal128 | {"$numberDecimal":"1.25"} | Error — class org.bson.types.Decimal128 cannot be cast to class java.lang.String (org.bson.types.Decimal128 is in unnamed module of loader 'app'; java.lang.String is in module java.base of |
| empty array | [] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| mixed array | [1,null,"x",3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| nested array | [[1,2],[3]] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| empty object | {} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| object | {"x":1} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | null |

**Argument: `find`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | "aba" |
| text | "hello" | "aba" |
| empty string | "" | "xaxbxax" |
| boolean | true | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| false | false | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal128 | {"$numberDecimal":"1.25"} | Error — class org.bson.types.Decimal128 cannot be cast to class java.lang.String (org.bson.types.Decimal128 is in unnamed module of loader 'app'; java.lang.String is in module java.base of |
| empty array | [] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| mixed array | [1,null,"x",3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| nested array | [[1,2],[3]] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| empty object | {} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| object | {"x":1} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| ISO date string | "2026-01-15T15:00:00Z" | "aba" |
| omitted named argument | Argument removed | null |

**Argument: `replacement`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | "12b12" |
| text | "hello" | "hellobhello" |
| empty string | "" | "b" |
| boolean | true | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| false | false | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal128 | {"$numberDecimal":"1.25"} | Error — class org.bson.types.Decimal128 cannot be cast to class java.lang.String (org.bson.types.Decimal128 is in unnamed module of loader 'app'; java.lang.String is in module java.base of |
| empty array | [] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| mixed array | [1,null,"x",3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| nested array | [[1,2],[3]] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| empty object | {} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| object | {"x":1} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| ISO date string | "2026-01-15T15:00:00Z" | "2026-01-15T15:00:00Zb2026-01-15T15:00:00Z" |
| omitted named argument | Argument removed | null |


</details>

## Verification

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/replaceAll.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **19 exact BSON matches**, **40 both rejected**, **4 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| input / omitted named argument | null | Error — Invalid $project :: caused by :: $replaceAll requires 'input' to be specified |
| find / omitted named argument | null | Error — Invalid $project :: caused by :: $replaceAll requires 'find' to be specified |
| replacement / omitted named argument | null | Error — Invalid $project :: caused by :: $replaceAll requires 'replacement' to be specified |
| all / unknown option | null | Error — Invalid $project :: caused by :: $replaceAll found an unknown argument: unexpected |

</details>

[Download full comparison evidence](../../downloads/operator-parity/replaceAll.json).

<!-- END MONGO PARITY -->

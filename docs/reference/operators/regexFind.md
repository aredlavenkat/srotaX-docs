# $regexFind

## Definition

Finds the first regex match and its UTF-16 index.

**Expression operator** · Text · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$regexFind": {
    "input": <input>,
    "regex": <regex>,
    "options": <options>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `regex` | Yes | Regular-expression pattern to search for. |
| `options` | No | Regex option string. See Supported values below. |

## Supported values

`options` accepts any combination of `i` (case-insensitive), `m` (multiline anchors), `s` (dot matches newlines), and `x` (ignore pattern whitespace/comments). Omit it or use `""` for no flags. Patterns use Java regular-expression behavior.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "java.lang.CharSequence.length()" because "this.text" is null |
| missing | Field absent | Error — Cannot invoke "java.lang.CharSequence.length()" because "this.text" is null |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | null |
| text | "hello" | null |
| boolean | true | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| empty array | [] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| object | {"x":1} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$regexFind":[]} | Error — class java.util.ArrayList cannot be cast to class java.util.Map (java.util.ArrayList and java.util.Map are in module java.base of loader 'bootstrap') |
| {"$regexFind":{"unexpected":1}} | Error — Cannot invoke "String.isEmpty()" because "this.pattern" is null |

## Examples

Expression:
```json
{
  "$regexFind": {
    "input": "abc",
    "regex": "ab"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** {"idx":0,"captures":[],"match":"ab"}.

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "java.lang.CharSequence.length()" because "this.text" is null |
| missing | Field absent | Error — Cannot invoke "java.lang.CharSequence.length()" because "this.text" is null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | null |
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
| ISO date string | "2026-01-15T15:00:00Z" | null |
| omitted named argument | Argument removed | Error — Cannot invoke "java.lang.CharSequence.length()" because "this.text" is null |

**Argument: `regex`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "String.isEmpty()" because "this.pattern" is null |
| missing | Field absent | Error — Cannot invoke "String.isEmpty()" because "this.pattern" is null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | {"idx":0,"captures":[],"match":""} |
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
| ISO date string | "2026-01-15T15:00:00Z" | null |
| omitted named argument | Argument removed | Error — Cannot invoke "String.isEmpty()" because "this.pattern" is null |

**Argument: `options`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "String.matches(String)" because "options" is null |
| missing | Field absent | Error — Cannot invoke "String.matches(String)" because "options" is null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | Error — Unsupported regex option |
| text | "hello" | Error — Unsupported regex option |
| empty string | "" | {"idx":0,"captures":[],"match":"ab"} |
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
| ISO date string | "2026-01-15T15:00:00Z" | Error — Unsupported regex option |
| omitted named argument | Argument removed | {"idx":0,"captures":[],"match":"ab"} |


</details>

## Verification

This page records **63 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/regexFind.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **7 exact BSON matches**, **46 both rejected**, **6 value/type/acceptance differences**, **4 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

<details markdown="1">
<summary>Show observed differences</summary>

| Tested case | SrotaX | MongoDB |
| --- | --- | --- |
| all / baseline | {"idx":0,"captures":[],"match":"ab"} | {"match":"ab","idx":0,"captures":[]} |
| input / null | Error — Cannot invoke "java.lang.CharSequence.length()" because "this.text" is null | null |
| input / missing | Error — Cannot invoke "java.lang.CharSequence.length()" because "this.text" is null | null |
| regex / null | Error — Cannot invoke "String.isEmpty()" because "this.pattern" is null | null |
| regex / missing | Error — Cannot invoke "String.isEmpty()" because "this.pattern" is null | null |
| regex / empty string | {"idx":0,"captures":[],"match":""} | {"match":"","idx":0,"captures":[]} |
| options / null | Error — Cannot invoke "String.matches(String)" because "options" is null | {"match":"ab","idx":0,"captures":[]} |
| options / missing | Error — Cannot invoke "String.matches(String)" because "options" is null | {"match":"ab","idx":0,"captures":[]} |
| options / empty string | {"idx":0,"captures":[],"match":"ab"} | {"match":"ab","idx":0,"captures":[]} |
| options / omitted named argument | {"idx":0,"captures":[],"match":"ab"} | {"match":"ab","idx":0,"captures":[]} |

</details>

[Download full comparison evidence](../../downloads/operator-parity/regexFind.json).

<!-- END MONGO PARITY -->

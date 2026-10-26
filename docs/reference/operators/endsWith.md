# $endsWith

## Definition

Checks a literal text suffix.

**Expression operator** · Text · Studio Visual: not exposed. Studio validates the complete expression separately.

## Syntax

```text
{ "$endsWith": [ <input>, <text> ] }
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `text` | Yes | Expression supplying the text value. |

Arguments are positional: keep the order shown. The authoring signature accepts 2–2 arguments.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "String.endsWith(String)" because "input" is null |
| missing | Field absent | Error — Cannot invoke "String.endsWith(String)" because "input" is null |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | false |
| text | "hello" | false |
| boolean | true | Error — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| empty array | [] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| object | {"x":1} | Error — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$endsWith":[]} | Error — $endsWith expects [string, suffix] |
| {"$endsWith":{"unexpected":1}} | Error — class org.bson.Document cannot be cast to class java.util.List (org.bson.Document is in unnamed module of loader 'app'; java.util.List is in module java.base of loader 'bootstrap') |

## Examples

Expression:
```json
{
  "$endsWith": [
    "abc",
    "c"
  ]
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** true.

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input[0]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "String.endsWith(String)" because "input" is null |
| missing | Field absent | Error — Cannot invoke "String.endsWith(String)" because "input" is null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | false |
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
| ISO date string | "2026-01-15T15:00:00Z" | false |

**Argument: `text[1]`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — Cannot invoke "String.length()" because "suffix" is null |
| missing | Field absent | Error — Cannot invoke "String.length()" because "suffix" is null |
| zero | 0 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | true |
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
| ISO date string | "2026-01-15T15:00:00Z" | false |


</details>

## Verification

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/endsWith.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

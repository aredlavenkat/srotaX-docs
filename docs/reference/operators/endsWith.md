# $endsWith

Checks a literal text suffix.

**Category:** Text. **Studio Visual entry:** Not exposed. This page describes Core expression execution; Studio also checks field types and authoring permissions.

## Syntax and arguments

Supply an ordered array of arguments.

| Argument | Metadata input types | Required | Evaluation |
| --- | --- | --- | --- |
| `input` | STRING | Yes | Expression evaluated against the input |
| `text` | STRING | Yes | Expression evaluated against the input |

Argument count: minimum 2; maximum 2.

Declared result types: **BOOLEAN**. Actual result types for tested inputs appear below. Metadata is an authoring hint; where a case differs, use the observed result and treat the discrepancy as a limitation.

## Example

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

## Behavior for different inputs

Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

### Argument: `input[0]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: NullPointerException — Cannot invoke "String.endsWith(String)" because "input" is null |
| missing | Field absent | Error: NullPointerException — Cannot invoke "String.endsWith(String)" because "input" is null |
| zero | 0 | Error: ClassCastException — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error: ClassCastException — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error: ClassCastException — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | false |
| boolean | true | Error: ClassCastException — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| false | false | Error: ClassCastException — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: ClassCastException — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal128 | {"$numberDecimal":"1.25"} | Error: ClassCastException — class org.bson.types.Decimal128 cannot be cast to class java.lang.String (org.bson.types.Decimal128 is in unnamed module of loader 'app'; java.lang.String is in module java.base of |
| empty array | [] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| mixed array | [1,null,"x",3] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| nested array | [[1,2],[3]] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| empty object | {} | Error: ClassCastException — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| object | {"x":1} | Error: ClassCastException — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| ISO date string | "2026-01-15T15:00:00Z" | false |

### Argument: `text[1]`

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error: NullPointerException — Cannot invoke "String.length()" because "suffix" is null |
| missing | Field absent | Error: NullPointerException — Cannot invoke "String.length()" because "suffix" is null |
| zero | 0 | Error: ClassCastException — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| negative | -2 | Error: ClassCastException — class java.lang.Integer cannot be cast to class java.lang.String (java.lang.Integer and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal | 2.5 | Error: ClassCastException — class java.lang.Double cannot be cast to class java.lang.String (java.lang.Double and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric string | "12" | false |
| text | "hello" | false |
| empty string | "" | true |
| boolean | true | Error: ClassCastException — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| false | false | Error: ClassCastException — class java.lang.Boolean cannot be cast to class java.lang.String (java.lang.Boolean and java.lang.String are in module java.base of loader 'bootstrap') |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error: ClassCastException — class java.util.Date cannot be cast to class java.lang.String (java.util.Date and java.lang.String are in module java.base of loader 'bootstrap') |
| decimal128 | {"$numberDecimal":"1.25"} | Error: ClassCastException — class org.bson.types.Decimal128 cannot be cast to class java.lang.String (org.bson.types.Decimal128 is in unnamed module of loader 'app'; java.lang.String is in module java.base of |
| empty array | [] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| numeric array | [1,2,3] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| mixed array | [1,null,"x",3] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| nested array | [[1,2],[3]] | Error: ClassCastException — class java.util.ArrayList cannot be cast to class java.lang.String (java.util.ArrayList and java.lang.String are in module java.base of loader 'bootstrap') |
| empty object | {} | Error: ClassCastException — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| object | {"x":1} | Error: ClassCastException — class org.bson.Document cannot be cast to class java.lang.String (org.bson.Document is in unnamed module of loader 'app'; java.lang.String is in module java.base of loader 'bootstr |
| ISO date string | "2026-01-15T15:00:00Z" | false |

## Invalid invocation shapes

| Invocation | SrotaX result |
| --- | --- |
| {"$endsWith":[]} | Error: IllegalArgumentException — $endsWith expects [string, suffix] |
| {"$endsWith":{"unexpected":1}} | Error: ClassCastException — class org.bson.Document cannot be cast to class java.util.List (org.bson.Document is in unnamed module of loader 'app'; java.util.List is in module java.base of loader 'bootstrap') |

## Scope and reproducibility

This page records **41 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/endsWith.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences (removable section)

This name is a SrotaX extension or belongs to another MongoDB context. It is **not compared as a MongoDB aggregation expression**. This is not a missing implementation failure.

<!-- END MONGO PARITY -->

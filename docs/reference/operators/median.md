# $median

## Definition

Computes single-document statistics, ignoring nonnumeric values.

**Expression operator** · Statistics · Studio Visual: available. Studio validates the complete expression separately.

## Syntax

```text
{
  "$median": {
    "input": <input>,
    "method": <method>
  }
}
```

Replace angle-bracket placeholders with expressions or values.

Optional parameters may be omitted.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input` | Yes | Expression supplying the value to process. A field reference such as `"$price"` reads from the current document. |
| `method` | Yes | Literal `"approximate"`. Other method names are rejected. |

## Supported values

`method` must be the literal `"approximate"`. See the results below for the engine’s numeric behavior.

## Behavior

The following observations use the example expression below. Each row substitutes one argument while retaining the other example arguments. A missing field differs from an explicit null; the result shown is what Core actually returned.

For the `input` argument:

| Input case | Supplied value | Result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | null |
| text | "hello" | null |
| boolean | true | null |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | null |
| empty array | [] | null |
| numeric array | [1,2,3] | 2.0 (double) |
| object | {"x":1} | null |

### Argument handling

| Invocation | Result |
| --- | --- |
| {"$median":[]} | Error — $median requires [input, method] |
| {"$median":{"unexpected":1}} | Error — $median requires [input, method] |

## Examples

Expression:
```json
{
  "$median": {
    "input": [
      10,
      20,
      30,
      40
    ],
    "method": "approximate"
  }
}
```

Input document:
```json
{}
```

**Observed SrotaX result:** 20.0 (double).

## Detailed input cases

<details markdown="1">
<summary>Expand the complete argument-by-argument test matrix</summary>


Each table changes **only the indicated argument** from the example above. Other arguments retain their baseline values. Values normally come from the input field `probe`; literal configuration arguments are replaced directly. “Missing” means the field is absent, not explicitly null. Numeric strings are strings, not numbers.

**Argument: `input`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | null |
| missing | Field absent | null |
| zero | 0 | 0.0 (double) |
| negative | -2 | -2.0 (double) |
| decimal | 2.5 | 2.5 (double) |
| numeric string | "12" | null |
| text | "hello" | null |
| empty string | "" | null |
| boolean | true | null |
| false | false | null |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | null |
| decimal128 | {"$numberDecimal":"1.25"} | 1.25 (double) |
| empty array | [] | null |
| numeric array | [1,2,3] | 2.0 (double) |
| mixed array | [1,null,"x",3] | 1.0 (double) |
| nested array | [[1,2],[3]] | null |
| empty object | {} | null |
| object | {"x":1} | null |
| ISO date string | "2026-01-15T15:00:00Z" | null |
| omitted named argument | Argument removed | Error — $median requires [input, method] |

**Argument: `method`**

| Input case | Supplied value | SrotaX result |
| --- | --- | --- |
| null | null | Error — $median method must be the literal string approximate |
| zero | 0 | Error — $median method must be the literal string approximate |
| negative | -2 | Error — $median method must be the literal string approximate |
| decimal | 2.5 | Error — $median method must be the literal string approximate |
| numeric string | "12" | Error — $median method must be the literal string approximate |
| text | "hello" | Error — $median method must be the literal string approximate |
| empty string | "" | Error — $median method must be the literal string approximate |
| boolean | true | Error — $median method must be the literal string approximate |
| false | false | Error — $median method must be the literal string approximate |
| typed date | {"$date":"2026-01-15T15:00:00Z"} | Error — $median method must be the literal string approximate |
| decimal128 | {"$numberDecimal":"1.25"} | Error — $median method must be the literal string approximate |
| empty array | [] | Error — $median method must be the literal string approximate |
| numeric array | [1,2,3] | Error — $median method must be the literal string approximate |
| mixed array | [1,null,"x",3] | Error — $median method must be the literal string approximate |
| nested array | [[1,2],[3]] | Error — $median method must be the literal string approximate |
| empty object | {} | Error — $median method must be the literal string approximate |
| object | {"x":1} | Error — $median method must be the literal string approximate |
| ISO date string | "2026-01-15T15:00:00Z" | Error — $median method must be the literal string approximate |
| omitted named argument | Argument removed | Error — $median requires [input, method] |


</details>

## Additional boundary examples

<details markdown="1">
<summary>Show 17 tested examples</summary>

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    10,
    20,
    30
  ]
}
```

**SrotaX:** 20.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    10,
    20,
    30,
    40
  ]
}
```

**SrotaX:** 20.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": []
}
```

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": null
}
```

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": 5
}
```

**SrotaX:** 5.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    1,
    "x",
    null,
    3
  ]
}
```

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    1,
    [
      50
    ],
    3
  ]
}
```

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    "x",
    null,
    {}
  ]
}
```

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    1,
    {
      "$numberDouble": "NaN"
    },
    3
  ]
}
```

**SrotaX:** 1.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    1,
    {
      "$numberDouble": "Infinity"
    },
    3
  ]
}
```

**SrotaX:** 3.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    {
      "$numberDecimal": "1.2"
    },
    2,
    3
  ]
}
```

**SrotaX:** 2.0 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    1e+100,
    2e+100,
    3e+100
  ]
}
```

**SrotaX:** 2.0E100 (double).

Expression:
```json
{
  "$median": {
    "input": "$values",
    "method": "approximate"
  }
}
```

Input:
```json
{
  "values": [
    {
      "$numberDouble": "Infinity"
    }
  ]
}
```

**SrotaX:** Infinity (double).

Expression:
```json
{
  "$median": {
    "input": "$missing",
    "method": "approximate"
  }
}
```

Input:
```json
{}
```

**SrotaX:** null.

Expression:
```json
{
  "$median": {
    "input": [
      1,
      2,
      3
    ],
    "method": "continuous"
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error — $median method must be the literal string approximate.

Expression:
```json
{
  "$median": {
    "input": [
      1,
      2,
      3
    ],
    "method": null
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error — $median method must be the literal string approximate.

Expression:
```json
{
  "$median": {
    "input": [
      1,
      2,
      3
    ],
    "method": {
      "$literal": "approximate"
    }
  }
}
```

Input:
```json
{}
```

**SrotaX:** Error — $median method must be the literal string approximate.

</details>

## Verification

This page records **59 executed cases**. It covers individual argument substitutions, not every cross-product of arguments, locale, daylight-saving transitions, numeric overflow, collation or resource limits. No untested behavior is guaranteed.

[Download exact expressions, inputs and SrotaX results](../../downloads/operator-behavior/median.json). Errors are observed messages, not stable public error codes. The reference generator reads the checked-in execution report; do not edit generated observations by hand.

<!-- BEGIN MONGO PARITY -->
## MongoDB differences

Compared with **MongoDB 9.0.4**: **34 exact BSON matches**, **25 both rejected**, **0 value/type/acceptance differences**, **0 object-field-order differences**.

“Exact” includes numeric BSON types and object key order. A value of `3` as int32 differs from `3.0` as double. Object-field-order differences are reported separately; object key ordering is not enforced by the engine regression baseline. Both rejected does not mean the error codes or messages match. This is finite-case evidence, not full compatibility certification.

No differences were observed in the compared cases.

[Download full comparison evidence](../../downloads/operator-parity/median.json).

<!-- END MONGO PARITY -->

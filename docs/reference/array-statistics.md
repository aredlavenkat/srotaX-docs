# Statistics and bitwise expressions

Use these **expression operators** inside a Set Fields calculation. They calculate a value from one request document; they are not pipeline stages and do not require splitting a list into documents.

The engine registers all five operators, the compiler accepts their expression forms, and the API catalog exposes them in the Visual expression editor. The JSON examples below are also supported. These additions do not add new Aggregate List palette choices.

## Calculate statistics from a list

For this request:

```json
{"amounts": [10, 20, 30, 40]}
```

Use `$amounts` in the generated document expression. In Studio's field picker this is `input.amounts`. Store the calculation in a declared `local.*` or `output.*` field. Reading the list does not modify the immutable input.

| Operator | Purpose | Result for this input |
| --- | --- | --- |
| [`$median`](operators/median.md) | Middle value using the discrete percentile rule | `20` |
| [`$percentile`](operators/percentile.md) | Values at selected probabilities | `[10, 20, 40]` for `[0, 0.5, 1]` |
| [`$stdDevPop`](operators/stdDevPop.md) | Spread when this list is the entire population | Approximately `11.1803398875` |
| [`$stdDevSamp`](operators/stdDevSamp.md) | Estimated spread when this list is a sample | Approximately `12.9099444874` |

### Median

```json
{"$median": {"input": "$amounts", "method": "approximate"}}
```

For an even number of values, this implementation matches the tested MongoDB 9.0.4 expression behavior: it selects the **lower middle value**, not the average of the two middle values. Thus `[10,20,30,40]` returns `20`, not `25`.

### Percentiles

```json
{"$percentile": {"input": "$amounts", "p": [0, 0.5, 1], "method": "approximate"}}
```

The result is always an array, ordered like `p`. Each probability must be between 0 and 1, inclusive. `p` cannot be empty. `0` selects the minimum; `1` selects the maximum. Other probabilities select the sorted value at index `ceil(p × count) - 1`, clamped to the first value.

In Visual mode choose a fixed array for `p` and the fixed text `approximate` for `method`. In SrotaX's JSON editor, `p` must also be a literal array. The engine can evaluate some constant expressions for `p`, but the authoring compiler deliberately accepts the literal form only. A document-field reference is not supported for `p`.

The method name is required for MongoDB syntax compatibility. Fluxion sorts the values and uses discrete selection for the document expression; it does not implement MongoDB's cross-document approximate accumulator algorithm.

### Population and sample deviation

```json
{"$stdDevPop": "$amounts"}
```

```json
{"$stdDevSamp": "$amounts"}
```

Choose population deviation when the list contains the full population you want to describe. Choose sample deviation when estimating a larger population from a sample. Sample deviation divides by `n - 1`; population deviation divides by `n`.

A single operand resolving to a list traverses its numeric elements. With multiple operands, each operand is considered separately and array-valued operands are ignored. For example:

```json
{"$stdDevSamp": [10, 20, 30]}
```

This returns `10`. To express a literal list as one operand explicitly, use `{"$literal": [10,20,30]}` as shown in the individual operator examples.

## Empty and mixed inputs

| Input case | Median / percentile | Population deviation | Sample deviation |
| --- | --- | --- | --- |
| Empty, missing, null, or no numeric values | `null` / one `null` per requested percentile | `null` | `null` |
| One numeric value | That value / repeated for each percentile | `0` | `null` |
| Mixed strings, booleans, objects, nested lists | Ignore nonnumeric elements | Ignore nonnumeric elements | Ignore nonnumeric elements |
| Numeric scalar | Treat as one value | `0` | `null` |

For BSON inputs containing special numeric values, median/percentile ignore NaN and retain infinities. Standard deviation can produce NaN for nonfinite values. Ordinary JSON cannot represent NaN or infinity; avoid these values in HTTP request examples.

## Bitwise NOT

[`$bitNot`](operators/bitNot.md) flips every bit in a signed integer. It is **not Boolean NOT**; use `$not` for a true/false condition.

```json
{"$bitNot": {"$toInt": 5}}
```

Result:

```json
-6
```

In two's complement, `~x = -x - 1`. The operator preserves a 32-bit or 64-bit integer's width. Missing/null returns null. Double, Decimal128, string, Boolean, and array operands are rejected. Use `$toInt` or `$toLong` deliberately when the source is not already an integer; conversion can truncate a fractional value or fail on overflow. Visual number literals may be represented as decimals, so nest a conversion before Bitwise NOT.

## MongoDB compatibility boundary

The focused differential test used a real MongoDB **9.0.4** process: **99 cases**, **80 matching values**, and **19 inputs rejected by both engines**. It checked empty/missing/null values, mixed arrays, odd/even lengths, scalar inputs, Decimal128 values, nonfinite values, percentile bounds, invalid options, and integer widths.

This is evidence for the tested **single-document expression forms**, not complete MongoDB compatibility:

- No new `$group` accumulators or `$setWindowFields` variants are provided by this change.
- Standard deviation uses double arithmetic and comparisons allow a relative tolerance of `1e-12`; bit-for-bit equality for all numeric inputs is not promised.
- MongoDB error codes and messages are not reproduced.
- The compiler requires literal percentile options; it does not accept every constant-expression spelling supported by MongoDB.
- Locale/collation, storage/query operators, and distributed accumulation are outside this feature.

See [the broader audit](mongo-compatibility.md) for existing operator differences. The checked-in evidence is `verification/statistics-mongo-9.0.4.json`; rerun the opt-in `StatisticsMongoParityTest` in fluxion-core-engine against MongoDB 9.0.4 to reproduce it.

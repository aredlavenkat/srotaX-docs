# MongoDB compatibility: tested scope

> **Historical baseline:** the results below predate the current [all-operator behavior and parity suite](operator-parity.md). Use each operator page for current observed behavior and differences.


SrotaX is a single-document decision and transformation engine. MongoDB operator names are not a guarantee of identical behavior. Catalog registration, authoring-compiler support, and parity tests are separate checks.

## New statistics and bitwise operators

The [five new expressions](array-statistics.md) passed 99 focused comparisons against MongoDB 9.0.4: 80 matching results and 19 inputs rejected by both engines. Results allow a relative floating-point tolerance of 1e-12; error-code and message parity remain unverified.

## Broader existing-operator audit

A separate audit of an earlier **119-operator Visual catalog snapshot** ran **514 cases** against MongoDB 9.0.4. It produced **284 exact BSON matches**, **122 cases rejected by both engines**, and **108 differences**. This snapshot is not the complete current catalog. The count is a number of test cases, not a number of unsupported operators.

Differences can be result values, BSON result types, document field order, null/missing behavior, or accepting an input MongoDB rejects. Some differences are representation-only; they are not all wrong business values. They are recorded as open compatibility gaps; the five new operators do not fix these existing differences. The exact-case report is checked in at `verification/mongodb-9.0.4-audit.json`.

Examples from the report:

| Case | MongoDB 9.0.4 | Fluxion |
| --- | --- | --- |
| `$add` of integer 2 and 3 | Integer `5` | Double `5.0`; same numeric value, different BSON type |
| `$filter` with `limit: 1` over `[1,2,3]` and a true condition | `[1]` | `[1,2,3]`; limit not respected |
| `$anyElementTrue` with null operand | Error | `false` |
| `$toBool` with an empty argument list | Error | `true` |
| `$regexFind` for `ab` in `abc` | Fields ordered `match`, `idx`, `captures` | Same values with a different field order |

| Existing operator | Differing test cases |
| --- | ---: |
| `$abs` | 1 |
| `$acos` | 2 |
| `$acosh` | 2 |
| `$add` | 5 |
| `$allElementsTrue` | 3 |
| `$anyElementTrue` | 3 |
| `$arrayElemAt` | 1 |
| `$arrayToObject` | 1 |
| `$asin` | 2 |
| `$asinh` | 2 |
| `$atan` | 2 |
| `$atan2` | 2 |
| `$atanh` | 2 |
| `$cond` | 1 |
| `$convert` | 2 |
| `$cos` | 2 |
| `$cosh` | 2 |
| `$degreesToRadians` | 2 |
| `$exp` | 2 |
| `$filter` | 2 |
| `$first` | 1 |
| `$getField` | 1 |
| `$ifNull` | 1 |
| `$indexOfBytes` | 2 |
| `$last` | 1 |
| `$let` | 1 |
| `$ln` | 2 |
| `$log` | 2 |
| `$log10` | 2 |
| `$map` | 1 |
| `$min` | 2 |
| `$mod` | 1 |
| `$multiply` | 2 |
| `$objectToArray` | 2 |
| `$pow` | 1 |
| `$radiansToDegrees` | 2 |
| `$range` | 1 |
| `$reduce` | 1 |
| `$regexFind` | 3 |
| `$regexFindAll` | 3 |
| `$reverseArray` | 1 |
| `$round` | 2 |
| `$setDifference` | 2 |
| `$setUnion` | 2 |
| `$sin` | 2 |
| `$sinh` | 2 |
| `$slice` | 2 |
| `$split` | 2 |
| `$strcasecmp` | 2 |
| `$substr` | 2 |
| `$substrBytes` | 2 |
| `$substrCP` | 2 |
| `$subtract` | 1 |
| `$sum` | 4 |
| `$tan` | 2 |
| `$tanh` | 2 |
| `$toBool` | 1 |
| `$tsIncrement` | 1 |
| `$tsSecond` | 1 |

## Product scope labels

Use these labels when interpreting the MongoDB inventory:

| Label | Meaning | Capabilities |
| --- | --- | --- |
| **Out of scope by design** | Deliberately excluded from the processing engine; not missing implementation work | Native UUID/ObjectId types, indexed text/vector search, search-index management, database/cluster administration, and writes to database collections |
| **Deferred** | Outside the current implementation; intended for later stream orchestration | Source/sink connectors, continuous consumption, checkpoints, retries, backpressure, and delivery guarantees |
| **Not supported yet** | An unimplemented processing capability, without a delivery commitment | Applicable document/array operators and the conversion extensions listed below |
| **Compatibility difference** | An implemented operator differs from MongoDB in tested behavior | The observed cases in the differential audit |

`$search`, `$searchMeta`, `$vectorSearch`, and `$listSearchIndexes` are **Out of scope by design**, as are database administration stages and collection-writing `$merge`/`$out`. Search and database access can be performed by an external integration that supplies input to the engine.

Do not classify calculations over vectors already supplied in a document as indexed vector search. Do not classify in-memory document/array processing as stream orchestration. Stage syntax alone does not determine product scope.

## Remaining expression-name inventory

Relative to the MongoDB 9.0.4 inventory checked on this feature branch, 151 of 167 expression names are shared after the thirteen array/statistics/JSON conversion additions. Fluxion registers 159 expression names in total, including eight extensions or names used in another MongoDB context. These **16 names are absent from the compared expression registry**; all 16 are **Out of scope by design**, not a backlog of missing features:

`$createObjectId`, `$encStrContains`, `$encStrEndsWith`, `$encStrNormalizedEq`, `$encStrStartsWith`, `$hash`, `$hexHash`, `$meta`, `$rand`, `$sampleRate`, `$sigmoid`, `$similarityCosine`, `$similarityDotProduct`, `$similarityEuclidean`, `$toHashedIndexKey`, `$toUUID`.

This list is an inventory, not a proposed roadmap. Storage/encryption/search metadata and nondeterministic expressions may not fit SrotaX's deterministic single-document purpose. Adding a name would still require behavior and compiler tests. Pipeline-stage and cross-document accumulator gaps are not addressed by these expressions.

## Interpreting these results

Test the complete expression with realistic boundary inputs before relying on MongoDB-equivalent behavior. A passing example does not cover all BSON types, arities, Unicode strings, numeric boundaries, or invalid inputs. “Both rejected” establishes rejection only, not equivalent errors. The broad audit compares BSON exactly; the focused statistics suite uses a documented numeric tolerance, so their match counts use different criteria.

The broader parity test is opt-in (`Mongo9CompatibilityAuditTest` with `FLUXION_AUDIT_MONGO_URI`). It fails when it sees a difference; report-only mode is for investigating gaps, not claiming parity. Normal engine unit tests do not substitute for this differential check.

## Unsupported conversion extensions

The presence of `$convert` does not imply support for all MongoDB conversion options. These capabilities are currently unavailable in SrotaX:

- UUID string ↔ binary UUID and `$toUUID`: **Out of scope by design** (native identifier types).
- Base64, Base64URL, hex, UTF-8, or UUID string ↔ binary conversions.
- Numeric value ↔ binary bytes, including configurable byte order.
- `binData` conversion targets and binary subtype selection.
- `$convert` options `format`, `byteOrder`, and `base`, including newer conversion-format variants.

Perform these conversions in the calling application or integration layer if needed. UUID identifiers can remain ordinary strings when no binary representation is required. Existing supported conversions remain available. **`$bitNot` is supported** and is not included in this list.

Copilot's authoring instructions include these exclusions. For a request that requires an unsupported conversion, the instructed response is `status=unsupported` with no authoring proposal and a specific explanation. This prompt guidance does not guarantee every model response will comply; backend validation remains necessary.

## Ranked array selection

`$topN` is now supported as a single-document array expression. It delegates to the existing `$sortArray` and `$firstN` implementations. See the [executed example](operators/topN.md). Accumulator and window forms remain unsupported; collation and exact MongoDB error parity are not certified.

## Native identifier types: Out of scope by design

Native UUID (binary subtype 4) and BSON ObjectId data types are **Out of scope by design** for SrotaX authoring. They are not missing/planned product features. Represent identifiers as ordinary strings in contracts, models, inputs, local fields, and outputs; callers can validate/normalize strings and perform native-type conversion at integration boundaries.

This scope decision includes `$toUUID`, `$createObjectId`, `$toObjectId`, and `$convert` targeting native UUID/ObjectId values (including BSON type code 7 and UUID binary subtype 4). Copilot should direct requests for these native types to an external integration rather than generate them.

Ordinary **Object** data remains supported: nested JSON fields, models, and responses are not ObjectId values. `$toObject` is a separate object-conversion capability, not an identifier conversion.

This is a product-scope classification, not a claim that all corresponding engine code is absent. Existing low-level ObjectId conversion support is still present; this documentation change does not remove or disable it.


## JSON string containers

`$toArray`, `$toObject`, and `$convert` targeting `array`/`object` share strict JSON parsing. Null/missing input returns null; invalid input raises a conversion error or uses `$convert.onError`. Binary-vector conversion remains unsupported. Verified with 76 focused MongoDB 9.0.4 comparison cases; error-code parity is not claimed.

## Remaining expression operators: Out of scope by design

All 16 absent expression names in the MongoDB 9.0.4 comparison are **Out of scope by design**. They are deliberately excluded from the current product scope, not planned implementation work.

| Category | Operators |
| --- | --- |
| Hashing | `$hash`, `$hexHash`, `$toHashedIndexKey` |
| Scoring | `$sigmoid` |
| Vector calculations | `$similarityCosine`, `$similarityDotProduct`, `$similarityEuclidean` |
| Randomness | `$rand`, `$sampleRate` |
| Encrypted-field matching | `$encStrContains`, `$encStrEndsWith`, `$encStrNormalizedEq`, `$encStrStartsWith` |
| Metadata | `$meta` |
| Native identifiers | `$createObjectId`, `$toUUID` |

Perform these operations in the caller or an external integration when needed. Vector calculations are excluded by product choice, even when vectors are already present in the input; this is separate from indexed vector search.

The scope decision applies to these **expression operators**. The custom Fluxion `$sampleRate` stage has also been removed; do not generate it in any context. Expression-name coverage remains 151 of 167 MongoDB names. This classification does not establish full compatibility: behavioral differences in supported operators still require verification and fixes. Stage, accumulator and window-function gaps retain their separate classifications.

The former custom $agentCall stage has been removed from Fluxion Core. Agent invocation belongs in an external integration/orchestration layer. This does not remove SrotaX Copilot for authoring decisions.

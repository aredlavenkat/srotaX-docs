# Aggregation stages

Stages transform a **list of documents**. Expression operators calculate a value inside a document. The same name can have different syntax in these contexts.

These pages describe the 21 registered Core stages. They are not a list of Studio palette steps. For the authoring UI, use the [Flow step reference](steps.md). SrotaX normally processes one request document; use array expressions such as `$map` and `$sortArray` to transform its lists.

Each page includes a runnable pipeline, actual Core output, and implementation limits. The stage examples are separate from the 6,495-case expression parity suite.

| Stage | Purpose |
| --- | --- |
| [$match](stages/match.md) | Retains documents that satisfy a condition object. |
| [$addFields](stages/addFields.md) | Adds or replaces fields while retaining other fields. |
| [$set](stages/set.md) | Adds or replaces fields while retaining other fields. |
| [$project](stages/project.md) | Builds each output document from explicitly selected or computed fields. |
| [$unset](stages/unset.md) | Removes named fields from each document. |
| [$limit](stages/limit.md) | Keeps the first N documents. |
| [$skip](stages/skip.md) | Drops the first N documents. |
| [$sort](stages/sort.md) | Orders documents by one or more fields. |
| [$unwind](stages/unwind.md) | Produces one document for each element of an array field. |
| [$replaceRoot](stages/replaceRoot.md) | Replaces the entire document with an object expression. |
| [$replaceWith](stages/replaceWith.md) | Replaces the entire document with an object expression. |
| [$group](stages/group.md) | Combines documents sharing a grouping key and computes accumulator outputs. |
| [$sortByCount](stages/sortByCount.md) | Counts documents per grouping value and sorts groups by descending count. |
| [$bucket](stages/bucket.md) | Groups numeric values into explicit lower-inclusive, upper-exclusive ranges. |
| [$bucketAuto](stages/bucketAuto.md) | Divides the numeric value range into equal-width buckets. |
| [$facet](stages/facet.md) | Runs named child pipelines over the same input list and collects their results. |
| [$lookup](stages/lookup.md) | Adds matching records from a host-provided in-memory dataset. |
| [$densify](stages/densify.md) | Inserts documents for missing numeric or date positions. |
| [$fill](stages/fill.md) | Replaces null or missing values using a value expression or interpolation. |
| [$setWindowFields](stages/setWindowFields.md) | Adds values computed over an ordered partition of documents. |
| [$subPipeline](stages/subPipeline.md) | Executes inline child pipelines or resolves child references through the caller’s execution context. |

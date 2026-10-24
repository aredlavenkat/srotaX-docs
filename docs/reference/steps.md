# Flow step reference

Configure steps using available contract fields and compatible local destinations. This is a task reference for Studio operations; it is not a promise that every MongoDB aggregation stage is exposed.

| Step | Purpose | Important configuration |
| --- | --- | --- |
| Request | Start with the incoming document | Input contract |
| Validate Data | Check required values and types | Fields to validate and behavior |
| Set Fields | Assign fixed values, copies, or expressions | Destination and source/expression; never write `input.*` |
| Choose Fields | Select the fields retained in a working/result object | Source and retained fields; input remains immutable |
| Transform Each Item | Map list items | Source list, item expression/mapping, destination |
| Filter List | Keep matching items | Source list, item conditions, destination |
| Flatten List | Flatten nested lists | Source and destination |
| Sort List | Order list items | Sort fields/directions; in-place only for local lists |
| Trim List | Keep a range or count | Source, range/count, destination |
| Aggregate List | Calculate a list summary | List, operation, value field, destination |
| Check Exists | Test whether matching items exist | List, predicate, boolean destination |
| Lookup | Read reference-data values | Dataset/version, key mapping, result destination |
| If / Else | Route by conditions | Conditions and complete outgoing branches |
| Decision Table / Decision Tree | Call a decision asset | Dependency, input mappings, result destination |
| Call Flow | Call a reusable Flow | Dependency, input mappings, result destination |
| Response | Return the chosen response | Response mapping/shape compatible with Outputs |

Do not infer support for collection-level stages such as `$merge` or `$out` from MongoDB documentation. Use the editor's actual palette and validate the completed Flow. Operator registration alone does not establish that a stage is available in Studio.

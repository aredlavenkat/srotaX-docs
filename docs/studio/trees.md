# Build a Decision Tree

Use a tree when decisions are naturally expressed as branches. Begin with the start node, add conditions, connect each outcome to a result or another condition, and define the returned output fields on result nodes.

For a shipping example, branch on `input.subtotal >= 100`: the yes result returns fee 0, and the no result returns fee 9. Both return method Standard.

Test one input for every result leaf, including exact thresholds. Use **Result** to verify returned values and **Trace** to inspect execution. The graph indicates the executed path; do not interpret tile colour alone as evidence of execution.

On Main, graph zoom and navigation remain available. Adding conditions or results requires an editable change set. A missing branch or invalid output is a validation problem, not an instruction for the runtime to invent a result.

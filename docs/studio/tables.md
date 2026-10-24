# Write a Decision Table

Use a table when business rules fit rows of conditions and results. Define Inputs and Outputs in Data Contract first, then choose those fields when adding columns.

## Evaluation order matters

Rows run top-to-bottom. The first matching row supplies the result. A rule `subtotal < 50` placed below `subtotal < 100` cannot win for a subtotal of 25: the broader earlier row already matches. Put the more specific rule first or make the conditions disjoint.

Result cells can assign values or use the supported editing modes. Choose types that match the output contract. Do not rely on JSON strings being silently converted into numbers at runtime.

## Inspect and test

Use the shared Test Panel. **Result** shows output, **Trace** identifies the matched row, and **Issues** explains failures. Test each rule and exact thresholds, plus missing and wrong-type inputs. See the [shipping walkthrough](../quickstart.md).

On Main, adding rows and columns is disabled. Search remains available for inspection. Select an editable change set to change the table. Save Draft persists editor changes; Run Test in a change set includes unsaved changes.

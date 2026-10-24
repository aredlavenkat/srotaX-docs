# Reuse Models

A Model is a named object schema in a workspace. Use it when multiple contracts or nested objects share a structure, such as an Address. Models have a flat namespace; there are no model packages in this version.

## Create and reference

1. Select an editable change set and open **Models**.
2. Create a model, give it a name, and define its fields using **Fields** or **JSON**.
3. Save the model draft.
4. Open an asset's Data Contract and choose the model on an object row or as the item schema of an object list.

Studio and Models use the same field editor. Referenced children are shown for inspection, not copied into the consuming contract's authoring definition.

## When a model changes

Consumers resolve the current model in their selected change set, falling back to Main when it has not been edited there. The editor refreshes referenced fields on focus and periodically while a change-set editor is active; this is not instant collaborative streaming.

Merging a model change validates and recompiles affected Main consumers. A field removal or incompatible type change can block the merge until its consuming rules are fixed. Existing executable versions and releases retain their resolved model definitions.

There is no **Update from model** button or user-facing version selector. Internal immutable revisions still exist for reproducibility.

## Import OpenAPI components

Open the import dialog, supply an OpenAPI document, select component schemas with the checkboxes (or **Select all**), and import the selected models. The eye icon previews a schema. Select every referenced component that is not already available under a matching name.

If matching names exist, **Overwrite existing models** replaces their fields and description inside the current change set while preserving their IDs. Review consumers before merging. Import is atomic: unsupported keywords, missing references, or cycles reject the operation.

Import translates component names into stable model-ID `$ref` values. Export translates those IDs back to readable component names in one OpenAPI document. Renaming a model therefore does not change its consumers' stored references.

Only the [supported schema subset](../reference/schemas.md) is accepted; “OpenAPI import” does not mean all OpenAPI schema features are supported.

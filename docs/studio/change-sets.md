# Work in a change set

Main is the shared integrated state and is read-only in the editors. A change set stores your touched drafts and organizational edits until merge.

1. Create and select a change set.
2. Edit and **Save Draft** for each intended asset or model.
3. Test and validate.
4. Inspect the comparison against Main.
5. Resolve content conflicts, then merge.

Merge validates and creates immutable versions of changed executable assets. Shared model changes can also require revalidation and recompilation of consumers. Failed validation must be fixed before merge succeeds.

## Understand isolation

A change set does not copy every asset and folder when it is created. It stores overrides for touched resources. Untouched folders follow later Main merges; your unmerged folder edits remain private. Do not treat a change set as a fully frozen copy of the workspace.

Folder structure changes do not present content-conflict resolution; the merge applies recorded organizational edits with structural validation. Asset and model content conflicts still require resolution. See [Catalog](catalog.md).

## Save, merge, release, activate

| Action | Effect |
| --- | --- |
| Save Draft | Persists editable work in the change set |
| Merge | Integrates changes into Main and creates immutable resource versions |
| Create release | Captures the complete Main revision |
| Activate | Selects a release for an environment's runtime calls |

Do not use “published version” as a synonym for “currently running in Production.”

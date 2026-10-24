# Verification and boundaries

This documentation was built against the current local SrotaX code and running services on 2026-10-23/24. The source repositories contain uncommitted work, so a Git commit alone does not identify this exact build. File fingerprints and the operator catalog snapshot are recorded under `verification/` and `reference/`.

## Shipping journey

`scripts/verify-journey.mjs` ran against a disposable PostgreSQL database with fixture identity and real Management and Runtime HTTP servers. It verified creation, schema persistence, validation, five preview cases, merge, immutable version retrieval, release creation, activation, five runtime cases, release-linked history, wrong-type failures, invalid-key denial, and the Java HTTP client.

Fixture authentication is test-only. This does not test Google/Microsoft identity providers, production infrastructure, or a customer's permissions configuration. No existing customer release was activated or overwritten.

Browser verification additionally loaded the published table and contract, generated example input, ran the test successfully, confirmed **Row 2 matched**, and checked Development activation. The quickstart screenshots come from this disposable workspace. Creation, merge, and activation were exercised through HTTP, not by clicking every Studio action.

## Operator reference

The reference is generated from the actual Management operator catalog. Metadata reports compatibility classifications, source revision, null/missing behavior, signatures, and limitations. These are attributed as **engine metadata**, not independently certified MongoDB equivalence.

The suite has **23 successful compiler/engine examples and one reproduced known failure**.

Selected runnable expression examples are checked against the compiler and engine by `scripts/verify-expressions.sh`. They do not certify every registered operator or every BSON type. A full MongoDB differential suite remains separate work; the documentation does not claim it has passed.

## Build checks

Local Markdown links and JSON examples are checked by `scripts/check.py`. MkDocs strict build validates navigation. The CI workflow repeats these checks; the fixture journey requires a sibling backend build and is documented separately.

## Known gaps surfaced

- A literal-array `$size` expression compiled but failed during execution (`$size requires one argument`). Its operator page and regression fixture record this limitation.
- Older backend ad-hoc E2E scripts still contain tuple-shaped input fixtures. This new walkthrough uses nested schemas and does not reuse those obsolete payloads.
- Runtime OpenAPI currently has a generic response schema rather than an exhaustive typed failure contract.
- Direct Java embedding and broad MongoDB semantic parity are not certified by this documentation.

## Illustrated guide evidence

The Studio guides include real screenshots from a disposable BrowserFixture, using synthetic shipping and address data. The shipping management/runtime journey was rerun for this update. The additional Tree and Flow examples were prepared with `scripts/seed-visual-guides.mjs`; preview calls returned fee 9 / Standard and total 84 respectively for subtotal 75. These checks cover those inputs, not every branch or UI interaction.

Screenshots demonstrate the Catalog, change-set selection, contract reference, Models editor, OpenAPI selection dialog, Tree branches and condition drawer, and a simple Flow. They are not a claim that every illustrated task has a complete automated browser test.

## Order fulfillment walkthrough

`verification/fulfillment.json` records four successful draft inputs, two rejected inputs, and nested execution trace checks for the reconstructed Main example. The main Flow also succeeded through Studio with the documented sample request. Merge of this example failed with `Invalid compiled artifact` while constructing reference-data metadata, so release creation and activation are not certified for this walkthrough. The original workspace was only read; test mutations were confined to a disposable fixture.

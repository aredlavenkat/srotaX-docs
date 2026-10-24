# Release and activate

A release is an immutable snapshot of one complete workspace Main revision. Merge your change set before creating it. Creating again for the same Main revision returns the existing release.

Review all included assets and dependencies. A release is not a selected subset of just the Flow you were editing. It captures the exact compiled definitions and model snapshots used by its assets.

## Activate an environment

Development and Production each select one release. Activation replaces the environment's active release atomically. Runtime API keys are scoped to an environment, so the same decision ID may produce different results in Development and Production.

Creating a release alone does not activate it. An asset unavailable in the environment's active release cannot be executed there.

## Roll back

Activate a previous release for that environment. Rollback switches the complete snapshot; it does not selectively undo one asset. To combine an older rule with newer unrelated rules, author the desired combination in a change set, merge, and create a new release.

Main and existing releases are not edited by activation. Requests already executing use the release snapshot they resolved for that invocation.

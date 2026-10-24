# Maintain verified documentation

Start from current Studio and backend code. Use tests and screenshots as evidence. Existing internal design notes may describe superseded behavior.

## Refresh operators

Fetch the catalog from the build you are documenting (no credentials are needed by this endpoint):

```sh
curl --fail http://localhost:8080/api/operator-catalog -o reference/operator-catalog.json
python scripts/generate-reference.py
python scripts/check.py
mkdocs build --strict
```

Do not turn metadata compatibility classifications into independent parity claims. Add normal, boundary, missing/null, and error examples to `examples/expressions.json` as coverage grows. An `expectedError` entry records a known reproducible product limitation, not successful operator behavior.

## Verify expressions

Build the sibling backend and its test classpath first, then:

```sh
export JAVA_HOME=/path/to/jdk-21
sh scripts/verify-expressions.sh
python scripts/generate-reference.py
```

The script expects `../srotax-backend`; override `SROTAX_BACKEND_DIR` if needed. It uses the built compiler and engine JARs. This is not a MongoDB differential test.

## Verify the shipping lifecycle

Use a fresh disposable backend fixture. Never point this script at an ordinary database or production service. The fixture uses a test-only identity provider and non-superuser application roles.

In a backend terminal:

```sh
export JAVA_HOME=/path/to/jdk-21
export SROTAX_FIXTURE_RUNTIME_JAR="$PWD/srotax-runtime-app/target/srotax-runtime-app-0.1.0-SNAPSHOT.jar"
sh scripts/browser-fixture.sh /tmp/srotax-docs-fixture-port
```

The backend build requires Maven and its existing engine dependency. Runtime binds loopback port 8097; ensure it is free. In this repository, with Node 22+:

```sh
node scripts/verify-journey.mjs /tmp/srotax-docs-fixture-port
```

This creates a table, tests five cases, merges, creates/activates a disposable release, checks failures, and runs the Java sample. It keeps temporary keys in process memory and never writes them to reports. Stop the fixture afterward to discard its database. Reruns require a new fixture because Main must start at revision 0.

For real Studio screenshots, start a separate Studio instance with `SROTAX_MANAGEMENT_TARGET` pointing at the fixture's port and `SROTAX_RUNTIME_TARGET=http://127.0.0.1:8097`. Sign in through its fixture login. Do not reuse customer assets or reload an editor with unsaved work. Record whether verification was via HTTP, browser, or direct compiler execution.

## Release coordination

Before publishing a docs release, refresh the source fingerprints, operator catalog and verification evidence against the actual released application build. The current evidence includes a working-tree state with uncommitted changes; it is not a tagged product support matrix. CI checks documentation structure, while the fixture journey needs the sibling backend. After those checks pass on `main`, the deployment job publishes to `gh-pages`, which GitHub Pages serves at `docs.srotax.com`. Pull requests never deploy.

## Illustrated Studio guides

Use real Studio screenshots from the disposable BrowserFixture, never customer data. Start each guide with an outcome and prerequisites; place screenshots next to numbered actions, then include an expected result and common failure. Link each image to its original so labels remain readable. Keep operator references focused on executable examples rather than decorative screenshots.

After running `scripts/verify-journey.mjs <port-file>` against a fresh fixture, run `scripts/seed-visual-guides.mjs <port-file>` once to prepare the Tree, Flow, shared Address model, and Catalog examples. This verifies Tree and Flow preview outputs and writes ignored `target/visual-guide-context.json`. Capture through Studio against that fixture. The seed script is for a disposable database, not an existing workspace.

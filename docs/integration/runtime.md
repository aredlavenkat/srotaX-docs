# Runtime API

Send one JSON document to:

```text
POST /api/runtime/decisions/{decisionId}/execute
Authorization: Bearer <runtime-api-key>
Content-Type: application/json
```

The key determines organisation, workspace, and environment. Do not send those as body fields to select another scope. The request body is the decision's input document.

## Successful execution

The response includes `success`, `data`, and execution metadata such as `runId`. Check `success` before using `data`; preserve `runId` for troubleshooting. Do not assume every HTTP 200 is a successful decision evaluation.

## Verified failure cases

| Case | Observed behavior |
| --- | --- |
| Invalid API key | HTTP 401 |
| No active release containing the asset | HTTP 404 |
| Wrong type for required input | Failed execution; no successful result |

These cases are verified by the documentation walkthrough. Other limits and error details are deployment-specific; do not treat this table as an exhaustive HTTP error schema.

The runtime OpenAPI document currently describes a generic response object. Applications should not assume an undocumented exhaustive generated error model. The source snapshot is `reference/runtime-openapi.json` in the documentation repository.

[Download the runtime OpenAPI snapshot](../downloads/runtime-openapi.json).

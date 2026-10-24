# Supported schema format

Models and contract sections use nested OpenAPI-style Schema Objects. The supported subset is intentionally narrower than unrestricted OpenAPI or JSON Schema.

```json
{
  "type": "object",
  "properties": {
    "subtotal": {"type": "number", "example": 75},
    "customer": {
      "type": "object",
      "properties": {"name": {"type": "string"}},
      "required": ["name"]
    },
    "items": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["subtotal"]
}
```

| Feature | Supported representation |
| --- | --- |
| Object | `type: object`, `properties`, optional `required` array |
| Scalar | `string`, `number`, `boolean` |
| Date/time | `type: string`, `format: date-time` |
| List | `type: array`, `items` schema; `{}` permits unspecified item type |
| Metadata | `title`, `description`, `example` where accepted |
| Model reference | `$ref: #/components/schemas/{modelId}` |

Stored refs use model UUIDs, not names. OpenAPI import/export converts readable external component names at the boundary. `$ref` objects cannot add sibling custom fields. Examples must match scalar types.

Unsupported keywords are rejected, including unrestricted `oneOf`, `allOf`, `anyOf`, `enum`, validation constraints such as `minimum`, and arbitrary `additionalProperties`. Use a decision or validation step for business constraints supported by the editor. `integer` is not a separate accepted scalar type here; use `number`.

Property names must match `[A-Za-z_][A-Za-z0-9_]*`. The current parser enforces a 64-field limit and nesting checks; model resolution also checks expanded references and cycles. Do not use recursive schemas.

This page is derived from `srotax-core/SchemaContracts.java` and model resolution, not a claim of full OpenAPI conformance.

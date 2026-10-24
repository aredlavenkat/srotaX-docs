# Call SrotaX from Java

Use Java's HTTP client to execute a decision through the Runtime API. This approach does not embed the engine or require a SrotaX SDK.

## Prerequisites

Merge the decision, create a release, activate it in the API key's environment, and obtain that environment's key. Use the decision's stable ID, not its display name. Set these environment variables through your deployment's secret configuration:

- `SROTAX_RUNTIME_URL`: runtime origin, for example `https://runtime.example.com`.
- `SROTAX_DECISION_ID`: decision UUID.
- `SROTAX_API_KEY`: runtime key. Do not put it in frontend code or source control.

The repository's `examples/java/ShippingClient.java` works on Java 17+ and was executed with Java 21 against the disposable runtime.

```sh
java examples/java/ShippingClient.java
```

The sample sends `{"subtotal":75}` and prints the JSON response. It checks HTTP status; your application must also parse the response using its JSON library and check **`success == true`** before using **`data`**. For the shipping example, `data` is `{"fee":9,"method":"Standard"}`.

[Download ShippingClient.java](../downloads/ShippingClient.java)

```java
import java.net.URI;
import java.net.http.*;
import java.time.Duration;

/** Java 17+; API key stays in the environment. The response is a JSON envelope. */
public class ShippingClient {
    public static void main(String[] args) throws Exception {
        String base = required("SROTAX_RUNTIME_URL").replaceAll("/$", "");
        String decision = required("SROTAX_DECISION_ID");
        var client = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(5)).build();
        var request = HttpRequest.newBuilder(URI.create(base + "/api/runtime/decisions/" + decision + "/execute"))
            .timeout(Duration.ofSeconds(30))
            .header("Authorization", "Bearer " + required("SROTAX_API_KEY"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString("{\"subtotal\":75}"))
            .build();
        var response = client.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new IllegalStateException("SrotaX HTTP status " + response.statusCode());
        }
        // The calling application must also parse and check `success` before using `data`.
        System.out.println(response.body());
    }
    private static String required(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) throw new IllegalArgumentException("Missing " + name);
        return value;
    }
}
```

## Handle failures

A transport failure or timeout is not a business result. An HTTP 200 response may still describe a failed execution. Keep these paths distinct. See [Runtime API](runtime.md).

The sample uses a 5-second connection timeout and 30-second request timeout as example client settings; these do not configure server limits. Choose them based on your deployment. Do not blindly retry a Flow containing external side effects: a timeout does not prove it never ran.

## Embedding is a separate integration

This guide verifies remote execution only. Direct JVM engine embedding does not automatically provide SrotaX release loading, workspace permissions, API-key scope, reference data, or dependency resolution. A supported embedding contract needs separate verification before it belongs in this guide.

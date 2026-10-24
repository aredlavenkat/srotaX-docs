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

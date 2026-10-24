import com.fasterxml.jackson.databind.*;
import com.srotax.compiler.*;
import com.srotax.engine.*;
import java.nio.file.*;
import java.util.*;
public class VerifyExpressions {
 public static void main(String[] args)throws Exception {
  var json=new ObjectMapper();var compiler=new Expressions(json,ConditionRecipes.catalog(json,FluxionOperatorCatalog.read(json)));
  var report=new ArrayList<Object>();
  for(var test:json.readTree(Files.readString(Path.of("examples/expressions.json")))){
   try {
   var compiled=compiler.compile(json.createObjectNode().put("kind","mongo").put("json",test.get("expression").toString()),Map.of());
   var result=new FluxionDocumentExecutor().execute(UUID.randomUUID(),UUID.randomUUID(),json.writeValueAsString(List.of(Map.of("$project",Map.of("_id",0,"value",compiled.expression())))),Map.of());
   var actual=json.valueToTree(result.get("value"));var expected=test.get("expected");
   boolean equal=actual.isNumber()&&expected.isNumber()?actual.decimalValue().compareTo(expected.decimalValue())==0:actual.equals(expected);
   if(!equal)throw new AssertionError(test.get("operator")+": expected "+expected+", got "+actual);
   if(test.has("expectedError"))throw new AssertionError("Known limitation changed; update docs: "+test.get("operator"));
   report.add(Map.of("operator",test.get("operator").asText(),"compiled",true,"executed",true));
   } catch (IllegalArgumentException e) {
    if(!test.has("expectedError")||!e.getMessage().contains(test.get("expectedError").asText()))throw e;
    report.add(Map.of("operator",test.get("operator").asText(),"executed",false,"knownFailure",e.getMessage()));
   }
  }
  Files.createDirectories(Path.of("verification"));json.writerWithDefaultPrettyPrinter().writeValue(Path.of("verification/expressions.json").toFile(),report);
  System.out.println("PASS: "+report.size()+" compiler + engine checks (including known-failure regression)");
 }
}

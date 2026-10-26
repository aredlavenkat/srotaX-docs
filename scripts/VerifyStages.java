import ai.fluxion.core.engine.PipelineExecutor;
import ai.fluxion.core.model.Document;
import ai.fluxion.core.model.Stage;
import com.fasterxml.jackson.databind.*;
import java.nio.file.*;
import java.util.*;

/** Executes documentation cases with a fresh Core pipeline context per case. */
public class VerifyStages {
 public static void main(String[] args) throws Exception {
  var json=new ObjectMapper();var results=json.createArrayNode();
  for(var test:json.readTree(Files.readString(Path.of("examples/stages.json")))){
   var row=((com.fasterxml.jackson.databind.node.ObjectNode)test).deepCopy();
   try {
    List<Document> input=new ArrayList<>();
    for(var d:test.path("input"))input.add(new Document(json.convertValue(d,LinkedHashMap.class)));
    List<Stage> pipeline=new ArrayList<>();
    for(var stage:test.path("pipeline"))pipeline.add(new Stage(json.convertValue(stage,LinkedHashMap.class)));
    var output=new PipelineExecutor().execute(input,pipeline);
    row.set("result",json.valueToTree(output.stream().map(Document::getData).toList()));
   }catch(Exception e){row.put("error",e.getClass().getSimpleName());row.put("message",Objects.toString(e.getMessage(),""));}
   results.add(row);
  }
  var destination=Path.of("verification/stage-behavior.json");
  if(Arrays.asList(args).contains("--record"))json.writerWithDefaultPrettyPrinter().writeValue(destination.toFile(),results);
  else {
   var baseline=json.readTree(Files.readString(destination));
   var actual=json.readTree(json.writeValueAsString(results));
   if(!baseline.equals(actual)) {
    for(int i=0;i<actual.size();i++)if(i>=baseline.size()||!baseline.get(i).equals(actual.get(i)))System.err.println("Changed case: "+actual.get(i));
    throw new AssertionError("Stage behavior changed; review the cases before updating the documentation evidence");
   }
  }
  System.out.println("PASS: "+results.size()+" stage documentation cases");
 }
}

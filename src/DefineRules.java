import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.reasoner.*;
import org.apache.jena.reasoner.rulesys.GenericRuleReasoner;
import org.apache.jena.reasoner.rulesys.Rule;
import org.apache.jena.util.FileManager;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;


public class DefineRules {
    public static void main(String[] args) {
        try {
        // load KG data
        String inputFileName = "../data/WiSoKG_distorted.ttl";

        Model model = ModelFactory.createDefaultModel();
        FileManager.get().readModel(model, inputFileName);

        // define reasoning rules
        String rules =
            // Rule 2_1: All People and the Devices they own (2 Hop)
            "[personDeviceRule: (?person <https://schema.org/workLocation> ?place) " +
            "                   (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                    -> (?person <http://example.com/ontology#ownsDevice> ?device)] " +

            // Rule 2_2: All Storeys and the Devices contained in them (2 Hop)
            "[storeyDeviceRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                   (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                    -> (?storey <http://example.com/ontology#containsDevice> ?device)] " +


            // Rule 3_1: All People in All Rooms and the Lights they own (Device filter: 3 Hop)
            "[personLightRule: (?person <https://schema.org/workLocation> ?place) " +
            "                  (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                  (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "                   -> (?person <http://example.com/ontology#ownsLight> ?device)] " +

            // Rule 3_2: All People in All Offices and the Devices they own (Room filter: 3 Hop)
            "[personOfficeDeviceRule: (?person <https://schema.org/workLocation> ?place) " +
            "                         (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                         (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                          -> (?person <http://example.com/ontology#ownsOfficeDevice> ?device)] " +

            // Rule 3_3: All RAs in All Rooms and the Devices they own (Person filter: 3 Hop)
            "[RADeviceRule: (?person <https://schema.org/workLocation> ?place) " +
            "               (?place <https://w3id.org/bot#containsElement> ?device) " +
            "               (?person <https://schema.org/jobTitle> 'Research Assistant') " +
            "                -> (?person <http://example.com/ontology#RAownsDevice> ?device)] " +

            // Rule 3_4: All Storeys and the Lights contained in them (Device filter: 3 Hop)
            "[storeyLightRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                  (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                  (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "                   -> (?storey <http://example.com/ontology#containsLight> ?device)] " +

            // Rule 3_5: All Storeys and the Office Devices contained in them (Room filter: 3 Hop)
            "[storeyOfficeDeviceRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                         (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                         (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                          -> (?storey <http://example.com/ontology#containsOfficeDevice> ?device)] " +

            // Rule 3_6: All Devices contained in Storey 4 (Storey filter: 3 Hop)
            "[storey4DeviceRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                    (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                    (?storey <http://www.w3.org/2000/01/rdf-schema#label> 'WiSo 4th Floor') " +
            "                     -> (?storey <http://example.com/ontology#storey4ContainsDevice> ?device)] " +


            // Rule 4_1: All Research Assistants and the Lights they own (Person-Device: 4 Hop)
            "[RALightRule: (?person <https://schema.org/workLocation> ?place) " +
            "              (?place <https://w3id.org/bot#containsElement> ?device) " +
            "              (?person <https://schema.org/jobTitle> 'Research Assistant') " +
            "              (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "               -> (?person <http://example.com/ontology#RAownsLight> ?device)] " +

            // Rule 4_2: All Research Assistants in Offices and the Devices they own (Person-Room filter: 4 Hop)
            "[RAOfficeDeviceRule: (?person <https://schema.org/workLocation> ?place) " +
            "                     (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                     (?person <https://schema.org/jobTitle> 'Research Assistant') " +
            "                     (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                      -> (?person <http://example.com/ontology#RAownsOfficeDevice> ?device)] " +

            // Rule 4_3: All People in Offices and the Lights they own (Room-Device filter: 4 Hop)
            "[personOfficeLightRule: (?person <https://schema.org/workLocation> ?place) " +
            "                  (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                  (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                  (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "                   -> (?person <http://example.com/ontology#ownsOfficeLight> ?device)] " +

            // Rule 4_4: All Offices in Storey 4 and the Devices contained in them (Storey-Room filter: 4 Hop)
            "[storey4OfficeDeviceRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                          (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                          (?storey <http://www.w3.org/2000/01/rdf-schema#label> 'WiSo 4th Floor') " +
            "                          (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                           -> (?storey <http://example.com/ontology#storey4ContainsOfficeDevice> ?device)] " +

            // Rule 4_5: All Lights contained in Storey 4 (Storey-Device filter: 4 Hop)
            "[storey4LightRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                   (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                   (?storey <http://www.w3.org/2000/01/rdf-schema#label> 'WiSo 4th Floor') " +
            "                   (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "                    -> (?storey <http://example.com/ontology#storey4ContainsLight> ?device)] " +

            // Rule 4_6: All Offices in All Storeys and the Lights contained in them (Room-Device filter: 4 Hop)
            "[storeyOfficeLightRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                        (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                        (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                        (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "                         -> (?storey <http://example.com/ontology#containsOfficeLight> ?device)] " +


             // Rule 5_1: All Research Assistants in Offices and the Lights they own (Person-Room-Device filter: 5 Hop)
            "[RAOfficeLightRule: (?person <https://schema.org/workLocation> ?place) " +
            "                    (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                    (?person <https://schema.org/jobTitle> 'Research Assistant') " +
            "                    (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                    (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "                     -> (?person <http://example.com/ontology#RAownsOfficeLight> ?device)] " +

            // Rule 5_2: All Offices in Storey 4 and the Lights contained in them (Storey-Room-Device filter: 5 Hop)
            "[storey4OfficeLightRule: (?storey <https://w3id.org/bot#hasSpace> ?place) " +
            "                         (?place <https://w3id.org/bot#containsElement> ?device) " +
            "                         (?storey <http://www.w3.org/2000/01/rdf-schema#label> 'WiSo 4th Floor') " +
            "                         (?place <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Office>) " +
            "                         (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) " +
            "                          -> (?storey <http://example.com/ontology#storey4ContainsOfficeLight> ?device)] ";


        // create a reasoner with the combined rules
            Reasoner reasoner = new GenericRuleReasoner(Rule.parseRules(rules));
            InfModel infModel = ModelFactory.createInfModel(reasoner, model);

            // SPARQL queries for each rule type
            String[] queries = {
                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:ownsDevice ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:containsDevice ?device }",


                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:ownsLight ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:ownsOfficeDevice ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:RAownsDevice ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:containsLight ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:containsOfficeDevice ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:storey4ContainsDevice ?device }",



                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:RAownsLight ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:RAownsOfficeDevice ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:ownsOfficeLight ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:storey4ContainsOfficeDevice ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:storey4ContainsLight ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:containsOfficeLight ?device }",



                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?person ?device WHERE { ?person ex:RAownsOfficeLight ?device }",

                "PREFIX ex: <http://example.com/ontology#> " +
                "SELECT ?storey ?device WHERE { ?storey ex:storey4ContainsOfficeLight ?device }"
            };

        // rule descriptions for print out to txt file
        String[] ruleTypes = {
            "Rule 2_1: All People and the Devices they own (2 Hop)",
            "Rule 2_2: All Storeys and the Devices contained in them (2 Hop)",
            "Rule 3_1: All People in All Rooms and the Lights they own (Device filter: 3 Hop)",
            "Rule 3_2: All People in All Offices and the Devices they own (Room filter: 3 Hop)",
            "Rule 3_3: All RAs in All Rooms and the Devices they own (Person filter: 3 Hop)",
            "Rule 3_4: All Storeys and the Lights contained in them (Device filter: 3 Hop)",
            "Rule 3_5: All Storeys and the Office Devices contained in them (Room filter: 3 Hop)",
            "Rule 3_6: All Devices contained in Storey 4 (Storey filter: 3 Hop)",
            "Rule 4_1: All Research Assistants and the Lights they own (Person-Device: 4 Hop)",
            "Rule 4_2: All Research Assistants in Offices and the Devices they own (Person-Room filter: 4 Hop)",
            "Rule 4_3: All People in Offices and the Lights they own (Room-Device filter: 4 Hop)",
            "Rule 4_4: All Offices in Storey 4 and the Devices contained in them (Storey-Room filter: 4 Hop)",
            "Rule 4_5: All Lights contained in Storey 4 (Storey-Device filter: 4 Hop)",
            "Rule 4_6: All Offices in All Storeys and the Lights contained in them (Room-Device filter: 4 Hop)",
            "Rule 5_1: All Research Assistants in Offices and the Lights they own (Person-Room-Device filter: 5 Hop)",
            "Rule 5_2: All Offices in Storey 4 and the Lights contained in them (Storey-Room-Device filter: 5 Hop)"
        };

         // write output to txt file
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("all_inferred_output.txt"))) {
                for (int i = 0; i < queries.length; i++) {
                    writer.write("==== " + ruleTypes[i] + " ====" + System.lineSeparator());

                    Query query = QueryFactory.create(queries[i]);
                    try (QueryExecution qe = QueryExecutionFactory.create(query, infModel)) {
                        ResultSet results = qe.execSelect();

                        while (results.hasNext()) {
                            QuerySolution solution = results.nextSolution();
                            writer.write(solution.toString() + System.lineSeparator());
                        }
                    }
                    writer.write(System.lineSeparator());
                }
            }

            System.out.println("Inferred results written to all_inferred_output.txt");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

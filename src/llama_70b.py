from openai import OpenAI

# load kg file
with open('WiSoKG_distorted.ttl', 'r', encoding='utf-8') as file:
    kg = file.read()
#print(kg)

rule_1_jena = """[personDeviceRule: (?person <https://schema.org/workLocation> ?place) " +
                (?place <https://w3id.org/bot#containsElement> ?device) " +
                -> (?person <http://example.com/ontology#ownsDevice> ?device)];"""
rule_2_1 = """ If a person work at a place and the place has devices, then the person has the devices."""
rule_2_2 = """ If a storey has rooms and the rooms have devices, then the storey has the devices"""


client = OpenAI(
base_url = "URL",
api_key= "KEY",
)

response = client.chat.completions.create(
      model="llama3.1:70b",
      temperature=0,
      messages=[
      {"role": "system",  "content": "You are an assistant that helps with reasoning over knowledge graphs."},
      {"role": "user", "content": f'''
       Given the following knowledge graph in Turtle format:

        {kg}

       
        Question: give me a list of all Offices in Storey 3 and the Heaters contained in them.
        
        '''
    }
      ]
)
print(response.choices[0].message.content) 


"""
prompt test:
# CoT: Do not include SPARQL queries. Think step by step.
# Do not include SPARQL queries, intermediate reasoning steps, intermediate reasoning steps, or explanations in the result.
Your answer must only contain the final results in the format:
        - person: URI, device: URI.  
        Do not include SPARQL queries. Think step by step.
"""

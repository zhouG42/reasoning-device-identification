from transformers import pipeline
import openai

openai.api_key = "KEY"

# load kg file
with open('WiSoKG_distorted.ttl', 'r', encoding='utf-8') as file:
    kg = file.read()


# # Reasoning rules
# rule_1 = """If a room contains an element, then the element is contained in that room."""
# #rule_2 = """If a container has a sub-space that contains an element, the container indirectly contains that element."""
# rule_1_jena = """
# [personDeviceRule: (?person <https://schema.org/workLocation> ?room) 
#                    (?room <https://w3id.org/bot#containsElement> ?device)
#                    (?device <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology#Light>) 
#                 -> (?person <http://example.com/ontology#hasDevice> ?device)] 
# """

# rule_2 = """
# [indirectContainmentRule: (?container <https://w3id.org/bot#hasSpace> ?subSpace)
#                            (?subSpace <https://w3id.org/bot#containsElement> ?element)
#                         -> (?container <https://w3id.org/bot#indirectlyContains> ?element)]
# """


messages = [
    {"role": "system", "content": "You are an assistant that helps with reasoning over knowledge graphs."},
    {"role": "user", "content": f""" Given the following knowledge graph in Turtle format:

        {kg}

        Question: give me a list of all Offices in Storey 3 and the Lights contained in them.
    """}
]

response = openai.ChatCompletion.create(
    #model="gpt-3.5-turbo",
    model="gpt-4",
    #model="o1-mini",
    #model = "gpt-4o-mini",          # options: "gpt-3.5-turbo", "gpt-4" (most expensive),  "gpt-4o", "gpt-4o-mini", ["o1-preview","o1-mini","o1-preview-2024-09-12"(for reasoning, not available in api call)]
    messages=messages,
    max_tokens=1000,          
    temperature=0         
)


print("LLM Output:", response['choices'][0]['message']['content'].strip())

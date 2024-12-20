import anthropic

API_KEY = "KEY"

# load kg file
with open('WiSoKG_distorted.ttl', 'r', encoding='utf-8') as file:
    kg = file.read()

# Initialize the Anthropic client with your API key
client = anthropic.Anthropic(api_key=API_KEY)

# Send a prompt to Claude
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",  # choose one of: claude-3-haiku-20240307, claude-3-5-sonnet-20241022
    max_tokens=1500,
    temperature=0,
    messages=[
        {"role": "user", "content": f"""You are an assistant that helps with reasoning over knowledge graphs.
         
        Given the following knowledge graph in Turtle format:

        {kg}

        Question: give me a list of all Offices in Storey 3 and the Lights contained in them. 
"""}
    ]
)


""" prompt test
# Your answer must only contain the final results in the format: - storey: URI, device: URI. Do not include SPARQL queries, intermediate reasoning steps, intermediate reasoning steps, or explanations in the result.
#, intermediate reasoning steps, or explanations in the result.
#. Think step by step.
"""


# Print the response
print(response.content[0].text)

import bard

# Create a Bard client
client = bard.Client()

# Send a text prompt to Bard
prompt = "Write a poem about a cat"
response = client.send_text_prompt(prompt)

# Print the response
print(response)

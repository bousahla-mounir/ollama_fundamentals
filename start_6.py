from openai import OpenAI
#from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

resp = client.chat.completions.create(
    model="llama3.2:latest",
    messages=[{"role": "user", "content": "Explain Linux"}],
)

print(resp.choices[0].message.content)
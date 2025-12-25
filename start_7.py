from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

stream = client.chat.completions.create(
    model="llama3.2:latest",
    messages=[
        {"role": "system", "content": "You are a Linux expert."},
        {"role": "user", "content": "Explain what a kernel is."}
    ],
    temperature=0.7,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print("\n--- done ---")
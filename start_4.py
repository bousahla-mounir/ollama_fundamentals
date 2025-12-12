
import ollama

res = ollama.chat(
    model="deepseek-r1:32b",
    messages=[
        { "role":"user", "content":"Why is the ocean so salty ?" }
    ],
    stream=True
)

for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)
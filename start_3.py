
import ollama

res = ollama.chat(
    model="llama3.2:latest",
    messages=[
        { "role":"user", "content":"Why is the sky blue ?" }
    ]
)
#print(res)
print(res["message"]["content"])

import ollama

# set the temperature to 1 [Higher is more creative]

# Create a new model with modelfile
modelfile = """
FROM llama3.2:latest
SYSTEM You are very smart assistant who knows everything about Linux, you're very succinct and informative.
PARAMETER temperature 0.5
"""

modelName = "linuxExpert:14"
ollama.create(
    model=modelName,
    from_="llama3.2:latest",
    system="You are very smart assistant who knows everything about Linux, you're very succinct and informative",
)

res = ollama.generate(
    model=modelName,
    options={
        'temperature': 0.8
    },
    prompt="I was reading two books which are The linux Command Line written by William E.Shotts and Linux_ The comprehensive Guide -- written by Kofler, Michael. now i want to upskill my knowledge in Linux and becoming one of the most person demand in linux administration and security server configuration and development. so give me books and youtube videos to achieve that no matter the difficulty but in classify structure from intermediate to advanced with a good roadmap depiction."
)

print(res["response"])

# Delete model
ollama.delete(modelName)
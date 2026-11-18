from ollama import Client

client = Client(
    host="http://host.docker.internal:11434"
)

def ask_llm(prompt: str):

    response = client.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

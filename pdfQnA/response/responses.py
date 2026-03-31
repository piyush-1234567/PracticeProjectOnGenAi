import os
from huggingface_hub import InferenceClient

client = InferenceClient()

def ask_llm(prompt):
    completion = client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages = [
            { 
                "role":"user",
                "content": prompt
            }
        ],
    )
    return completion.choices[0].message.content

import requests
import os

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Content-Type": "application/json"
}

prompt = """
You are a question answering system.
1. Answer only using the provided context
2. If the answer is not in the context, say "I don't know"
3. Do not make up information
4. Keep the answer concise

Context:
Text formatting options to ensure proper rendering in PDF readers.

Text Formatting Examples:
1. Bold text is used for emphasis.
2. Italic text can be used for titles or subtle emphasis.
3. Strikethrough is used to show deleted text.

Query:
What formatting options are available in the document?
"""

payload = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 100,
        "temperature": 0
    }
}

response = requests.post(API_URL, headers=headers, json=payload)

print("Status:", response.status_code)
print("Raw:", response.text)

if response.status_code == 200:
    print("Answer:", response.json()[0]["generated_text"])
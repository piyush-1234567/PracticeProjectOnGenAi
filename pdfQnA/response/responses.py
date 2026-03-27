import requests
import os
API_URL = "https://router.huggingface.co/hf-inference/models/distilbert-base-uncased-finetuned-sst-2-english"
token = os.getenv("HF_TOKEN")
headers = {
    "Authorization": f"Bearer {token}" 
}
data = {
    "inputs":"I love building real projects"
}
response = requests.post(API_URL,headers = headers, json=data)
print(response.json())
print(os.getenv("HF_TOKEN"))
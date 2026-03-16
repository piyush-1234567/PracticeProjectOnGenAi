from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
def embedding(sentences):
    
    embedding = model.encode(sentences)
    data = []
    for text,em in zip(sentences,embedding):
        data.append({
            "text": text,
            "embedding": em
        })
    return data

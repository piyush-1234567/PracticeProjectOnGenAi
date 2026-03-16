from main import main
import chromadb
from Embedding.embed import embedding
query = "what is introduction"
ans = main()
client = chromadb.Client()
collection = client.create_collection(name="pdf_chunks")

for i , item in enumerate(ans):
    collection.add(
        ids=[str(i)],
        embeddings = [item["embedding"]],
        documents = [item["text"]]
    )

query_embedding = embedding([query])[0]["embedding"]
results = collection.query(
    query_embeddings = [query_embedding],
    n_results = 3
)
for doc in results["documents"][0]:
    print(doc)
    print("--------------")
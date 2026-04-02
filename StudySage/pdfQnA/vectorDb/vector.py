
import chromadb

def vectorDbStorage(x):
    client = chromadb.PersistentClient(path="./chromadb")
    try:
        client.delete_collection(name="pdf_chunks")
    except:
        pass
    collection = client.get_or_create_collection(name="pdf_chunks")
    ids = []
    embeddings = []
    documents = []
    for i , item in enumerate(x):
        ids.append(str(i))
        embeddings.append(item["embedding"])
        documents.append(item["text"])
    
    if ids:
        collection.add(
        ids = ids,
        embeddings = embeddings,
        documents = documents,
    )
    return collection


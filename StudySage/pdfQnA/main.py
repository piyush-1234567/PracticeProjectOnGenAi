from fastapi import FastAPI , UploadFile , File
import os
from PdfextractorF.extractor import extract_text
from chunking.makeChunks import make_Chunks
from Embedding.embed import embedding
from vectorDb.vector import vectorDbStorage
from prompt.prompt import promptBuilder
from response.responses import ask_llm

app = FastAPI()
vector_store = None
def process_pdf(pdf_path):
    text = extract_text(pdf_path)
    chunks = make_Chunks(text)
    embeddings = embedding(chunks)
    vector_store = vectorDbStorage(embeddings)
    return vector_store
    # query = "what formatting options are available in the document?"
def answer_query(query,vector_store):

    query_embedding = embedding([query])[0]["embedding"]
    results = vector_store.query(
        query_embeddings = query_embedding,
        n_results = 3
    )
    chunks = results['documents'][0]
    context = '\n'.join(chunks)

    prompt = promptBuilder(context,query)
    answer = ask_llm(prompt)
    return answer
    
@app.post("/upload")
async def upload_pdf(file: UploadFile=File(...)):
    global vector_store

    #save uploaded file
    file_location = f"./data/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    vector_store = process_pdf(file_location)

    return {"message":"pdf processed successfully"}
@app.get("/ask")
def ask_question(query: str):
    global vector_store
    if vector_store is None:
        return {"error":"Please upload a pdf first"}
    answer = answer_query(query,vector_store)
    return {"answer":answer}
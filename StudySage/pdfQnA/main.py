from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

from PdfextractorF.extractor import extract_text
from chunking.makeChunks import make_Chunks
from Embedding.embed import embedding
from vectorDb.vector import vectorDbStorage
from prompt.prompt import promptBuilder
from response.responses import ask_llm

# ✅ Create app
app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Shared state
app.state.vector_store = None


# ✅ Process PDF
def process_pdf(pdf_path):
    text = extract_text(pdf_path)
    chunks = make_Chunks(text)
    embeddings = embedding(chunks)
    vector_store = vectorDbStorage(embeddings)
    return vector_store   # IMPORTANT


# ✅ Answer Query
def answer_query(query, vector_store):
    query_embedding = embedding([query])[0]["embedding"]

    results = vector_store.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    chunks = results['documents'][0]
    context = '\n'.join(chunks)

    prompt = promptBuilder(context, query)
    answer = ask_llm(prompt)

    return answer


# ✅ Upload Endpoint
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("data", exist_ok=True)
    file_location = f"./data/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    # ✅ Store properly in app state
    app.state.vector_store = process_pdf(file_location)

    return {"message": "PDF processed successfully"}


# ✅ Ask Endpoint
@app.get("/ask")
def ask_question(query: str):

    if app.state.vector_store is None:
        return {"error": "Please upload a pdf first"}

    answer = answer_query(query, app.state.vector_store)
    return {"answer": answer}
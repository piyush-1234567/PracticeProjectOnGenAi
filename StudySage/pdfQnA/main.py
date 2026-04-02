from PdfextractorF.extractor import extract_text
from chunking.makeChunks import make_Chunks
from Embedding.embed import embedding
from vectorDb.vector import vectorDbStorage
from prompt.prompt import promptBuilder
from response.responses import ask_llm

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

def main():
    vector_store = process_pdf("./data/basic-text.pdf")
    while True:
        ask = input("Ask: ")
        if( ask == "e"):
            break
        answer = answer_query(ask,vector_store)
        print(answer)

    return "hello"  
if __name__ == "__main__":
    main()
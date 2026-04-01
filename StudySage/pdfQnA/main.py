from PdfextractorF.extractor import extract_text
from chunking.makeChunks import make_Chunks
from Embedding.embed import embedding
from vectorDb.vector import vectorDbStorage
from prompt.prompt import promptBuilder
from response.responses import ask_llm
def main():
    pdf_path = "./data/basic-text.pdf"
    text = extract_text(pdf_path)
    chunks = make_Chunks(text)
    ans = embedding(chunks)
    hello = vectorDbStorage(ans)
    # query = "what formatting options are available in the document?"
    while(True):
        query = input("how can i help you today ? ")
        if query == "e":
            break
        query_embedding = embedding([query])[0]["embedding"]
        results = hello.query(
            query_embeddings = query_embedding,
            n_results = 3
        )
        chunks = results['documents'][0]
        context = '\n'.join(chunks)

        prompt = promptBuilder(context,query)
        ll = ask_llm(prompt)
        print(ll)
if __name__ == "__main__":
    main()
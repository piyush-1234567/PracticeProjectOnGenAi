from PdfextractorF.extractor import extract_text
from chunking.makeChunks import make_Chunks
from Embedding.embed import embedding
def main():
    pdf_path = "./data/basic-text.pdf"
    text = extract_text(pdf_path)
    chunks = make_Chunks(text)
    ans = embedding(chunks)
    print(ans)
if __name__ == "__main__":
    main()
from extractorF.extractor import extract_text
from chunking.makeChunks import make_Chunks
def main():
    pdf_path = "./data/basic-text.pdf"
    text = extract_text(pdf_path)
    chunks = make_Chunks(text)
    print(chunks)

if __name__ == "__main__":
    main()
import pymupdf
doc =  pymupdf.open("data/basic-text.pdf")
for page in doc:
    print(page.get_text())
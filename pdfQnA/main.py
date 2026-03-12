import pymupdf
doc =  pymupdf.open("data/pdf-sample_0.pdf")
for page in doc:
    print(page.get_text())
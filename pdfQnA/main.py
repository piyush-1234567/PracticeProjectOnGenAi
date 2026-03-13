import pymupdf
doc =  pymupdf.open("data/basic-text.pdf")
text = ""
for page in doc:
    text += page.get_text()
# print(text)
words = text.split()
start = 0
overlap = 30
chunk_size = 50
ans = []
i = 0
while(start < len(words)):

    chunk = words[start : start + chunk_size]
    chunk_text = " ".join(chunk)
    ans.append(chunk_text)
    i = i + 1
    start += chunk_size - overlap
print(ans)
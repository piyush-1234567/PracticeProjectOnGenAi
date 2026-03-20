import re

def make_Chunks(text,chunk_size=10,overlap=7):
    sentences = re.split(r'(?<=[.!?]) +',text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if(len(current_chunk) + len(sentence) > chunk_size):
            if(current_chunk.strip()):
                chunks.append(current_chunk.strip())
            current_chunk = current_chunk[-overlap:]
        current_chunk += " "+sentence
    if(current_chunk):
        chunks.append(current_chunk.strip())
    return chunks


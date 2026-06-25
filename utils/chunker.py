def chunk_text(text):
    words = text.split()
    chunk_size=100
    overlap=20

    chunks = []
    step = chunk_size - overlap
    for start in range(0,len(words),step):
        chunk_words = words[start:start+chunk_size]
        chunk = ' '.join(chunk_words)
        chunks.append(chunk)
    return chunks

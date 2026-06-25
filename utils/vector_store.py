import chromadb

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(name="pdf_chunks")


def store_embeddings(chunks, embeddings):
    chunk_ids = [f"chunk_{x}" for x in range(1, len(chunks) + 1)]
    collection.add(documents=chunks, embeddings=embeddings, ids=chunk_ids)


def search(query_embedding, top_k):
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results["documents"][0]


def reset_collection():
    global collection

    try:
        chroma_client.delete_collection("pdf_chunks")
    except Exception:
        pass

    collection = chroma_client.get_or_create_collection(name="pdf_chunks")

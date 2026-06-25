from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    return model.encode(chunks)




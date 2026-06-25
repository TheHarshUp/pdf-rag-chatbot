from utils.pdf_reader import read_pdf
from utils.chunker import chunk_text
from utils.embedder import generate_embeddings
from utils.vector_store import store_embeddings

text=read_pdf("data/sample-pdf-rag.pdf")

chunks=chunk_text(text)

embeddings=generate_embeddings(chunks)

store_embeddings(chunks, embeddings)

print("Ingestion complete.")
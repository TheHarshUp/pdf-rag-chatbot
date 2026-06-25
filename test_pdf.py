from utils.pdf_reader import read_pdf
from utils.chunker import chunk_text
from utils.embedder import generate_embeddings
from utils.vector_store import store_embeddings
from utils.vector_store import search
from utils.llm import ask_llm

text=read_pdf("data/sample-pdf-rag.pdf")

chunks=chunk_text(text)

embeddings=generate_embeddings(chunks)

store_embeddings(chunks, embeddings)

question="What is self attention?"
question_embedding=generate_embeddings(question)
results=search(question_embedding, top_k=3)
answer=ask_llm(question, results)
print(answer)
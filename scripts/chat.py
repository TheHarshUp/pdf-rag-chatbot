from utils.embedder import generate_embeddings
from utils.vector_store import search
from utils.llm import ask_llm

question = input("Ask a question: ")

question_embedding = generate_embeddings(question)

results = search(question_embedding, top_k=3)

answer = ask_llm(question, results)

print("\nAnswer:")
print(answer)
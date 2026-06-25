import ollama

def ask_llm(question,context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""
Use only the provided context to answer the question.
If the answer is not in the context, say "I don't know."

Context:
{context}
Question:
{question}
Answer:
"""
    
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
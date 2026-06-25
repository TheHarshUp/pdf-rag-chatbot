# PDF RAG Chatbot using ChromaDB and Groq LLM

## Live Demo
https://pdf-rag-chatbot-2izdqetqvpmm5spepoc4qs.streamlit.app/

A cloud-deployed Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions based on the document content.

## Features

* Upload PDF files
* Extract text from PDFs
* Split text into chunks
* Generate semantic embeddings
* Store embeddings in ChromaDB
* Retrieve relevant chunks using vector similarity search
* Generate context-aware answers using Groq LLM
* Interactive chat interface using Streamlit

## Tech Stack

* Python
* Streamlit
* ChromaDB
* Sentence Transformers
* Groq API (Llama model)
* PyPDF

## Project Workflow

1. User uploads a PDF
2. PDF text is extracted
3. Text is divided into chunks
4. Embeddings are generated for each chunk
5. Embeddings are stored in ChromaDB
6. User asks a question
7. Question embedding is generated
8. Top relevant chunks are retrieved
9. LLM generates answer using retrieved context

## Project Structure

```bash
pdf-rag-chatbot/
│
├── app.py
├── requirements.txt
├── utils/
│   ├── chunker.py
│   ├── embedder.py
│   ├── llm.py
│   ├── pdf_reader.py
│   └── vector_store.py
```

## Installation

Clone the repository:

```bash
git clone <repo-link>
cd pdf-rag-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

## Challenges Solved

* Managing Streamlit session state for persistent chat history
* Resetting vector database on new PDF upload
* Deploying RAG pipeline on Streamlit Cloud
* Replacing local Ollama with cloud-based Groq API

## Future Improvements

* Multi-PDF support
* Better UI/UX
* Source citation for answers
* Chat history export
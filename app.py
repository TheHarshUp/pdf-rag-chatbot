import streamlit as st

from utils.embedder import generate_embeddings
from utils.vector_store import search, reset_collection, store_embeddings
from utils.llm import ask_llm
from utils.pdf_reader import read_pdf
from utils.chunker import chunk_text

st.title("PDF RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)
if uploaded_file:

    if uploaded_file.name != st.session_state.current_pdf:
        st.session_state.current_pdf = uploaded_file.name
        st.session_state.pdf_processed = False

    if not st.session_state.pdf_processed:

        with open("uploads/uploaded.pdf", "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("Processing PDF..."):
            reset_collection()

            text = read_pdf("uploads/uploaded.pdf")
            chunks = chunk_text(text)
            embeddings = generate_embeddings(chunks)

            store_embeddings(chunks, embeddings)

        st.session_state.pdf_processed = True
        st.success("PDF indexed successfully!")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if not st.session_state.pdf_processed:
    st.warning("Upload a PDF first")
    st.stop()

question = st.chat_input("Ask a question about the PDF")

if question:

    st.session_state.messages.append({"role": "user", "content": question})

    question_embedding = generate_embeddings(question)
    results = search(question_embedding, top_k=3)
    answer = ask_llm(question, results)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

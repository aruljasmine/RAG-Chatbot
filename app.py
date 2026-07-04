import streamlit as st

from utils.retriever import load_vector_store
from utils.rag_chain import get_llm

from utils.read_pdf import load_pdf
from utils.split_pdf import split_text
from utils.vector_store import create_vector_store

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🤖 RAG Chatbot")
st.write("Chat with your PDF using AI.")

# -------------------------
# Load Resources
# -------------------------

@st.cache_resource
def load_resources():
    db = load_vector_store()
    llm = get_llm()
    return db, llm

db, llm = load_resources()

if "db" in st.session_state:
    db = st.session_state.db

# -------------------------
# Sidebar
# -------------------------

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.header("📄 Document Info")

    st.success("Vector Database Loaded")

    st.write("Chunks Retrieved: **3**")

    # -------------------------
    # Upload PDF
    # -------------------------

    st.header("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    # If a PDF is uploaded
    if uploaded_file is not None:

        with st.spinner("📖 Reading PDF..."):

            text, pages = load_pdf(uploaded_file)

            chunks = split_text(text)

            st.session_state.db = create_vector_store(chunks, save=False)

        st.success("✅ PDF uploaded successfully!")

        st.write(f"📄 **File Name:** {uploaded_file.name}")
        st.write(f"📑 **Pages:** {pages}")
        st.write(f"🧩 **Chunks:** {len(chunks)}")

    # -------------------------
    # Clear Chat
    # -------------------------

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
# -------------------------
# Chat History
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Chat Input
# -------------------------

question = st.chat_input("Ask anything about your PDF...")

if question:

    st.chat_message("user").markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner("Searching document..."):

        docs = db.similarity_search(question, k=3)

        context = "\n\n".join(doc.page_content for doc in docs)

        prompt = f"""
You are an intelligent AI assistant.

You have two sources of knowledge:

1. Document Context
2. General Knowledge

Instructions:

- First search the document.
- If the answer exists there, answer using the document.
- If not, answer using your own knowledge.
- Mention the source at the end as either:
    📄 Source: Document
or
    🧠 Source: General Knowledge
or
    📄🧠 Source: Document + General Knowledge

Document:

{context}

Question:

{question}
"""

        response = llm.invoke(prompt)

    answer = response.content

    with st.chat_message("assistant"):
        st.markdown(answer)

        st.divider()

        st.subheader("📚 Retrieved Chunks")

        for i, doc in enumerate(docs, start=1):
            with st.expander(f"Chunk {i}"):
                st.write(doc.page_content)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
# 🤖 RAG Chatbot using LangChain, FAISS & Gemini

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that allows users to upload a PDF and ask questions about its contents. The application uses semantic search with FAISS and HuggingFace embeddings to retrieve relevant information before generating answers with Google's Gemini 2.5 Flash model.

---

## 🚀 Features

- 📄 Upload any PDF document
- ✂️ Automatically split text into chunks
- 🧠 Generate embeddings using HuggingFace
- 🔍 Semantic search with FAISS Vector Database
- 🤖 Answer questions using Gemini 2.5 Flash
- 💬 Streamlit chat interface
- 🗑️ Clear chat history
- 🌐 Falls back to general knowledge when information is not available in the uploaded document

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings (`all-MiniLM-L6-v2`)
- Google Gemini 2.5 Flash
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```
RAG-Chatbot/
│
├── Data/
├── utils/
│   ├── read_pdf.py
│   ├── split_pdf.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_chain.py
│
├── vector_db/
├── app.py
├── chat.py
├── build_vector_db.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aruljasmine/RAG-Chatbot.git
cd RAG-Chatbot
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / WSL**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Build the Vector Database

```bash
python build_vector_db.py
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

```
PDF Upload
      │
      ▼
Read PDF
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
Semantic Search
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Final Answer
```

---
## 🌐 Live Demo

https://rag-chatbot-aj.streamlit.app/

## 📌 Future Improvements

- Support multiple PDF uploads
- Conversation memory
- Source page references
- Advanced retrieval techniques

---

## 👨‍💻 Author

**Arul Jasmine D**

Computer Science Engineering Student

GitHub: https://github.com/aruljasmine

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

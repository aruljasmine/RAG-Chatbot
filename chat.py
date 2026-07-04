from utils.retriever import load_vector_store
from utils.rag_chain import get_llm

print("Loading Vector Database...")
db = load_vector_store()

print("Loading Gemini Model...")
llm = get_llm()

print("\n🤖 RAG Chatbot is Ready!")
print("Type 'exit' to quit.\n")

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # Retrieve top 3 relevant chunks
    docs = db.similarity_search(question, k=3)

    # Combine retrieved chunks into context
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an intelligent AI assistant.

You have TWO sources of knowledge:

1. Document Context
2. Your own General Knowledge

Instructions:

- First, carefully check whether the answer exists in the document context.
- If the document contains the answer, answer using ONLY the document.
- If the document does NOT contain enough information, answer using your own knowledge.
- Never say "I couldn't find the answer."
- At the end of every answer, mention the source exactly as:

📄 Source: Document

OR

🧠 Source: General Knowledge

-----------------------------
Document Context:
{context}
-----------------------------

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("\n" + "=" * 70)
    print("🤖 Answer:\n")
    print(response.content)
    print("=" * 70 + "\n")
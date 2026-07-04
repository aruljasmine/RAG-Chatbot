from utils.retriever import load_vector_store

db = load_vector_store()

query = input("Ask a question: ")

docs = db.similarity_search(query, k=3)

print("\nTop Matching Chunks\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 70)
    print(f"Chunk {i}")
    print("=" * 70)
    print(doc.page_content)
    print()
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, save=True):
    """
    Creates a FAISS vector database.

    save=True  -> saves to vector_db/
    save=False -> returns the database without saving
    """

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating vector database...")

    vector_db = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    if save:
        vector_db.save_local("vector_db")
        print("✅ Vector database created successfully!")

    return vector_db
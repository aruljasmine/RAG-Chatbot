from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db
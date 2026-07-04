from utils.read_pdf import load_pdf
from utils.split_pdf import split_text
from utils.vector_store import create_vector_store

print("Loading PDF...")

text = load_pdf("Data/tasks.pdf")

print("Splitting text...")

chunks = split_text(text)

print(f"Total Chunks: {len(chunks)}")

print("Creating Vector Database...")

create_vector_store(chunks)

print("Done!")
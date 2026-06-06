from src.document_loader import load_pdf
from src.text_splitter import split_text
from src.vector_store import VectorStore
from src.rag_chat import RAGChat

pdf_path = "LLM1_NEXA.pdf"

with open(pdf_path, "rb") as file:

    text = load_pdf(file)

chunks = split_text(text)

store = VectorStore()

store.create_index(chunks)

rag = RAGChat(store)

answer = rag.ask(
    "Qu'est-ce qu'un transformer ?"
)

print("\n")
print("===== RÉPONSE =====")
print("\n")
print(answer)
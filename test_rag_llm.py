from src.vector_store import VectorStore
from src.rag_chat import RAGChat


chunks = [
    "Les Transformers utilisent le mécanisme d'attention.",
    "Python est un langage de programmation.",
    "Les réseaux de neurones sont utilisés en intelligence artificielle.",
    "Les LLM sont entraînés sur de grandes quantités de texte."
]

store = VectorStore()

store.create_index(chunks)

rag = RAGChat(store)

question = "Comment fonctionnent les transformers ?"

response = rag.ask(question)

print("\nRéponse :\n")
print(response)
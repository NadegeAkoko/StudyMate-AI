from src.vector_store import VectorStore

chunks = [
    "Les Transformers utilisent le mécanisme d'attention.",
    "Python est un langage de programmation.",
    "Les réseaux de neurones sont utilisés en IA.",
    "Les LLM sont entraînés sur de grandes quantités de texte."
]

store = VectorStore()

store.create_index(chunks)

results = store.search(
    "Comment fonctionnent les transformers ?"
)

print(results)
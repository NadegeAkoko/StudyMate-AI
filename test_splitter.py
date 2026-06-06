from src.text_splitter import split_text

sample_text = """
Les Large Language Models sont des modèles d'intelligence artificielle.
Ils sont capables de comprendre et générer du texte.
""" * 200

chunks = split_text(sample_text)

print(f"Nombre de chunks : {len(chunks)}")

print("\nPremier chunk :\n")

print(chunks[0][:300])
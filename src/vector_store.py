from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            "paraphrase-multilingual-MiniLM-L12-v2"
        )

        self.index = None
        self.chunks = []

    def create_index(self, chunks):

        self.chunks = chunks

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings.astype("float32")
        )

    def search(self, query, k=1):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            query_embedding.astype("float32"),
            k
        )

        results = []

        for idx in indices[0]:
            results.append(
                self.chunks[idx]
            )

        return results
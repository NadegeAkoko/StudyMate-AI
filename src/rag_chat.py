from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

class RAGChat:


    def __init__(self, vector_store):

        self.vector_store = vector_store

        self.tokenizer = AutoTokenizer.from_pretrained(
            "google/flan-t5-base"
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            "google/flan-t5-base"
        )

    def ask(self, question, k=1):

        contexts = self.vector_store.search(
            question,
            k=k
        )

        print("\n===== CHUNKS RETROUVÉS =====")

        for i, chunk in enumerate(contexts, 1):
            print(f"\n--- CHUNK {i} ---")
            print(chunk)

        context = "\n\n".join(contexts)

        print("\n====================")
        print("QUESTION :", question)
        print("====================")
        print("CONTEXTE RETROUVÉ :")
        print(context)
        print("====================\n")

        prompt = f"""
    ```

    You are a helpful educational assistant.

    Use the context below to answer the student's question.

    Rules:

    * Answer in the same language as the question.
    * Write complete sentences.
    * Explain the concept clearly.
    * Give a short educational answer.
    * Summarize the information.
    * Do not copy the context word for word.

    Context:
    {context}

    Question:
    {question}

    Final answer:
    """


        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.6
        )

        answer = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return context, contexts

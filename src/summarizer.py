from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM


class Summarizer:

    def __init__(self):

        print("Chargement du modèle de résumé...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            "google/flan-t5-base"
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            "google/flan-t5-base"
        )

        print("Modèle chargé ✅")

    def summarize(self, chunks):

        useful_chunks = chunks[5:15]

        content = "\n\n".join(
            useful_chunks
        )

        prompt = f"""
Summarize this course in French.

Give:
- Main topics
- Key concepts
- Important notions

Course:

{content}
"""

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=False
        )

        summary = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return summary
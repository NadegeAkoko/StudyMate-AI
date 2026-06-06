from src.document_loader import load_pdf
from src.summarizer import Summarizer
from src.text_splitter import split_text

pdf_path = "LLM1_NEXA.pdf"

with open(pdf_path, "rb") as file:

    text = load_pdf(file)

chunks = split_text(text)

summarizer = Summarizer()

summary = summarizer.summarize(
    chunks
)

print("\n")
print("===== RÉSUMÉ =====")
print("\n")
print(summary)
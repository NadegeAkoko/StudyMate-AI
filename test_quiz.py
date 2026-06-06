from src.quiz_generator import QuizGenerator

chunks = [
    "Les transformers sont une architecture de deep learning utilisée principalement pour traiter des données séquentielles.",
    "Le NLP est le domaine qui étudie le traitement automatique du langage naturel."
]

generator = QuizGenerator()

quiz = generator.generate_quiz(
    chunks,
    nb_questions=2
)

for q in quiz:

    print("\nQUESTION")
    print(q["question"])

    for option in q["options"]:
        print("-", option)

    print(
        "\nBonne réponse :",
        q["answer"]
    )

import random
import re


class QuizGenerator:

    def __init__(self):
        pass

    def clean_sentence(self, sentence):

        sentence = sentence.strip()

        if len(sentence) < 40:
            return None

        if len(sentence) > 200:
            return None

        if "http" in sentence.lower():
            return None

        if re.search(r"\d{4}", sentence):
            return None

        return sentence

    def build_question(self, sentence):

        sentence_lower = sentence.lower()

        if "attention" in sentence_lower:

            return {
                "question":
                "Quel mécanisme est utilisé par les Transformers ?",

                "answer":
                "Attention",

                "options":
                [
                    "Attention",
                    "SQL",
                    "Compression",
                    "Ethernet"
                ]
            }

        if "transformer" in sentence_lower:

            return {
                "question":
                "Les Transformers sont principalement utilisés pour ?",

                "answer":
                "Traiter des données séquentielles",

                "options":
                [
                    "Traiter des données séquentielles",
                    "Créer des bases SQL",
                    "Compresser des images",
                    "Gérer un réseau"
                ]
            }

        if "nlp" in sentence_lower:

            return {
                "question":
                "Que signifie NLP ?",

                "answer":
                "Traitement du langage naturel",

                "options":
                [
                    "Traitement du langage naturel",
                    "Programmation réseau",
                    "Base de données",
                    "Vision par ordinateur"
                ]
            }

        return None

    def generate_quiz(self, chunks, nb_questions=10):

        quiz = []

        valid_sentences = []

        for chunk in chunks:

            sentences = chunk.split(".")

            for sentence in sentences:

                cleaned = self.clean_sentence(
                    sentence
                )

                if cleaned:
                    valid_sentences.append(
                        cleaned
                    )

        random.shuffle(
            valid_sentences
        )

        for sentence in valid_sentences:

            question = self.build_question(
                sentence
            )

            if question:

                quiz.append(question)

            if len(quiz) >= nb_questions:
                break

        return quiz

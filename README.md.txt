# 📚 StudyMate AI

##  Présentation

StudyMate AI est une application intelligente d'aide à la révision basée sur l'Intelligence Artificielle.

L'objectif est d'aider les étudiants à apprendre plus efficacement en transformant leurs supports de cours en outils interactifs.

L'application permet :

*  D'importer des fichiers PDF, DOCX et PPTX
*  De générer automatiquement des quiz
*  De poser des questions à un assistant IA
*  D'analyser le contenu des documents
*  D'utiliser une architecture RAG (Retrieval-Augmented Generation)

---

# Technologies utilisées

## Frontend

* Streamlit

## Intelligence Artificielle

* Sentence Transformers
* FAISS
* FLAN-T5

## Traitement du langage naturel

* LangChain Text Splitters

## Langage

* Python 3.12

---

# Fonctionnalités

##  Importation de documents

Formats pris en charge :

* PDF
* DOCX
* PPTX

---

##  Génération automatique de quiz

À partir du contenu du cours, l'application génère automatiquement des questions à choix multiples permettant à l'utilisateur de tester ses connaissances.

---

##  Assistant IA

L'assistant utilise une architecture RAG :

1. Recherche des passages pertinents dans le cours
2. Sélection des informations utiles
3. Génération d'une réponse adaptée à la question posée

---

##  Analyse du document

L'application affiche :

* Le nombre de caractères
* Le nombre de chunks générés
* Un aperçu du document

---

#  Architecture RAG

Pipeline de fonctionnement :

1. Import du document
2. Extraction du texte
3. Découpage en chunks
4. Création des embeddings
5. Stockage dans FAISS
6. Recherche sémantique
7. Génération de réponse avec FLAN-T5

---

#  Structure du projet

StudyMate-AI/

├── app.py

├── src/

│ ├── document_loader.py

│ ├── text_splitter.py

│ ├── vector_store.py

│ ├── quiz_generator.py

│ ├── rag_chat.py

│ └── summarizer.py

├── requirements.txt

└── README.md

---

#  Installation

Créer un environnement virtuel :

python -m venv venv

Activer l'environnement :

venv\Scripts\activate

Installer les dépendances :

pip install -r requirements.txt

---

#  Lancer l'application

streamlit run app.py

---

# Objectif pédagogique

Ce projet a été réalisé dans le cadre d'un Master en Intelligence Artificielle et Data Science.

Il met en œuvre :

* La recherche sémantique
* Les bases vectorielles
* Le traitement automatique du langage naturel
* Le Retrieval-Augmented Generation (RAG)
* Les modèles génératifs

---

#  Auteur

Nadège Akoko Kangni-soukpe

Je precise que j'ai eu a utilisé les pdf du cours


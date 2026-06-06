
from src.rag_chat import RAGChat


import streamlit as st

from src.document_loader import (
    load_pdf,
    load_docx,
    load_pptx
)

from src.text_splitter import split_text
from src.vector_store import VectorStore
from src.quiz_generator import QuizGenerator



# CONFIG


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)



# STYLE


st.markdown("""
<style>

/* Fond général */
.stApp{
    background: linear-gradient(
        135deg,
        #f8fafc,
        #eef4ff
    );
}

/* Titre principal */
.main-title{
    text-align:center;
    font-size:4rem;
    font-weight:800;
    background: linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;
}

/* Sous titre */
.subtitle{
    text-align:center;
    font-size:1.3rem;
    color:#64748b;
    margin-bottom:40px;
}

/* Cartes d'accueil */
.feature-card{
    background:white;
    padding:25px;
    border-radius:18px;
    text-align:center;
    font-size:1.1rem;
    font-weight:600;
    box-shadow:0 8px 25px rgba(0,0,0,0.08);
    transition:all 0.3s ease;
}

.feature-card:hover{
    transform:translateY(-5px);
    box-shadow:0 15px 35px rgba(79,70,229,0.20);
}

/* Sidebar premium */
section[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #1e293b,
        #334155
    );
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Boutons */
.stButton > button{
    width:100%;
    background:linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed
    );
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:bold;
    transition:0.3s;
}

.stButton > button:hover{
    transform:scale(1.03);
}

/* Input */
.stTextInput input{
    border-radius:12px !important;
}

/* Onglets */
.stTabs [data-baseweb="tab"]{
    font-size:16px;
    font-weight:600;
}

/* Cartes réponses */
.answer-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 6px 20px rgba(0,0,0,0.08);
    border-left:5px solid #4f46e5;
}

</style>
""", unsafe_allow_html=True)



# SESSION STATE


if "document_loaded" not in st.session_state:
    st.session_state.document_loaded = False

if "quiz" not in st.session_state:
    st.session_state.quiz = []

if "score" not in st.session_state:
    st.session_state.score = 0



# HEADER


st.markdown(
    """
    <div class="main-title">
        📚 StudyMate AI
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Learn Smarter, Not Harder 🚀
    </div>
    """,
    unsafe_allow_html=True
)


# FEATURES


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        🎯<br><br>
        Smart Quiz
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        💬<br><br>
        AI Assistant
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        📊<br><br>
        Learning Analytics
    </div>
    """, unsafe_allow_html=True)

st.divider()


# UPLOAD


st.markdown("""
<div style="
background:white;
padding:30px;
border-radius:20px;
box-shadow:0 8px 25px rgba(0,0,0,0.08);
margin-bottom:20px;
text-align:center;
">
<h3>🚀 Welcome to StudyMate AI</h3>

</div>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader(
    "Import your course",
    type=["pdf", "docx", "pptx"]
)



# LOAD DOCUMENT


if uploaded_file:

    if not st.session_state.document_loaded:

        with st.spinner("Analyzing document..."):

            file_type = uploaded_file.name.split(".")[-1]

            if file_type == "pdf":
                text = load_pdf(uploaded_file)

            elif file_type == "docx":
                text = load_docx(uploaded_file)

            elif file_type == "pptx":
                text = load_pptx(uploaded_file)

            chunks = split_text(text)

            store = VectorStore()
            store.create_index(chunks)
            rag = RAGChat(store)

            st.session_state.rag = rag

            quiz_generator = QuizGenerator()

            quiz = quiz_generator.generate_quiz(
                chunks,
                nb_questions=5
            )

            st.session_state.text = text
            st.session_state.chunks = chunks
            st.session_state.store = store
            st.session_state.quiz = quiz

            st.session_state.document_loaded = True


  
    # SIDEBAR
   

    with st.sidebar:

        st.title("📚 StudyMate AI")

        st.success("Document Loaded")

        st.write(
            f"📄 {uploaded_file.name}"
        )

        st.metric(
            "Characters",
            len(st.session_state.text)
        )

        st.metric(
            "Chunks",
            len(st.session_state.chunks)
        )


   
    # TABS
   

    tab1, tab2, tab3 = st.tabs(
        [
            "🎯 Quiz",
            "💬 Assistant",
            "📊 Analysis"
        ]
    )


    # QUIZ
   

    with tab1:

        st.subheader("🎯 Smart Quiz")

        if "quiz_started" not in st.session_state:
            st.session_state.quiz_started = False

        if "current_question" not in st.session_state:
            st.session_state.current_question = 0

        if not st.session_state.quiz_started:

            st.info(
                "Ready to test your knowledge?"
            )

            if st.button("🚀 Start Quiz"):

                st.session_state.quiz_started = True
                st.rerun()

        else:

            total_questions = len(
                st.session_state.quiz
            )

            current = st.session_state.current_question

            if current < total_questions:

                question = st.session_state.quiz[current]

                st.progress(
                    (current + 1) / total_questions
                )

                st.markdown(
                    f"### Question {current + 1}/{total_questions}"
                )

                answer = st.radio(
                    question["question"],
                    question["options"],
                    key=f"question_{current}"
                )

                if st.button(
                    "✅ Validate Answer",
                    key=f"validate_{current}"
                ):

                    if answer == question["answer"]:

                        st.success(
                            "✅ Correct Answer"
                        )

                        st.session_state.score += 1

                    else:

                        st.error(
                            "❌ Incorrect Answer"
                        )

                        st.write(
                            f"Correct answer: {question['answer']}"
                        )

                    st.session_state.current_question += 1
                    st.rerun()

            else:

                final_score = st.session_state.score

                percentage = int(
                    (final_score / total_questions) * 100
                )

                st.balloons()

                st.success(
                    "🎉 Quiz Completed!"
                )

                st.metric(
                    "Score",
                    f"{final_score}/{total_questions}"
                )

                st.metric(
                    "Success Rate",
                    f"{percentage}%"
                )

                if st.button(
                    "🔄 Restart Quiz"
                ):

                    st.session_state.current_question = 0
                    st.session_state.score = 0
                    st.session_state.quiz_started = False

                    st.rerun()


   
    # ASSISTANT
   

    with tab2:

        st.subheader(
            "💬 Course Assistant"
        )

        question = st.text_input(
            "Ask a question about your course"
        )

        if question:

            with st.spinner(
                "Analyzing course..."
            ):

                answer, contexts = (
                    st.session_state.rag.ask(
                        question
                    )
                )

            st.markdown(
                "### 🤖 Answer"
            )

            st.markdown(
                f"""
                <div class="answer-card">
                🤖 {answer}
                </div>
                """,
                unsafe_allow_html=True
            )

            with st.expander(
                "📚 Sources Used"
            ):

                for i, chunk in enumerate(
                    contexts,
                    1
                ):

                    st.markdown(
                        f"**Source {i}**"
                    )

                    st.write(
                        chunk
                    )

  
    # ANALYSIS
   

    with tab3:

        st.subheader(
            "📊 Document Analysis"
        )

        st.metric(
            "Characters",
            len(st.session_state.text)
        )

        st.metric(
            "Chunks",
            len(st.session_state.chunks)
        )

        st.text_area(
            "Preview",
            st.session_state.text[:3000],
            height=300
        )

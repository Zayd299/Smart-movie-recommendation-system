import streamlit as st
from backend.preprocess import load_and_clean
from backend.recommender import ContentRecommender
from backend.mood_engine import filter_by_mood, MOOD_MAP
from backend.explainability import explain

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Smart Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom CSS (Modern UI)
# --------------------------------------------------
st.markdown("""
<style>

/* Main background */
.main {
    background-color: #0f172a;
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #020617);
}

/* Headings */
h1, h2, h3 {
    color: #38bdf8;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

/* Selectbox */
.stSelectbox div {
    border-radius: 10px;
}

/* Movie card */
.movie-card {
    background: #020617;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 18px;
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.15);
}

/* Explanation text */
.explain {
    color: #cbd5f5;
    font-size: 14px;
    margin-top: 8px;
}

hr {
    border: 1px solid #1e293b;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Helper function to show cards
# --------------------------------------------------
def show_card(title, explanation):
    st.markdown(f"""
    <div class="movie-card">
        <h3>🎬 {title}</h3>
        <p class="explain">{explanation}</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Load Data & Model
# --------------------------------------------------
movies = load_and_clean()
recommender = ContentRecommender(movies)

# --------------------------------------------------
# Hero Section
# --------------------------------------------------
st.markdown("""
<h1 style="text-align:center;">🎬 Smart Movie Recommendation System</h1>
<p style="text-align:center; color:#94a3b8;">
Personalized • Mood-Based • Explainable AI
</p>
<hr>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.markdown("## 🎛️ Recommendation Mode")

mode = st.sidebar.radio(
    "Choose how you want recommendations:",
    ["🎥 Movie Based", "🎭 Mood Based"]
)

# --------------------------------------------------
# Main Content
# --------------------------------------------------
col1, col2 = st.columns([2, 3])

# ---------------- MOVIE BASED ----------------
if mode == "🎥 Movie Based":
    with col1:
        st.subheader("🎥 Select a Movie")
        movie = st.selectbox(
            "Choose a movie you like",
            movies['title'].values
        )
        recommend_btn = st.button("✨ Get Recommendations")

    with col2:
        if recommend_btn:
            st.subheader("🍿 Recommended for You")
            results = recommender.recommend(movie)

            for title, score in results:
                show_card(title, explain(movie, title))

# ---------------- MOOD BASED ----------------
else:
    with col1:
        st.subheader("🎭 Select Your Mood")
        mood = st.selectbox(
            "How are you feeling today?",
            list(MOOD_MAP.keys())
        )

        filtered_movies = filter_by_mood(movies, mood)

        movie = st.selectbox(
            "Pick a movie",
            filtered_movies['title'].values
        )

        recommend_btn = st.button("✨ Recommend by Mood")

    with col2:
        if recommend_btn:
            st.subheader(f"🎬 Movies for Your Mood: {mood}")
            mood_recommender = ContentRecommender(filtered_movies)
            results = mood_recommender.recommend(movie)

            for title, score in results:
                show_card(title, explain(movie, title))

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<hr>
<p style="text-align:center; color:#64748b;">
Built with ❤️ using Python, ML & Streamlit
</p>
""", unsafe_allow_html=True)

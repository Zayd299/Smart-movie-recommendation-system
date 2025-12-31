🎬 Smart Movie Recommendation System

An end-to-end Machine Learning powered Movie Recommendation System that provides personalized, mood-based, and explainable movie recommendations through a modern web interface.

This project demonstrates real-world ML pipeline design, NLP techniques, and deployment-ready application development using Python and Streamlit.

🚀 Features

🎥 Movie-Based Recommendations (Content-Based Filtering)

🎭 Mood-Based Recommendations

🧠 Explainable AI

“Recommended because you liked…”

🔍 NLP using TF-IDF

🎨 Modern Dark UI with Streamlit

🧱 Modular Backend Architecture

⚡ Fast & Lightweight Web App

🧠 Recommendation Techniques Used
1️⃣ Content-Based Filtering

TF-IDF Vectorization on:

Movie overview

Genres

Keywords

Cosine similarity to find similar movies

2️⃣ Mood-Based Recommendation

User selects a mood (Happy, Sad, Excited, Relaxed, Romantic)

Mood mapped to relevant genres

Recommendations generated from filtered movie space

3️⃣ Explainable AI

Each recommendation includes a human-readable explanation describing why it was suggested.

🛠️ Tech Stack
Category	Tools
Language	Python
Data Processing	Pandas, NumPy
Machine Learning	Scikit-learn
NLP	TF-IDF
Similarity	Cosine Similarity
Web App	Streamlit
Version Control	Git & GitHub
📁 Project Structure
Smart-movie-recommendation/
│
├── backend/
│   ├── preprocess.py
│   ├── recommender.py
│   ├── mood_engine.py
│   └── explainability.py
│
├── data/
│   ├── README.md          # Dataset instructions
│
├── app.py                 # Streamlit app
├── requirements.txt
├── .gitignore
└── README.md

📊 Dataset
This project uses the TMDB 5000 Movie Dataset.

Required files:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

⚠️ Dataset is not included in this repository due to size and licensing.

How to get the data:

Download TMDB 5000 Movie Dataset from Kaggle

Place both CSV files inside the data/ folder

data/
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/Zayd299/Smart-movie-recommendation.git
cd Smart-movie-recommendation

2️⃣ Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application
python -m streamlit run app.py


The app will open in your browser at:

http://localhost:8501

🎨 UI Preview

Dark theme

Gradient buttons

Card-based recommendations

Clean, modern layout

(Screenshots can be added here later)

🧪 Example Use Cases

“Recommend movies similar to Inception”

“Suggest movies based on my current mood”

“Explain why this movie was recommended”

📌 Why This Project Stands Out

✔ End-to-end ML pipeline
✔ Real-world dataset
✔ NLP + ML integration
✔ Explainable AI
✔ Clean backend architecture
✔ Deployable web app
✔ Recruiter-friendly project

🔮 Future Improvements

Collaborative Filtering

Hybrid Recommendation System

User login & feedback loop

Movie posters via TMDB API

FastAPI backend

Cloud deployment (Render / HuggingFace)

👤 Author

Zaid Khan
Machine Learning & AI Enthusiast

📌 Feel free to connect and explore more projects!

⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!
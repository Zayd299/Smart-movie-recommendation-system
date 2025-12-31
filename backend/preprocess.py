import pandas as pd
import ast

def load_and_clean():
    movies = pd.read_csv("data/tmdb_5000_movies.csv")

    def convert(text):
        try:
            return " ".join([i['name'] for i in ast.literal_eval(text)])
        except:
            return ""

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)

    movies['tags'] = movies['overview'].fillna('') + " " + movies['genres'] + " " + movies['keywords']

    return movies[['title', 'tags', 'genres']]

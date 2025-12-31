from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentRecommender:
    def __init__(self, movies):
        self.movies = movies
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(movies['tags'])
        self.similarity = cosine_similarity(self.tfidf_matrix)

    def recommend(self, movie_name, top_n=5):
        idx = self.movies[self.movies['title'] == movie_name].index[0]
        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

        results = []
        for i, score in scores:
            results.append((self.movies.iloc[i]['title'], score))
        return results

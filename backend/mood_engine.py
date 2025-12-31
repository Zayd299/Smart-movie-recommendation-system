MOOD_MAP = {
    "Happy 😊": ["Comedy", "Adventure"],
    "Sad 😢": ["Drama", "Romance"],
    "Excited 🔥": ["Action", "Thriller"],
    "Relaxed 😌": ["Animation", "Family"],
    "Romantic ❤️": ["Romance"]
}

def filter_by_mood(movies, mood):
    genres = MOOD_MAP[mood]
    return movies[movies['genres'].str.contains('|'.join(genres))]

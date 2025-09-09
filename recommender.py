import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Load and preprocess data
def load_data():
    movies = pd.read_csv('tmdb_5000_movies.csv')
    credits = pd.read_csv('tmdb_5000_credits.csv')
    movies = movies.merge(credits, on='title')
    return movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast']]

def preprocess_data(movies):
    movies = movies.fillna('')
    
    def extract_names(obj):
        try:
            return [item['name'] for item in ast.literal_eval(obj)]
        except:
            return []
    
    movies['genres'] = movies['genres'].apply(extract_names)
    movies['keywords'] = movies['keywords'].apply(extract_names)
    movies['cast'] = movies['cast'].apply(lambda x: extract_names(x)[:3])
    
    # Create tags
    movies['tags'] = (
        movies['overview'] + ' ' +
        movies['genres'].apply(lambda x: ' '.join(x)) + ' ' +
        movies['keywords'].apply(lambda x: ' '.join(x)) + ' ' +
        movies['cast'].apply(lambda x: ' '.join(x))
    ).str.lower()
    
    return movies

# Build recommendation system
def build_recommender(movies):
    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['tags'])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def recommend(movie_title, movies, similarity_matrix):
    try:
        idx = movies[movies['title'].str.lower() == movie_title.lower()].index[0]
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
        movie_indices = [i[0] for i in sim_scores]
        return movies.iloc[movie_indices]['title'].tolist()
    except:
        return f"Movie '{movie_title}' not found"

# Main execution
if __name__ == "__main__":
    # Load and process data
    movies = load_data()
    movies = preprocess_data(movies)
    similarity_matrix = build_recommender(movies)
    
    # Demo
    test_movies = ['The Dark Knight', 'Inception', 'Avatar']
    
    for movie in test_movies:
        print(f"\nRecommendations for '{movie}':")
        recommendations = recommend(movie, movies, similarity_matrix)
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
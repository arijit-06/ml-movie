# Movie Recommendation System

Content-based filtering using TMDB dataset.

## Setup
```bash
pip install pandas scikit-learn numpy
```

## Usage
1. Download TMDB dataset from Kaggle
2. Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in project folder
3. Run: `python recommender.py`

## Features
- Content-based filtering using genres, overview, keywords, cast
- TF-IDF vectorization with cosine similarity
- Returns top 5 similar movies
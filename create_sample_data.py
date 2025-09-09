import pandas as pd
import json

# Sample movie data
movies_data = {
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'title': [
        'The Dark Knight', 'Inception', 'Avatar', 'Interstellar', 'The Matrix',
        'Pulp Fiction', 'The Godfather', 'Forrest Gump', 'Fight Club', 'Goodfellas'
    ],
    'overview': [
        'Batman faces the Joker in Gotham City',
        'A thief enters dreams to plant ideas',
        'Humans colonize alien planet Pandora',
        'Astronauts travel through a wormhole',
        'Hacker discovers reality is simulation',
        'Interconnected crime stories in LA',
        'Italian-American crime family saga',
        'Man with low IQ experiences history',
        'Insomniac forms underground fight club',
        'Rise and fall of mob associate'
    ],
    'genres': [
        '[{"name": "Action"}, {"name": "Crime"}, {"name": "Drama"}]',
        '[{"name": "Action"}, {"name": "Sci-Fi"}, {"name": "Thriller"}]',
        '[{"name": "Action"}, {"name": "Adventure"}, {"name": "Fantasy"}]',
        '[{"name": "Adventure"}, {"name": "Drama"}, {"name": "Sci-Fi"}]',
        '[{"name": "Action"}, {"name": "Sci-Fi"}]',
        '[{"name": "Crime"}, {"name": "Drama"}]',
        '[{"name": "Crime"}, {"name": "Drama"}]',
        '[{"name": "Drama"}, {"name": "Romance"}]',
        '[{"name": "Drama"}]',
        '[{"name": "Biography"}, {"name": "Crime"}, {"name": "Drama"}]'
    ],
    'keywords': [
        '[{"name": "superhero"}, {"name": "joker"}, {"name": "batman"}]',
        '[{"name": "dream"}, {"name": "heist"}, {"name": "mind"}]',
        '[{"name": "alien"}, {"name": "planet"}, {"name": "nature"}]',
        '[{"name": "space"}, {"name": "wormhole"}, {"name": "time"}]',
        '[{"name": "virtual reality"}, {"name": "hacker"}, {"name": "simulation"}]',
        '[{"name": "nonlinear"}, {"name": "violence"}, {"name": "crime"}]',
        '[{"name": "mafia"}, {"name": "family"}, {"name": "power"}]',
        '[{"name": "life"}, {"name": "history"}, {"name": "destiny"}]',
        '[{"name": "insomnia"}, {"name": "violence"}, {"name": "identity"}]',
        '[{"name": "mafia"}, {"name": "betrayal"}, {"name": "loyalty"}]'
    ]
}

credits_data = {
    'title': [
        'The Dark Knight', 'Inception', 'Avatar', 'Interstellar', 'The Matrix',
        'Pulp Fiction', 'The Godfather', 'Forrest Gump', 'Fight Club', 'Goodfellas'
    ],
    'cast': [
        '[{"name": "Christian Bale"}, {"name": "Heath Ledger"}, {"name": "Aaron Eckhart"}]',
        '[{"name": "Leonardo DiCaprio"}, {"name": "Marion Cotillard"}, {"name": "Tom Hardy"}]',
        '[{"name": "Sam Worthington"}, {"name": "Zoe Saldana"}, {"name": "Sigourney Weaver"}]',
        '[{"name": "Matthew McConaughey"}, {"name": "Anne Hathaway"}, {"name": "Jessica Chastain"}]',
        '[{"name": "Keanu Reeves"}, {"name": "Laurence Fishburne"}, {"name": "Carrie-Anne Moss"}]',
        '[{"name": "John Travolta"}, {"name": "Samuel L. Jackson"}, {"name": "Uma Thurman"}]',
        '[{"name": "Marlon Brando"}, {"name": "Al Pacino"}, {"name": "James Caan"}]',
        '[{"name": "Tom Hanks"}, {"name": "Robin Wright"}, {"name": "Gary Sinise"}]',
        '[{"name": "Brad Pitt"}, {"name": "Edward Norton"}, {"name": "Helena Bonham Carter"}]',
        '[{"name": "Robert De Niro"}, {"name": "Ray Liotta"}, {"name": "Joe Pesci"}]'
    ]
}

# Create DataFrames and save as CSV
movies_df = pd.DataFrame(movies_data)
credits_df = pd.DataFrame(credits_data)

movies_df.to_csv('tmdb_5000_movies.csv', index=False)
credits_df.to_csv('tmdb_5000_credits.csv', index=False)

print("Sample dataset created successfully!")
print("Files created: tmdb_5000_movies.csv, tmdb_5000_credits.csv")
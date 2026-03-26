import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("tmdb_5000_movies.csv")

# Use only required columns
movies = movies[['title', 'overview']]

# Remove missing values
movies.dropna(inplace=True)

# Convert text to vectors
cv = CountVectorizer(stop_words='english')
vectors = cv.fit_transform(movies['overview']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]
import streamlit as st
import pandas as pd
from model import recommend

st.title("🎬 Movie Recommendation System")

movies = pd.read_csv("tmdb_5000_movies.csv")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].dropna().values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.write("### Top 5 Recommendations")
    for movie in recommendations:
        st.write("👉", movie)
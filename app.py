import streamlit as st
import pandas as pd
import pickle
import gdown
import os

# Download similarity.pkl from Google Drive if not present
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1m2HmzO4oW6sL6J5uOJ7_LJW8eRXTdQwn"
    gdown.download(url, "similarity.pkl", quiet=False)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
"Select movie",
movies['title'].values)

if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

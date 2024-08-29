import pickle
import streamlit as st
import requests

st.header("Movie Recommendation System TMDB 2024")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key="..."&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    # Find the index of the given movie in the DataFrame
    index = movi[movi['title'] == movie].index[0]
    
    # Calculate similarity distances
    distances = sorted(list(enumerate(simi[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    # Print the recommended movies
    for i in distances[1:20]:  # Skip the first one because it's the movie itself
        movie_id = movi.iloc[i[0]].id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movi.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

movi = pickle.load(open('OTT/movie_list.pkl', 'rb'))
simi = pickle.load(open('OTT/similarity.pkl', 'rb'))

movie_list = movi['title'].values
movi_selected = st.selectbox('Search any movie for Recommendation : ', movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(movi_selected)
    cols = st.columns(5)  # Change number of columns to 5 to make images larger
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i], use_column_width=True)

    cols = st.columns(5)  # Add another row of 5 columns
    for i in range(5, 10):
        with cols[i - 5]:  # Use (i - 5) to index into the second row
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i], use_column_width=True)

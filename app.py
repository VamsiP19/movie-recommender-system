import streamlit as st
import pickle

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies=pickle.load(open('/Users/vamshi/Desktop/Code/movies-recommender-system/movies.pkl','rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('movies-recommender-system/similarity.pkl','rb'))

st.title("Vamshi's Movie Recommender system")
selected_movie_name= st.selectbox(
    'How would you lik to be contacted ?',
    movies_list
)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    for i in names:
        st.write(i)
    
import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("Esta es la primera prueba")

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')
streamlit.text('🥣Omega 3 y avena con arándanos')
streamlit.text('🥗Batido de col rizada, espinacas y rúcula')
streamlit.text('🐔Huevo de gallinas camperas hervidas')
streamlit.text('🥑🍞Advocado Toast')
streamlit.dataframe(my_fruit_list)

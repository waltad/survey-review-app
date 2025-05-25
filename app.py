import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ankieta powitalna", # Set the title of the page
    page_icon=":bar_chart:", # Set the icon of the page
    layout="wide", # Set the layout of the page
    initial_sidebar_state="expanded", # Set the initial state of the sidebar
)

st.title(":bar_chart: Ankieta powitalna") # Set the title of the app
st.write("Przegląd danych z ankiety powitalnej z kursu `Od zera do AI`.")

df = pd.read_csv('35__welcome_survey_cleaned.csv', sep=';')

st.subheader("Przykładowe dane z ankiety") # Set a subheader for the data section
st.dataframe(df.head(5), hide_index=True)  # Display the first 5 rows of the DataFrame


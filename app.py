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

c0, c1, c2 = st.columns(3)  # Create three columns for layout

with st.sidebar:
    age_categories = st.multiselect(
        "Wybierz kategorie wiekowe",
        sorted(df["age"].dropna().unique()),
    )
    edu_levels = st.multiselect(
        "Wybierz poziomy wykształcenia",
        sorted(df["edu_level"].dropna().unique()),
    )
    gender = st.radio(
        "Wybierz płeć",
        ("Wszyscy", "Kobiety", "Mężczyzni"),
    )

if age_categories:
    df = df[df["age"].isin(age_categories)]

if edu_levels:
    df = df[df["edu_level"].isin(edu_levels)]

if gender == "Kobiety":
    df = df[df["gender"] == 1]
elif gender == "Mężczyzni":
    df = df[df["gender"] == 0]

with c0:
    st.metric(label="Liczba uczestników", value=len(df))  # Display the number of unique participants
with c1:
    st.metric(label="Liczba kobiet", value=len(df[df['gender']==1]))  # Display the number of women
with c2:
    st.metric(label="Liczba mężczyzn", value=len(df[df['gender']==0]))  # Display the number

st.subheader("Przykładowe dane z ankiety") # Set a subheader for the data section
st.dataframe(df.head(5), hide_index=True)  # Display the first 5 rows of the DataFrame


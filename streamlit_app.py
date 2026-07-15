import streamlit as st
from Weather import render_weather_app
from LanguageTranslator import render_language_translator_app

st.set_page_config(page_title="AI Apps Hub", page_icon="🤖")

st.title("AI Apps Hub")
st.write("Explore both apps from one page.")

weather_tab, translator_tab = st.tabs(["🌦️ Weather Bot", "🤯 Language Translator"])

with weather_tab:
    render_weather_app()

with translator_tab:
    render_language_translator_app()

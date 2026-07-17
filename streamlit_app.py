import streamlit as st
from Weather import render_weather_app
from LanguageTranslator import render_language_translator_app
from StoryGen import render_story_gen_app
from Resume_Analyzer import render_resume_analyzer_app

st.set_page_config(page_title="AI Apps Hub", page_icon="🤖")

st.title("AI Apps Hub")
st.write("Explore all AI apps from one page.")

weather_tab, translator_tab, story_tab, resume_tab = st.tabs(["🌦️ Weather Bot", "🤯 Language Translator", "📖 Story Generator", "💼 Resume Analyzer"])

with weather_tab:
    render_weather_app()

with translator_tab:
    render_language_translator_app()

with story_tab:
    render_story_gen_app()

with resume_tab:
    render_resume_analyzer_app()

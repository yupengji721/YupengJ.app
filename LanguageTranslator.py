import streamlit as st

try:
    from transformers import pipeline
except ImportError:  # pragma: no cover - graceful fallback for deployment
    pipeline = None


def render_language_translator_app():
    st.header("🤯 AI Language Translator 🤯")
    st.write("Translate English into different languages!")

    @st.cache_resource
    def load_model():
        return pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

    languages = {
        "French": "Helsinki-NLP/opus-mt-en-fr",
        "German": "Helsinki-NLP/opus-mt-en-de",
        "Spanish": "Helsinki-NLP/opus-mt-en-es",
        "Italian": "Helsinki-NLP/opus-mt-en-it",
    }

    if pipeline is None:
        st.warning("The translator requires the transformers package to be installed.")
        return

    language = st.selectbox("Select Language:", list(languages.keys()))
    text = st.text_area("Enter your text in English:")

    if st.button("Translate"):
        translator = pipeline("translation", model=languages[language])
        result = translator(text)
        st.success(result[0]["translation_text"])


if __name__ == "__main__":
    render_language_translator_app()

import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Story Generator", page_icon=":book:")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

def render_story_gen_app():
    st.header("📖 AI Story Generator 📖")
    st.write("Generate creative stories using GPT-2.")

    generator = load_model()

    topic = st.text_input("Enter a topic for your story:", "A Leo that hacks into the weather app.")

    genre = st.selectbox("Select a genre:", ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", "Adventure", "Comedy", "Drama", "Thriller", "Historical", "Dystopian", "Post-Apocalyptic", "Cyberpunk", "Steampunk", "Urban Fantasy", "Fairy Tale", "Mythology", "Superhero", "Western", "Slice of Life", "Time Travel", "Alternate History", "Steampunk Fantasy", "Anime", "Manga", "Graphic Novel", "Visual Novel", "Creepy Pasta", "Urban Legend", "Folk Tale", "Mythical Creature Story", "Legendary Hero Story", "Epic Quest Story"])

    length = st.slider(
        "Select story length (number of words):",
        100, 400, 200, step=50
    )

    if st.button("Generate Story"):

        if topic.strip() == "":
            st.warning("Please enter a topic for your story.")
            st.stop()

        prompt = f"""
Title: {topic}
Genre: {genre}
Story: 
Once upon a time, 
"""
        
        with st.spinner("Your imagination is coming to life..."):

            result = generator(
                prompt, 
                max_new_tokens = length,
                temperature = 0.9,
                do_sample = True,
                top_p = .95, 
                repetition_penalty = 1.2,
                pad_token_id = 50256
                )
            
        story = result[0]["generated_text"]

        #Removes the prompt from the generated story
        story = story.replace(prompt, "").strip()

        st.subheader("Your Depraved Imagination Below: ")
        st.write(story)


if __name__ == "__main__":
    render_story_gen_app()

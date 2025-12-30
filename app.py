
import streamlit as st
from tts_engine import text_to_speech, get_voices
from text_validation import validate_text

st.set_page_config(page_title="Text to Speech App")
st.title("🔊 Text-to-Speech Generator")

text_input = st.text_area("Enter Text")

voices = get_voices()
voice_names = [f"{i}: {v.name}" for i, v in enumerate(voices)]

voice_choice = st.selectbox(
    "Select Voice",
    range(len(voice_names)),
    format_func=lambda x: voice_names[x]
)

rate = st.slider("Speech Rate", 100, 250, 150)
volume = st.slider("Volume", 0.0, 1.0, 1.0)

if st.button("Generate Speech"):
    valid, result = validate_text(text_input)

    if not valid:
        st.error(result)
    else:
        audio_path = text_to_speech(
            result,
            voice_choice,
            rate,
            volume
        )

        st.success("Speech generated successfully!")
        with open(audio_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")

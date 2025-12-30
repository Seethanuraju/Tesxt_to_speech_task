import pyttsx3
import os
import uuid

"""Initializes the TTS engine
Retrieves all available voices on the system
Returns a list of voices (male/female, accents, etc.)"""

def get_voices():
    engine = pyttsx3.init()
    return engine.getProperty('voices')

def text_to_speech(text, voice_index, rate, volume):
    engine = pyttsx3.init()

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)

    os.makedirs("outputs", exist_ok=True)
    filename = f"speech_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("outputs", filename)

    engine.save_to_file(text, filepath)
    engine.runAndWait()

    return filepath

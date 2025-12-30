# Text-to-Speech (TTS) Web Application

## Project Description

This project is a Python-based Text-to-Speech (TTS) application that converts user-provided text into speech. The application supports voice selection, adjustable speech rate and volume, input validation, and plays the generated audio directly in a web browser using Streamlit.

## Technologies Used

* Python
* pyttsx3
* Streamlit
* PyTest

## Project Setup

1. Open the project folder in VS Code.
2. Install required dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run unit tests:

   ```
   pytest test_validation.py
   ```
4. Start the web application:

   ```
   streamlit run app.py
   ```

## How to Use

1. Enter text in the text area.
2. Select a voice from the dropdown.
3. Adjust speech rate and volume.
4. Click **Generate Speech**.
5. Listen to the audio output in the browser.

## Author

Raju Seethanu

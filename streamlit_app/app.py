import streamlit as st
import openai
import os
import pyttsx3
import whisper
import tempfile
import time
from datetime import datetime

# Initialize TTS engine
engine = pyttsx3.init()

# Set OpenAI API key from environment variable (works on Render)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Whisper model for STT
whisper_model = whisper.load_model("base")

# Function to convert voice to text
def transcribe_audio(audio_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        temp.write(audio_file.read())
        temp_path = temp.name
    result = whisper_model.transcribe(temp_path)
    return result["text"]

# Function to get LLM response
def ask_llm(context, question):
    prompt = f"Context: {context}\nQuestion: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Function to speak out response
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Streamlit UI
st.set_page_config(page_title="Voice Finance Assistant", layout="wide")
st.title("🎙️ Voice-Powered Finance Assistant")
st.markdown("Ask finance-related questions using your voice!")

# Upload audio
audio_input = st.file_uploader("Upload your question as a voice file (.wav)", type=["wav"])

if audio_input:
    st.info("Transcribing your audio...")
    with st.spinner("Transcribing..."):
        transcribed_text = transcribe_audio(audio_input)
        st.success("Transcription Complete!")
        st.write("🗣️ You said:", transcribed_text)

    # LLM response
    st.info("Generating response from assistant...")
    with st.spinner("Thinking..."):
        context = "Risk exposure in Asian tech stocks and earnings surprises."
        llm_response = ask_llm(context, transcribed_text)
        st.success("Here’s your answer:")
        st.markdown(f"💬 **Assistant:** {llm_response}")

        # Speak response
        with st.spinner("Speaking..."):
            speak_text(llm_response)

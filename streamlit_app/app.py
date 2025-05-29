import streamlit as st
import openai
import os
import pyttsx3

# Load OpenAI API Key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Voice-Enabled Finance Assistant")

# Step 1: Upload Audio
audio_file = st.file_uploader("🎙️ Upload your audio question (mp3/wav/m4a)", type=["wav", "mp3", "m4a"])

if audio_file is not None:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())

    # Step 2: Transcribe
    with open("temp_audio.wav", "rb") as audio:
        transcript = openai.Audio.transcribe("whisper-1", audio)

    st.markdown("#### 📝 Transcribed Text")
    st.write(transcript["text"])

    # Step 3: Ask LLM
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": transcript["text"]}]
    )
    answer = response['choices'][0]['message']['content']

    st.markdown("#### 💡 Assistant's Answer")
    st.write(answer)

    # Step 4: Convert Answer to Speech
    engine = pyttsx3.init()
    engine.save_to_file(answer, 'response.mp3')
    engine.runAndWait()

    # Step 5: Play Audio
    audio_response = open('response.mp3', 'rb')
    audio_bytes = audio_response.read()
    st.audio(audio_bytes, format='audio/mp3')

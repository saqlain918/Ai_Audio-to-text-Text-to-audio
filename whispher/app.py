import streamlit as st
import whisper
from pydub import AudioSegment
import tempfile
import requests
import os

st.title("🎙️ Whisper + vapi TTS")

# -----------------------
# PART 1: AUDIO → TEXT
# -----------------------
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg", "m4a"])

if uploaded_file:
    st.audio(uploaded_file, format='audio/wav')

    # Save uploaded audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio_bytes = uploaded_file.read()
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    # Convert to wav if needed
    if uploaded_file.name.endswith((".mp3", ".m4a", ".ogg")):
        sound = AudioSegment.from_file(tmp_path)
        tmp_path = tmp_path.replace(".mp3", ".wav").replace(".m4a", ".wav").replace(".ogg", ".wav")
        sound.export(tmp_path, format="wav")

    # Transcribe with Whisper
    st.info("Transcribing with Whisper...")
    model = whisper.load_model("base")  # tiny, base, small, medium, large
    result = model.transcribe(tmp_path)

    st.success("✅ Transcription Complete!")
    st.text_area("Transcribed Text", value=result["text"], height=200)

# -----------------------
# PART 2: TEXT → AUDIO (TTS)
# -----------------------
st.subheader("🗣️ Convert Text to Speech with ")
input_text = st.text_area("Enter text to convert to speech:")

if st.button("Generate Audio with "):
    if input_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        ELEVEN_API_KEY = "Elenenlab Api key"  # 🔑 replace with your key
        VOICE_ID = "pqHfZKP75CvOlQylNhV4"  # can be Rachel, Domi, Bella, or your own voice ID
        ELEVEN_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

        headers = {
            "xi-api-key": ELEVEN_API_KEY,
            "Content-Type": "application/json"
        }

        data = {
            "text": input_text,
            "voice_settings": {
                "stability": 0.75,
                "similarity_boost": 0.9
            }
        }

        response = requests.post(ELEVEN_URL, headers=headers, json=data)

        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_audio:
                tmp_audio.write(response.content)
                tmp_audio_path = tmp_audio.name

            st.success("✅ Audio generated successfully!")
            st.audio(tmp_audio_path, format="audio/mp3")
        else:
            st.error(f"❌ ElevenLabs Error: {response.status_code} - {response.text}")


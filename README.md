## Whisper + ElevenLabs TTS with Streamlit

A simple speech-to-text (STT) and text-to-speech (TTS) app built with Streamlit, OpenAI Whisper, and ElevenLabs. Upload audio files for transcription or convert text into realistic human-like speech.

## What it does

- Transcribes audio files into text using OpenAI Whisper
- Converts typed text into realistic speech using ElevenLabs TTS
- Provides simple web interface for audio processing
- Supports multiple audio formats for input
- Delivers high-quality speech synthesis output
- Offers seamless integration between STT and TTS workflows

## Features

- Audio Upload: Support for .mp3, .wav, .ogg, .m4a formats
- Speech-to-Text: Accurate transcription using Whisper
- Text Display: Shows transcription in editable text box
- Text-to-Speech: Converts text to realistic speech with ElevenLabs
- Web Interface: Simple, user-friendly Streamlit app
- Real-time Processing: Quick audio conversion and synthesis

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/whisper-elevenlabs-tts.git
   cd whisper-elevenlabs-tts
   ```

2. Create virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## API Key Setup

### ElevenLabs API Key
1. Create an account at https://elevenlabs.io/
2. Go to Profile → API Keys and copy your key
3. Replace the placeholder in the code:
   ```python
   ELEVEN_API_KEY = "your_api_key_here"
   ```

### Voice ID Configuration
Use a valid voice_id (e.g., Rachel → 21m00Tcm4TlvDq8ikWAM)

To fetch available voices:
```python
import requests
headers = {"xi-api-key": "your_api_key_here"}
voices = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers).json()
print(voices)
```

## How to use

1. Start the Streamlit server:
   ```
   streamlit run app.py
   ```

2. Open your browser at http://localhost:8501

3. Usage options:
   - **Speech-to-Text:** Upload an audio file and get transcription
   - **Text-to-Speech:** Enter text and generate speech audio
   - **Combined Workflow:** Transcribe audio, edit text, then convert back to speech

## Project Structure

```
whisper-elevenlabs-tts/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Dependencies

- streamlit
- whisper
- pydub
- requests
- elevenlabs

## Requirements

- Python 3.8+
- ElevenLabs API key
- Internet connection for TTS API calls
- Audio input files for transcription
- Sufficient storage for temporary audio processing

## Tech Stack

**Frontend:** Streamlit for web interface
**Speech-to-Text:** OpenAI Whisper for transcription
**Text-to-Speech:** ElevenLabs API for speech synthesis
**Audio Processing:** Pydub for format conversion
**Backend:** Python for application logic

## Use Cases

- Audio transcription and documentation
- Creating voiceovers from text content
- Accessibility applications for hearing/vision impaired
- Language learning and pronunciation practice
- Content creation and podcasting workflows
- Meeting transcription and audio notes

## Supported Audio Formats

**Input Formats:**
- MP3
- WAV
- OGG
- M4A

**Output Format:**
- High-quality synthesized speech audio

## Notes

- Whisper runs locally for privacy and speed
- ElevenLabs provides realistic voice synthesis
- Simple interface suitable for non-technical users
- Extensible architecture for additional features
- Real-time processing capabilities

## Future Enhancements

- Multiple voice selection options
- Batch audio processing capabilities
- Audio editing and trimming features
- Custom voice training integration
- Multi-language support expansion
- Export options for different audio formats

## Built with

- Python
- Streamlit
- OpenAI Whisper
- ElevenLabs API
- Pydub

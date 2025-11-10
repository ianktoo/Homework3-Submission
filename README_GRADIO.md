# Voice Agent with Gradio Interface

This project provides an interactive voice agent with a Gradio web interface for seamless voice and text-based conversations.

## Features

### 🎤 Voice Chat
- Upload audio files or record directly using your microphone
- Automatic speech-to-text transcription using Whisper
- AI-powered responses using Ollama (smollm2:1.7b)
- Text-to-speech conversion using BentoML
- View both transcribed text and audio responses

### 💬 Text Chat
- Direct text-based conversation with the AI agent
- Maintains conversation history
- Clean, intuitive chat interface

## Prerequisites

Before running the Gradio interface, ensure the following services are running:

1. **Ollama** (Port 11434)
   ```bash
   ollama serve
   ```

2. **BentoML TTS Service** (Port 3000)
   ```bash
   # Start your BentoML TTS service
   bentoml serve <your-tts-service>
   ```

3. **FastAPI** (Port 8000) - Optional
   ```bash
   # If you have a FastAPI service
   python src/main.py
   ```

## Installation

1. Install required dependencies:
   ```bash
   pip install gradio requests whisper ollama bentoml
   ```

2. Ensure your project structure includes:
   ```
   src/
   ├── voice_agent.ipynb
   └── utils/
       ├── voice_agent.py
       └── tts.py
   ```

## Usage

### Running the Gradio Interface

1. Open the notebook:
   ```bash
   jupyter notebook src/voice_agent.ipynb
   ```

2. Run all cells in order:
   - First cells set up directories and check network connectivity
   - The main Gradio interface cell launches the web UI
   - The interface will be available at `http://127.0.0.1:7860`

3. Access the interface in your browser at the provided URL

### Using Voice Chat

1. Navigate to the "🎤 Voice Chat" tab
2. Either:
   - Click "Upload Audio" to select an audio file
   - Click the microphone icon to record directly
3. Click "Process Audio"
4. View the results:
   - Status message
   - Your transcribed message
   - AI agent's text response
   - AI agent's audio response (playable)

### Using Text Chat

1. Navigate to the "💬 Text Chat" tab
2. Type your message in the text box
3. Click "Send" or press Enter
4. View the conversation history
5. Use "Clear Conversation" to start fresh

## Project Structure

```
src/
├── voice_agent.ipynb          # Main Gradio interface
├── utils/
│   ├── voice_agent.py         # Core voice agent functions
│   └── tts.py                 # Text-to-speech utilities
└── data/
    └── audio/
        ├── conversations/     # Saved conversation audio
        └── test/             # Test audio files
```

## Key Functions

### `process_audio(audio_file)`
Processes audio through the complete pipeline:
1. Transcribes audio to text using Whisper
2. Generates AI response using Ollama
3. Converts response to speech using BentoML

### `chat_with_text(user_message, history)`
Handles text-based conversations:
1. Sends user message to Ollama
2. Receives AI response
3. Updates conversation history

## Troubleshooting

### Services Not Available
If you see "❌ Service: Not available" messages:
- Ensure Ollama is running: `ollama serve`
- Ensure BentoML TTS service is running
- Check that services are accessible at the specified ports

### Audio Processing Errors
- Ensure audio files are in supported formats (m4a, mp3, wav)
- Check that Whisper model is properly installed
- Verify BentoML TTS service is responding

### Import Errors
- Ensure all dependencies are installed
- Check that `utils/voice_agent.py` and `utils/tts.py` exist
- Verify Python path includes the project directory

## Configuration

Default service endpoints (can be modified in the notebook):
- FastAPI: `http://127.0.0.1:8000`
- Ollama: `http://127.0.0.1:11434`
- BentoML: `http://127.0.0.1:3000`

## Notes

- The interface runs on `http://127.0.0.1:7860` by default
- Conversation history is maintained during the session
- Audio responses are saved to `data/audio/conversations/`
- The agent uses the smollm2:1.7b model via Ollama
- Conversation context includes the last 5 messages

## License

See LICENSE file for details.


from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

from utils.voice_agent import transcribe_audio_to_text, generate_audio_response, generate_text_response

app = FastAPI() # Initialize fast api

@app.get("/")
async def home():
    return {
        "message": "We're good! ✅",
        "extra-info":"Just had breakfast!"
    }

@app.post("/chat/")
async def chat_endpoint(file: UploadFile = File(...), conversation_id : str = "0"):
    """
    Accepts an audio file, transforms it using the pipeline:
        ASR -> LLM -> TTS
    """

    # TODO return FileResponse("audio_file",media_type="audio/wav")
    return {
        "message":"okay",
        "conversation_id":conversation_id
    }
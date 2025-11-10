import bentoml
import requests
import json
import asyncio
import logging
import whisper
import os

from ollama import chat
from ollama import ChatResponse
from ollama import AsyncClient
from typing import Any


# Todo: Set logging preferences

BENTO_ML = "http://127.0.0.1:3000/synthesize"

conversation_history = []

def transcribe_audio_to_text(audio_bytes)-> dict:
    """
    Transcribes audio to text
    """
    model = whisper.load_model("base")
    text_result = model.transcribe(audio_bytes)
    return text_result


def generate_text_response(user_prompt:str)-> str:
    """
    Generates text from user prompt using a LLM (local ollama)
    """

    message = {
        'role':'user',
        'content':user_prompt
    }

    conversation_history.append(message)

    # Use the last 5 messages from conversation history
    messages = conversation_history[-5:]
    
    outputs: ChatResponse = chat(model="smollm2:1.7b", messages=messages)

    bot_response = outputs['message']['content']

    conversation_history.append({
        'role': 'assistant', 'content': bot_response
    })

    return bot_response

def generate_audio_response(llm_text:str, output_folder: str = "audio"):
    """
    Generates speech from text
    """

    os.makedirs(output_folder, exist_ok=True)

    # Define the endpoint URL
    url = f'{BENTO_ML}/synthesize'

    # Define the headers
    headers = {
        'accept': 'audio/*',
        'Content-Type': 'application/json'
    }

    # Define the JSON payload (the body of the request)
    payload = {
        "text": llm_text,
        "lang": "en"
    }

    try:
        # Make the POST request
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Check for a successful response (status code 200)
        response.raise_for_status()

        # The content type is 'audio/*', so you'll likely want to save the binary content.
        # The actual file extension (.mp3, .wav, etc.) will depend on the API's response headers.
        
        # Example: Save the audio content to a file
        with open(f'{output_folder}/synthesized_audio.mp3', 'wb') as f:
            f.write(response.content)

        print("✅ Request successful. Audio saved to 'synthesized_audio.mp3'.")
        print(f"Status Code: {response.status_code}")
        # print(f"Headers: {response.headers}") # Uncomment to see response headers

    except requests.exceptions.HTTPError as errh:
        print(f"❌ HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"❌ Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"❌ Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"❌ An error occurred: {err}")
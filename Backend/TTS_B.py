import requests
from playsound import playsound
import os
import uuid
from typing import Union

def generate_audio(message: str, voice: str = "Brian") -> Union[bytes, None]:
    """Fetches TTS audio from StreamElements API."""
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"[⚠️] TTS API Error: {e}")
        return None

def speak(message: str, voice: str = "Brian", folder: str = "", extension: str = ".mp3") -> None:
    """Generates and plays TTS audio."""
    audio_data = generate_audio(message, voice)
    
    if audio_data:
        # Generate a unique filename to prevent overwriting
        filename = f"{uuid.uuid4().hex}{extension}"
        file_path = os.path.join(folder, filename)

        try:
            with open(file_path, "wb") as file:
                file.write(audio_data)

            playsound(file_path)  # Play the generated audio
            os.remove(file_path)  # Delete the file after playing
        except Exception as e:
            print(f"[⚠️] Error playing TTS: {e}")
    else:
        print("[❌] Failed to generate TTS audio.")


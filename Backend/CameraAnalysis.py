import google.generativeai as genai
import cv2
import numpy as np
import time
from Backend.TTS_B import speak  # Your custom TTS function
from PIL import Image
from dotenv import dotenv_values
import speech_recognition as sr  # For voice command detection
import json

# Configure Google Gemini AI API
env_vars = dotenv_values(".env")
GEMINI_API_KEY = env_vars.get("GeminiAPIKey")

genai.configure(api_key=GEMINI_API_KEY)

def analyze_screen(image):
    """Sends the captured frame to Google's Gemini AI for analysis."""
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(["Describe in short what is happening in this frame:", image])
    return response.text

def analyze_once():
    """Analyzes a single frame from the webcam and returns the analysis.
    This is a non-blocking version for integration with Jarvis."""
    print("\n[📸] Capturing webcam frame...")
    
    cap = cv2.VideoCapture(0)  # Start webcam
    if not cap.isOpened():
        print("[❌] Error: Could not open webcam")
        return None

    try:
        ret, frame = cap.read()
        if not ret:
            print("[❌] Failed to capture frame")
            return None

        # Convert OpenCV frame to PIL Image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        print("[🤖] Analyzing webcam frame with Google AI...")
        analysis = analyze_screen(image)
        print("[🗣️] AI Analysis:", analysis)

        # Store the camera analysis in the chat log
        try:
            with open(r"Data\ChatLog.json", "r") as f:
                chat_log = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            chat_log = []

        # Add the camera analysis to the chat log
        chat_log.append({
            "role": "system",
            "content": f"Camera Analysis: {analysis}"
        })

        # Save the updated chat log
        with open(r"Data\ChatLog.json", "w") as f:
            json.dump(chat_log, f, indent=4)

        return analysis

    except Exception as e:
        print(f"[⚠️] Error analyzing webcam: {str(e)}")
        return None
    finally:
        cap.release()
        cv2.destroyAllWindows()

def listen_for_command():
    """Listens for the user's voice command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[🎙️] Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds max
            command = recognizer.recognize_google(audio).lower()
            print(f"[🎧] You said: {command}")
            return command
        except sr.UnknownValueError:
            print("[⚠️] Couldn't understand the command.")
            return None
        except sr.RequestError:
            print("[⚠️] Could not request results.")
            return None

def main():
    """Waits for the command to start and stop webcam analysis."""
    while True:
        command = listen_for_command()
        
        if command in ["start analysis", "analyze", "start"]:
            speak("Starting webcam analysis")
            print("\n[🤖] Analyzing webcam feed with Google AI...")

            cap = cv2.VideoCapture(0)  # Start webcam
            if not cap.isOpened():
                print("[❌] Error: Could not open webcam")
                speak("Error opening webcam")
                continue

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("[❌] Failed to capture frame")
                    break

                # Convert OpenCV frame to PIL Image
                image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                try:
                    analysis = analyze_screen(image)
                    print("[🗣️] AI Analysis:", analysis)
                    speak(analysis)  
                except Exception as e:
                    print("[⚠️] Error analyzing screen:", str(e))

                # Check if the user says "stop analysis"
                stop_command = listen_for_command()
                if stop_command in ["stop analysis", "stop"]:
                    speak("Stopping webcam analysis")
                    print("[🛑] Stopping analysis...")
                    break

                time.sleep(2)  # Adjust time interval

            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

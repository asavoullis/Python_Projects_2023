import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
import platform

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to speak text using VLC (for Linux) or afplay (for macOS)
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")

    # Use VLC for Linux or afplay for macOS
    if platform.system() == "Linux":
        subprocess.Popen(["vlc", "response.mp3"])
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["afplay", "response.mp3"])


# Function to handle voice commands
def process_command(command):
    if "hello" in command:
        return "Hello, how can I help you?"
    elif "bye" in command:
        return "Goodbye!"
    else:
        return "I'm sorry, I didn't understand that."

# Main loop
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
            print("Recognizing...")

        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)

        response = process_command(command)
        speak(response)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, there was an error recognizing your voice. Error: {e}")


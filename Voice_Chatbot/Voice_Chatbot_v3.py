import speech_recognition as sr
from gtts import gTTS
import os
import platform  # Import the platform module


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
nltk.download('punkt')

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to speak text using VLC (for Linux) or afplay (for macOS)
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")

    # Use VLC for Linux or afplay for macOS
    if platform.system() == "Linux":
        os.system("vlc response.mp3")
    elif platform.system() == "Darwin":  # macOS
        os.system("afplay response.mp3")



# Main loop
while True:

    # Create a chatbot instance
    chatbot = ChatBot('MyBot')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot on the English language
    trainer.train('chatterbot.corpus.english')


    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
            print("Recognizing...")

        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)

        if command.lower() == 'exit':
            break
        
        response = chatbot.get_response(command)
        print("Bot:", response)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, there was an error recognizing your voice. Error: {e}")

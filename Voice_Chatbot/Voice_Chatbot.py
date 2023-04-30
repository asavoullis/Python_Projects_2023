import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""

def respond(text):
    response = f"You said: {text}"
    print(response)
    engine.say(response)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input.lower() == "exit":
            print("Exiting the chatbot...")
            break
        if user_input:
            respond(user_input)

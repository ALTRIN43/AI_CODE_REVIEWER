import speech_recognition as sr
import pyttsx3
from compiler import analyze_file

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function for voice commands
def listen_command():
    with sr.Microphone() as source:
        speak_text("Listening... Say 'review file' or 'exit now'.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        if "review file" in command:
            analyze_file()
        elif "exit now" in command:
            speak_text("Goodbye!")
            exit()
    except sr.UnknownValueError:
        speak_text("Sorry, I didn't understand.")
    except sr.RequestError:
        speak_text("API error. Try again.")

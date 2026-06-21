#pip install pyttsx3
import pyttsx3

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
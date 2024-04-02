import datetime

import pyttsx3 as tts
import speech_recognition as sr

engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def speak(data):
    engine.say(data)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us ')
        print(f"You said: {query}")

    except Exception:
        print("Say that again please...")
        return "None"
    return query


def wish_me(greet="How can i help you"):
    time = datetime.datetime.now().hour
    if 0 <= time < 12:
        speak("Hi I am edwin, Good morning")
    elif 12 <= time < 18:
        speak("Hi I am edwin, Good afternoon")
    else:
        speak("hi I am edwin, good evening")
    speak(greet)



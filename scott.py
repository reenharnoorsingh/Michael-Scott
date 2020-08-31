import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')  # using Microsoft Speech API
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)  # sets voice DAVID


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # wishes the user acoording to time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon")
    else:
        speak("Good Evening!")

    speak("My name is Michael Scott. What can I do for you today?")


def takeCommand():  # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you......")
        # pause_threshold is seconds of non speaking audio before a phrase os considered complete
        r.pause_threshold = 1
        audio = r.listen(source)  # listens to the user
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        print("Say that again please.....")
        return None
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    # Task excecution based on query

    if 'wikipedia' in query: #searches and speaks wikipedia
        speak("Searching Wikipedia.....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia")
        print(results)
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')

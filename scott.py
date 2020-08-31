import pyttsx3  # pip install pyttsx3
import datetime
engine = pyttsx3.init('sapi5')  # using Microsoft Speech API
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)  # sets voice DAVID


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(): #wishes the user acoording to time 
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon")
    else:
        speak("Good Evening!")
    
    speak("My name is Michael Scott, Dunder Mifflin. What can I do for you today?")


if __name__ == "__main__":
    wishMe()

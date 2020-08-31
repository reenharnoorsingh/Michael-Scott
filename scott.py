import pyttsx3  # pip install pyttsx3

engine = pyttsx3.init('sapi5')  # using Microsoft Speech API
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)  # sets voice DAVID


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("My name is Michael Scott")
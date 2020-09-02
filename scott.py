import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')  # using Microsoft Speech API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # sets voice DAVID


def speak(audio):  # speak function
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    intro = "My name is Michael Scott. What can I do for you today? That's What She Said" #intro message
    print(intro)
    speak(intro)


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you...")
        # pause_threshold is seconds of non speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        audio = r.listen(source)    # listens to the user

    try:
        print("Recognizing...")
        # using google for voice recognition
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # user query will be printed

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'hi' in query:
            msg = "Hello what can I do for you?"
            print(msg)
            speak(msg)
            
        if 'wikipedia' in query:  # searches and speaks wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.get(
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("stackoverflow.com")

        elif 'open netflix' in query:
            webbrowser.get(
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("netflix.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Harnoor Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open spotify' in query:
            spotify = "C:\\Users\\Harnoor Singh\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify)
        
        elif 'open powershell' in query:
            powershell = "%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe"
            os.startfile(powershell)

        elif 'tell me about yourself' in query:
            about = "My name is Micheal Scott, I work in a paper company called Dunder Mifflin in Scranton,Pennsylvania as Regional Manager. Some of my colleagues say that I am The Best Boss Ever. I am married to Holly Flax, she lives in Colorado. Currenty I am employed on Harnoor's Computer"
            print(about)
            speak(about)

        elif 'who do you work with' in query:
            colleagues = "I work with one of the best people in Scranton. I love my employees even though I hit one of them with my car. Pam Beesly Halpert is my best friend and the office administrator. Jim Halpert is a prankster and a true friend who is now a co-ownwer of sports startup Athleap. Dwight Schrute is the Assistant to the Regional Manager at Dunder Mifflin and my right hand guy. Oscar Martinez, Angela Schrute and Kevin Malone are my accountants. Creed Bratton and Meredith Palmer are in Quality Assurance. Fun Fact, Meredith was the one I hit with the car. Ryan Howard, the temp is my prodigee. Stanley Hudsonn, Andy Bernard and Phyllis Vance, Vance Refrigeration make up the sales. Kelly Kapoor is in Customer Service. And the person I hate the most Toby Flenderson is in HR"
            print(colleagues)
            speak(colleagues)

        elif "tell a joke" in query:
            joke= "If I had a gun with two bullets and I was in a room with Hitler, Bin Laden, and Toby, I would shoot Toby twice. That's What She Said"
            print(joke)
            speak(joke)

        elif 'goodbye' in query:
            msg1="Have a nice day!"
            print(msg1)
            speak(msg1)
            exit()

import speech_recognition as sr
import pyttsx3
import datetime
import os
import subprocess

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 170)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am JARVIS. How can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"You said: {query}")
    except Exception as e:
        print("Could not understand. Say that again please.")
        return ""
    return query.lower()

def open_app(query):
    if 'notepad' in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif 'chrome' in query:
        speak("Opening Google Chrome")
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path])
        else:
            speak("Chrome is not installed in the default path.")

    elif 'file explorer' in query or 'explorer' in query:
        speak("Opening File Explorer")
        os.system("explorer")

    elif 'calculator' in query:
        speak("Opening Calculator")
        os.system("calc")

    elif 'command prompt' in query or 'cmd' in query:
        speak("Opening Command Prompt")
        os.system("start cmd")

    else:
        speak("Sorry, I cannot recognize the application.")

if __name__ == "__main__":
    greet_user()

    while True:
        query = takeCommand()

        if 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye, Harish.")
            break

        if 'open' in query or 'launch' in query or 'start' in query:
            open_app(query)

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

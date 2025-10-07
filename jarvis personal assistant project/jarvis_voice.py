import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"🧠 J.A.R.V.I.S.: {text}")
    engine.say(text)
    engine.runAndWait()

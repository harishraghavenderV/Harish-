import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
            return ""
        except sr.RequestError:
            print("🔌 Speech recognition service error.")
            return ""

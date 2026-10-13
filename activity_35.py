import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")

        except sr.RequestError as e:
            print(f"❌ API Error: {e}")

    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "your name" in command:
        speak("I am your voice assistant.")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False

    
    elif "google" in command: 
        import webbrowser
        webbrowser.open("https://www.google.com")

    else: 
        speak("I'm sorry, I didn't understand that command.")

    return True

def main():
    speak("Welcome! I am your voice assistant. How can I help you today?")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()
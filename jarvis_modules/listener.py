import speech_recognition as sr
import time
from jarvis_modules import notify
from jarvis_modules.speech import speak


r = sr.Recognizer()
def jarvis_speech_recognize():
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source, timeout=2, phrase_time_limit=1)
        # Wake up command
        word = r.recognize_google(audio)
        return word

def jarvis_activate():
    speak("Yes, how can i help you?")
    print("jarvis active...")
    # Google Speech recognition
    with sr.Microphone() as source:
        audio = r.listen(source)
        command = r.recognize_google(audio)
        return command
    
def jarvis_stop():
    speak("closing jarvis")
    print("closing jarvis.....")
    # Notification system
    notify.notify_stop()
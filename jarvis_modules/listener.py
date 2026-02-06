import speech_recognition as sr
import time
from jarvis_modules import notify
from jarvis_modules.speech import speak
from data_handling import DataHandling

data = DataHandling()
assistant_name = data.get_settings("basic", "assistant_name")


r = sr.Recognizer()
def jarvis_speech_recognize():
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source, timeout=2, phrase_time_limit=1)
        # Wake up command
        word = r.recognize_google(audio)
        return word

def jarvis_activate():
    with sr.Microphone() as source:
        audio = r.listen(source)
        command = r.recognize_google(audio)
        return command
    
def jarvis_stop():
    speak(f"closing {assistant_name}")
    print(f"closing {assistant_name}.....")
    # Notification system
    notify.notify_stop()
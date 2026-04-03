import time
import plyer.platforms.win.notification
from modules import notify
# from jarvis_modules.commands import CommandHandling
from modules.voice.speech import speak
from modules.voice.listener import jarvis_activate, jarvis_speech_recognize, jarvis_stop
from modules.data_handler.data_handling import DataCollecting
from modules.commands.core import CommandHandling

commands = CommandHandling()
data = DataCollecting()
assistant_name = data.get_settings("basic", "assistant_name")



def stop_jarvis_execution():
    global is_running
    is_running = False

def run_jarvis(word=True):
    global is_running
    is_running = True
    # Guide
    print(f"Say stop program' to stop {assistant_name}\n")
    speak(f"Activating {assistant_name}")
    notify.notify_start()

    # Time Checking --- notification 
    last_active = time.time()
    timeout_duration = data.get_settings("basic", "timeout_seconds")


    while is_running:
        print("Listening.......")
        # Closing notification --- time limit
        if time.time() - last_active > timeout_duration:
            notify.notify_timeout()
            break

        try:
            command = jarvis_activate()

            if not is_running:
                print("Jarvis successfully closed.")
                break
            if command is None:
                continue

            print(f"You: '{command}'")
            last_active = time.time()
            if command.lower() in [f"stop program", "stop {assistant_name}"]:
                jarvis_stop()
                break
            else:
                commands.processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))
            print(f"\n'stop {assistant_name}' or 'stop program' to stop {assistant_name}\n")


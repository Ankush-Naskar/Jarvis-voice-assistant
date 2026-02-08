import time
import plyer.platforms.win.notification
from jarvis_modules import notify
from jarvis_modules.commands import CommandHandling
from jarvis_modules.speech import speak
from jarvis_modules.listener import jarvis_activate, jarvis_speech_recognize, jarvis_stop
from data_handling import DataHandling

commands = CommandHandling()
data = DataHandling()
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

            print(f"DEBUG: I heard '{command}'")
            last_active = time.time()
            if command.lower() in [f"stop program", "stop {assistant_name}"]:
                jarvis_stop()
                break
            commands.processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))
            print(f"\n'stop {assistant_name}' or 'stop program' to stop {assistant_name}\n")


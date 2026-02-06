import time
from jarvis_modules import commands, notify
from jarvis_modules.speech import speak
from jarvis_modules.listener import jarvis_activate, jarvis_speech_recognize, jarvis_stop
from data_handling import DataHandling

data = DataHandling()
assistant_name = data.get_settings("basic", "assistant_name")

# Guide
print(f"Say stop program' to stop {assistant_name}\n")
speak(f"Activating {assistant_name}")
notify.notify_start()

            
if __name__ == "__main__":

    # Time Checking --- notification 
    last_active = time.time()
    timeout_duration = data.get_settings("basic", "timeout_seconds")
    while True:
        print("Listening.......")
        # Closing notification --- time limit
        if time.time() - last_active > timeout_duration:
            notify.notify_timeout()
            break

        try:
            command = jarvis_activate()
            print(f"DEBUG: I heard '{command}'")
            if command.lower() in [f"stop program", "stop {assistant_name}"]:
                jarvis_stop()
                break
            commands.processCommand(command)
            last_active = time.time()

        except Exception as e:
            print("error; {0}".format(e))
            print(f"\n'stop {assistant_name}' or 'stop program' to stop {assistant_name}\n")
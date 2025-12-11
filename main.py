import time
from jarvis_modules.file_and_data_handling import create_user_info
create_user_info()
from jarvis_modules import command_handling, notify
from jarvis_modules.speech import speak
from jarvis_modules.speech_recognization import jarvis_activate, jarvis_speech_recognize, jarvis_stop
import user_settings

# Guide
print("say 'jarvis' to start\nand 'stop program' to stop jarvis\n")
speak("Initializing jarvis......")
notify.notify_start()

            
if __name__ == "__main__":

    # Time Checking --- notification 
    last_active = time.time()
    timeout_duration = user_settings.DURATION_OF_TIMEOUT
    while True:
        print("Recognizing.....")
        # Closing notification --- time limit
        if time.time() - last_active > timeout_duration:
            notify.notify_timeout()
            break

        try:
            word = jarvis_speech_recognize()
            # activating jarvis 
            if word.lower() in ["jarvis", "hello jarvis"]:
                command = jarvis_activate()
                command_handling.processCommand(command)
                last_active = time.time()
            # Closing Jarvis
            elif word.lower() in ["stop program", "stop jarvis"]:
                jarvis_stop()
                break

        except Exception as e:
            print("error; {0}".format(e))
            print("\nsay 'jarvis' to start\nand 'stop jarvis' to stop jarvis\n")
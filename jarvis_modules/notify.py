from plyer import notification
from data_handling import DataHandling

data = DataHandling()
assistant_name = data.get_settings("basic", "assistant_name")



def notify_start():
    notification.notify(
        title=f"{assistant_name}",
        message=f"{assistant_name} is listening!\nSay 'stop {assistant_name}' or 'stop program to stop.",
        timeout=5
    )

def notify_timeout():
    notification.notify(
        title=f"{assistant_name}",
        message=f"No activity detected. Shutting down {assistant_name}.",
        timeout=5
    )
    print(f"No activity detected. Shutting down {assistant_name}.")

def notify_stop():
    notification.notify(
        title=f"{assistant_name}",
        message=f"{assistant_name} closed.",
        timeout=5
    )
    print(f"{assistant_name} closed")
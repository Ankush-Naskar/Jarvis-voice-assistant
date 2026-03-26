from modules.voice.speech import speak
from modules.services.weather import get_current_weather, get_weather_by_date
from datetime import datetime, timedelta
import asyncio
from data_handling import DataHandling



class WeatherHandling():
    def __init__(self):
        data_handling = DataHandling()
        self.location = data_handling.get_settings("basic", "location")

    def weather_update(self, c):
        Location = self.location
        
        if "current" in c.lower():
            l = asyncio.run(get_current_weather(Location))
            speak(l)
        elif "today" in c.lower():
            today = datetime.today().date()
            l = asyncio.run(get_weather_by_date(Location, today))
            speak("today," + l)
        elif "tomorrow" in c.lower():
            tomorrow = (datetime.today().date() + timedelta(days=1))
            l = asyncio.run(get_weather_by_date(Location, tomorrow))
            speak("tomorrow," + l)
        else:
            l = asyncio.run(get_current_weather(Location))
            speak(l)
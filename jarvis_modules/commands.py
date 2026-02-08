import webbrowser
from jarvis_modules.speech import speak
from jarvis_modules.weather import get_current_weather, get_weather_by_date
from datetime import datetime, timedelta
import asyncio
from data_handling import DataHandling
from jarvis_modules.ai_service import ArtificialIntelligence



class CommandHandling():
    def __init__(self):
        self.data_handling = DataHandling()
        self.ai = ArtificialIntelligence()

    def google_search(self, c):
        search = " ".join(c.lower().split(" ")[1:])
        speak(f"Searching {search} in google")
        query = search.replace(" ", "+")
        link = f"https://www.google.com/search?q={query}"
        webbrowser.open(link) 

    def link_open(self, c):
        key = " ".join(c.lower().split(" ")[1:])
        link = self.data_handling.get_bookmarks("links", key)
        if link:
            speak(f"opening {key}")
            webbrowser.open(link)
        else:
            self.google_search(c)

    def play_YT_song_video(self, c):
        song = " ".join(c.lower().split(" ")[1:])
        link = self.data_handling.get_bookmarks("videos", song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Playing {song} from YouTube")
            query = song.replace(" ", "+")
            song_link = f"https://www.google.com/search?q={query}+site:youtube.com&btnI"
            webbrowser.open(song_link)
  
    def weather_update(self, c):
        Location = self.data_handling.get_settings("basic", "location")
        
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

    def processCommand(self, c):
        # Opening links.
        if c.lower().startswith("open"):
            self.link_open(c)
        # Google search.
        elif c.lower().startswith("search"):
            self.google_search(c)
        # Playing songs
        elif c.lower().startswith("play"):
            self.play_YT_song_video(c)
        # Weather updates
        elif "weather update" in c.lower():
            self.weather_update(c)
        # Ai integration --OpenAi
        else:
            try:
                speak(self.ai.AI(c))
            except:
                return "Error occurred !"


from modules.commands.browser_cmd import BrowserHandling
from modules.commands.weather_cmd import WeatherHandling
from modules.voice.speech import speak
from modules.services.ai_service import ArtificialIntelligence

class CommandHandling():
    def __init__(self):
        self.bh = BrowserHandling()
        self.wh = WeatherHandling()
        self.ai = ArtificialIntelligence()

    def processCommand(self, c):
        # Opening links.
        if c.lower().startswith("open"):
            self.bh.link_open(c)
        # Google search.
        elif c.lower().startswith("search"):
            self.bh.google_search(c)
        # Playing songs
        elif c.lower().startswith("play"):
            self.bh.play_YT_song_video(c)
        # Weather updates
        elif "weather update" in c.lower():
            self.wh.weather_update(c)
        # Ai integration --Groq
        else:
            try:
                speak(self.ai.AI(c))
            except:
                return "Error occurred !"
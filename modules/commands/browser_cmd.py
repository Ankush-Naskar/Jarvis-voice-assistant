import webbrowser
from modules.voice.speech import speak
from modules.data_handler.data_handling import DataHandling
from modules.services.ai_service import ArtificialIntelligence



class BrowserHandling():
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
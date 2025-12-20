import webbrowser
# from data_source import music_library, URLs
from jarvis_modules.speech import speak
from jarvis_modules.weather import get_current_weather, get_weather_by_date
from datetime import datetime, timedelta
import asyncio
import user_settings
from jarvis_modules import ai_service
from jarvis_modules.file_and_data_handling import youtube_videos, link_open


# === For opening link in browser ===
def open_links(c):
    search = " ".join(c.lower().split(" ")[1:])
    link_ = link_open(search)
    

    if link_:
        speak(f"opening {search}")
        webbrowser.open(link_)
    else:
        speak(f"{search} is not Predefined. Searching in google")
        query = search.replace(" ", "+")
        link_ = f"https://www.google.com/search?q={query}"
        webbrowser.open(link_)

# ==== For search in google ====
def google_search(c):
        search = " ".join(c.lower().split(" ")[1:])
        speak(f"Searching {search} in google")
        query = search.replace(" ", "+")
        link_ = f"https://www.google.com/search?q={query}"
        webbrowser.open(link_) 

# ==== For playing video and songs in youtube ====
def play_YT_song_video(c):
    song = " ".join(c.lower().split(" ")[1:])
    link_ = youtube_videos(song)
    if link_:
        speak(f"Playing {song}")
        webbrowser.open(link_)
    else:
        speak(f"Playing {song} from YouTube")
        query = song.replace(" ", "+")
        song_link = f"https://www.google.com/search?q={query}+site:youtube.com&btnI"
        webbrowser.open(song_link)

# ==== For getting weather report ====
def weather_update(c):
    Location = user_settings.LOCATION_FOR_WEATHER
    
    if "current" in c.lower():
        l = asyncio.run(get_current_weather())
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
        l = asyncio.run(get_current_weather())
        speak(l)

def processCommand(c):

    # Opening links.
    if c.lower().startswith("open"):
        open_links(c)
    # Google search.
    elif c.lower().startswith("search"):
        google_search(c)
    # Playing songs
    elif c.lower().startswith("play"):
        play_YT_song_video(c)
    # Weather updates
    elif "weather update" in c.lower():
        weather_update(c)
    # Ai integration --OpenAi
    else:
        try:
            speak(ai_service.AI(c))
        except:
            return "Error occurred !"
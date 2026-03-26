from gtts import gTTS
import edge_tts
import pygame
import os
import asyncio
from data_handling import DataHandling

def speak(text):
    # Check corrupted  audio.mp3
    if os.path.exists("audio.mp3"):
        os.remove("audio.mp3")
    # Load and save Edge-TTS
    async def edge_tts_audio():        
        VOICE =  DataHandling().get_settings("basic", "voice_model")
        tts = edge_tts.Communicate(text, VOICE)
        await tts.save('audio.mp3')

    # # Logic
    try:
        asyncio.run(edge_tts_audio())
    except:
        tts = gTTS(text)
        tts.save('audio.mp3')

    # Initialize mixer and pygame
    pygame.mixer.pre_init(24000, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
     # Load and play MP3
    pygame.mixer.music.load("audio.mp3") 
    pygame.mixer.music.play()
    # Keep script alive while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("audio.mp3")

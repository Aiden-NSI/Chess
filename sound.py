#Merci OpenClassroom
import os.path
import time

try:
    import pygame.mixer
    pygame.mixer.init()
    
    SUCCESS = pygame.mixer.get_init() is not None

except (ImportError, RuntimeError):
    SUCCESS = False

if SUCCESS:

    background = pygame.mixer.Sound(os.path.join("res", "sounds", "background.ogg"))

class Music:
    def __init__(self):
        self.playing = False
        
    def play(self, load):
            background.play(-1)
            self.playing = True
    
    def stop(self):
        if SUCCESS:
            background.stop()
        self.playing = False
        
    def is_playing(self):
        return self.playing

if SUCCESS:
    pygame.mixer.quit()

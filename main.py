import pygame #Used for the creation of the GUI
import os #Used for creating directories
import ctypes #For getting screen dimensions

from cls import * #All game classes

from details import PropDetails
from leaderboard import Leaderboards
from loading import LoadScreen
from maingame import MainScreen
from new import NewGame
from pause import PauseMenu


#------------------------------Main Game Loop------------------------------
clock = pygame.time.Clock()
LoadScreen(clock)

user32 = ctypes.windll.user32
screen_w = user32.GetSystemMetrics(0)
screen_h = user32.GetSystemMetrics(1)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((screen_w - 1024)/2,(screen_h - 768)/2)

screen = pygame.display.set_mode([1024,768]) #Create screen in fullscreen mode and fill white
pygame.display.set_caption('Dunfermline-opoly')
screen.fill((255,255,255))

pygame.mixer.music.load('music.mp3') #Load in and set background music to play endlessly
pygame.mixer.music.play(-1)

nextScreen = 0
mGame = None #Create blank object that will store the Game object
while nextScreen != -1: #Main Game Loop
    if nextScreen == 0: #New Game Screen
        mGame, nextScreen = NewGame(screen, clock)
    elif nextScreen == 1: #Main Game Screen
        mGame, nextScreen = MainScreen(mGame, screen, clock)
    elif nextScreen == 2: #Property Details Screen
        mGame, nextScreen = PropDetails(mGame, screen, clock)
    elif nextScreen == 3: #Leaderboards Screen
        mGame, nextScreen = Leaderboards(mGame, screen, clock)
    elif nextScreen == 4: #Pause Menu
        mGame, nextScreen = PauseMenu(mGame, screen, clock)
    
pygame.quit() #Quits the pygame module and hence the GUI

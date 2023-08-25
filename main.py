# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
import menu
from settings import *
from game import Game
from menu import Menu
import image
import mediapipe
import cv2

# Setup pygame/window --------------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 32)  # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

mainClock = pygame.time.Clock()

# Fonts ----------------------------------------------------------- #
fps_font = pygame.font.SysFont("coopbl", 22)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Music ----------------------------------------------------------- #
# file_path = os.path.join(resource_path("C:/Users/Shala/PycharmProjects/pythonProject4", "Assests/Sounds/Komiku_-_12_-_Bicycle.mp3"))
pygame.mixer.music.load(resource_path("Assests\Sounds\Komiku_-_12_-_Bicycle.mp3"))
# pygame.mixer.music.load(file_path)
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)
# Variables ------------------------------------------------------- #
state = "menu"

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)


# Functions ------------------------------------------------------ #
def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    global state
    if state == "menu":
        if menu.update() == "game":
            game.reset()  # reset the game to start a new game
            state = "game"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
    pygame.display.update()
    mainClock.tick(FPS)


# Loop ------------------------------------------------------------ #
while True:

    # Buttons ----------------------------------------------------- #
    user_events()

    # Update ------------------------------------------------------ #
    update()

    # FPS
    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255, 200, 20))
        SCREEN.blit(fps_label, (5, 5))

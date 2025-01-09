import pygame
import pygame_gui
import ctypes
from os.path import join
from platform import system

MAP_SIZE = 30
WINDOW_WIDTH, WINDOW_HEIGHT = (1200, 800)
WINDOW_TITLE = "Interative Search"
RELATIVE_PATH = join(".", "source", "interactive")
pygame.font.init()
CELL_FONT = pygame.font.Font(None, 13)
CELL_STATES = ["none", "generated", "visited"]

CELL_SIZE = WINDOW_HEIGHT/(MAP_SIZE+1)
CELL_STROKE_SIZE = 1

COLORS = {
    "bg": "#bcccdc",
    "cell_none": "#d9eafd",
    "cell_generated": "#4da1a9",
    "cell_visited": "#2e5077",
    "text_none": "black",
    "text_generated": "white",
    "text_visited": "white",
    "cell_stroke": "black"
}
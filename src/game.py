"""Game"""


import sys
import pygame
import settings


class Game:
    """Game"""
    def __init__(self) -> None:
        self.__screen = pygame.display.set_mode(settings.window_size)
        self.__clock = pygame.time.Clock()

        pygame.display.set_caption(settings.window_caption)
        pygame.display.set_icon(settings.window_icon)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit(0)

            self.__clock.tick(settings.fps)


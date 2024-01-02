"""Game"""


import sys
import pygame
import settings
import objects


class Game:
    """Game"""
    def __init__(self) -> None:
        self.__screen = pygame.display.set_mode(settings.window_size)
        self.__clock = pygame.time.Clock()

        pygame.display.set_caption(settings.window_caption)
        pygame.display.set_icon(settings.window_icon)

        self.__gun = objects.Gun(self.__screen, 100, 100)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.window_background_color)
            self.__gun.draw()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.__gun.move('top')

            if keys[pygame.K_a]:
                self.__gun.move('left')

            if keys[pygame.K_s]:
                self.__gun.move('down')

            if keys[pygame.K_d]:
                self.__gun.move('right')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit(0)

            self.__clock.tick(settings.fps)
            pygame.display.update()


"""Gun"""


import pygame
import settings


class Gun:
    """Gun"""
    def __init__(self, screen, x: int, y: int) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__speed = 4

        # Loading gun image
        self.__size = (70, 70)
        self.__image = pygame.transform.scale(pygame.image.load('images/gun.png'), self.__size)

    def move(self, where: str) -> None:
        """Move gun"""
        if where == 'top':
            if self.__y > 0:
                self.__y -= self.__speed

        elif where == 'left':
            if self.__x > 0:
                self.__x -= self.__speed

        elif where == 'down':
            if self.__y + self.__image.get_height() < settings.window_size[1]:
                self.__y += self.__speed

        elif where == 'right':
            if self.__x + self.__image.get_width() < settings.window_size[0]:
                self.__x += self.__speed

    def draw(self) -> None:
        """Draw gun on the screen"""
        self.__screen.blit(self.__image, (self.__x, self.__y))


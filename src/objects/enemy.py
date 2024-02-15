"""Enemy"""


import os
import pygame


class Enemy:
    """Enemy"""
    def __init__(self, screen, x: int, y: int) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__speed = 3
        self.__size = (70, 70)

        # Enemy image
        self.__image = pygame.transform.scale(
            pygame.image.load(os.path.join('images',
                                           'enemy.png')),
            self.__size)

    @property
    def image_rect(self) -> pygame.rect.Rect:
        """Get enemy image rect"""
        return self.__image.get_rect(topleft=(self.__x, self.__y))

    def update(self) -> None:
        """Update enemy"""
        self.__y += self.__speed

    def draw(self) -> None:
        """Draw enemy"""
        self.__screen.blit(self.__image, (self.__x, self.__y))

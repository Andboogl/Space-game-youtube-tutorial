"""Bullet"""


import pygame


class Bullet:
    """Bullet"""
    def __init__(self, screen, gun) -> None:
        self.__screen = screen
        self.__y = gun.y - 2
        self.__color = (5, 255, 5)
        self.__size = (3, 50)
        self.__speed = 6
        self.__x = gun.x + gun.image.get_width() / 2 + self.__size[0] / 2

        # Bullet image
        self.__image = pygame.draw.line(self.__screen,
                                        self.__color,
                                        (self.__x, self.__y),
                                        (self.__x, self.__y - self.__size[1]),
                                        self.__size[0])

    @property
    def image(self) -> pygame.rect.Rect:
        """Get bullet image"""
        return self.__image

    @property
    def y(self) -> int:
        """Get bullet position on y"""
        return self.__y

    def update(self) -> None:
        """Update bullet"""
        self.__y -= self.__speed

        # Bullet image updating
        self.__image = pygame.draw.line(self.__screen,
                                        self.__color,
                                        (self.__x, self.__y),
                                        (self.__x, self.__y - self.__size[1]),
                                        self.__size[0])

    def draw(self) -> None:
        """Draw bullet"""
        pygame.draw.line(self.__screen,
                                        self.__color,
                                        (self.__x, self.__y),
                                        (self.__x, self.__y - self.__size[1]),
                                        self.__size[0])

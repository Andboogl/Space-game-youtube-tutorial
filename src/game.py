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

        # Game objects
        self.__gun = objects.Gun(self.__screen, 100, 100)
        self.__bullets = []

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.window_background_color)
            self.__gun.draw()

            # Gun moving
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.__gun.move('top')

            if keys[pygame.K_a]:
                self.__gun.move('left')

            if keys[pygame.K_s]:
                self.__gun.move('down')

            if keys[pygame.K_d]:
                self.__gun.move('right')

            # Bullets drawing
            for bullet in self.__bullets:
                bullet.draw()
                bullet.update()

                if bullet.y <= 0:
                    self.__bullets.remove(bullet)
                    print(self.__bullets)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = objects.Bullet(self.__screen, self.__gun)
                        self.__bullets.append(bullet)

            self.__clock.tick(settings.fps)
            pygame.display.update()


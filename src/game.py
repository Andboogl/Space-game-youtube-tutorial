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
        self.__gun = objects.Gun(self.__screen, 100, 700)
        self.__bullets = []
        self.__enemies = [objects.Enemy(self.__screen, 100, 50)]

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

            # Enemies drawing
            for enemy in self.__enemies:
                enemy.draw()
                enemy.update()

                if self.__gun.image.get_rect(
                    topleft=(self.__gun.x,
                             self.__gun.y)).colliderect(enemy.image_rect):
                    self.__init__()

            # Bullets drawing
            for bullet in self.__bullets:
                bullet.draw()
                bullet.update()

                if bullet.y <= 0:
                    self.__bullets.remove(bullet)

                for enemy in self.__enemies:
                    if bullet.image.colliderect(enemy.image_rect):
                        self.__bullets.remove(bullet)
                        self.__enemies.remove(enemy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = objects.Bullet(self.__screen, self.__gun)
                        self.__bullets.append(bullet)

            self.__clock.tick(settings.fps)
            pygame.display.update()


"""Modulo que contiene una cámara que puede seguir al jugador."""

import pygame
from player import Player


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, target: Player, display: pygame.surface):
        """Centra la cámara en el centro del objeto target."""

        player_center = pygame.math.Vector2()  
        player_center.x = display.get_width() / 2 - target.rect.centerx
        player_center.y = display.get_height() / 2 - target.rect.centery

        for sprite in self.sprites():  # ajusta los sprites en el grupo a la posición del jugador
            sprite_offset = pygame.math.Vector2()
            sprite_offset.x = player_center.x + sprite.rect.x
            sprite_offset.y = player_center.y + sprite.rect.y

            display.blit(sprite.image, sprite_offset)

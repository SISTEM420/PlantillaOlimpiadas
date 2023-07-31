"""Módulo que contiene la clase de las entidades del juego (bloques, NPCs, objetos)."""

import pygame
from globals import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image=pygame.Surface((TILESIZE, TILESIZE)), position=(0, 0)):
        super().__init__(groups)
        self.in_groups = groups
        self.image = image
        self.rect = image.get_rect(topleft=position)

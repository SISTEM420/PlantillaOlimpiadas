"""Modulo que contiene la clase de la escena."""

import pygame
from globals import *
from sprite import Entity
from player import Player
from texturedata import solo_texture_data, atlas_texture_data
from player import Player
import random
from opensimplex import OpenSimplex
from camera import Camera


class Scene():
    def __init__(self, app):
        self.app = app  # objeto de la clase Game

        # estas dos variables definen las texturas en la escena
        self.solo_textures = self.gen_solo_textures()
        self.atlas_textures = self.gen_atlas_textures("res/spritesheet.png")

        # instancian la cámara
        self.sprites = Camera()
        self.blocks = pygame.sprite.Group()


    def gen_solo_textures(self) -> dict:
        """Genera las texturas individuales (personajes, NPC, objetos, etc)."""

        textures = {}

        for name, data in solo_texture_data.items():
            textures[name] = pygame.transform.scale(pygame.image.load(
                data["file_path"]).convert_alpha(), (data["size"]))

        return textures

 
    def gen_atlas_textures(self, filepath) -> dict:
        """Genera las texturas de una spritesheet."""

        textures = {}
        atlas_img = pygame.transform.scale(pygame.image.load(
            filepath).convert_alpha(), (TILESIZE*2, TILESIZE*2))

        for name, data in atlas_texture_data.items():
            textures[name] = pygame.Surface.subsurface(
                atlas_img, pygame.Rect(data["position"][0] * TILESIZE, data["position"][1] * TILESIZE, data["size"][0], data["size"][1]))
        return textures

    def update(self):
        """Actualiza los sprites."""

        self.sprites.update()

    def draw(self):
        """Se encarga del renderizado."""
        
        self.app.screen.fill("white")
        self.sprites.draw(self.player, self.app.screen)

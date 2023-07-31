"""Módulo que contiene la clase que genera el jugador."""

import pygame
from globals import *
from events import EventHandler
from sprite import Entity


class Player(pygame.sprite.Sprite):
    def __init__(self, groups: pygame.Group, image: pygame.Surface, position: tuple, parameters: dict):
        super().__init__(groups)
        self.image = image

        self.rect = self.image.get_rect(topleft=position)

        self.velocity = pygame.math.Vector2(0, 0)
        self.mass = 5
        self.terminal_velocity = self.mass * TERMINALVELOCITY

        self.grounded = False  # define si el jugador está en el suelo

        # parámetros específicos del jugador, grupo de bloques y texturas
        self.block_group = parameters["block_group"]
        self.textures = parameters["textures"]

    
    def input(self):
        """Maneja el input del jugador y controla su velocidad."""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity.x = -1
        if keys[pygame.K_d]:
            self.velocity.x = 1
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity.x = 0

        # salto
        if self.grounded and EventHandler.keydown(pygame.K_w):
            self.velocity.y = -PLAYERJUMPPOWER

 
    def move(self):
        """Ejecuta el movimiento."""

        self.velocity.y += GRAVITY * self.mass
        if self.velocity.y > self.terminal_velocity:
            self.velocity.y = self.terminal_velocity

        self.rect.x += self.velocity.x * PLAYERSPEED
        self.check_collision("horizontal")
        self.rect.y += self.velocity.y
        self.check_collision("vertical")


    def check_collision(self, direction):
        """Detecta las colisiones entre el jugador y otros elementos en la escena."""

        if direction == "horizontal":
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.x > 0:  # Moviendo a la derecha
                        self.rect.right = block.rect.left
                    if self.velocity.x < 0:  # Moviendo a la izquierda
                        self.rect.left = block.rect.right

        elif direction == "vertical":
            collisions = 0
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.y > 0:  # Moviendo abajo
                        collisions += 1
                        self.rect.bottom = block.rect.top
                    if self.velocity.y < 0:  # Moviendo arriba
                        self.rect.top = block.rect.bottom

            if collisions > 0:  # en las colisiones y se detecta si estás sobre el suelo
                self.grounded = True
            else:
                self.grounded = False


    def get_adjusted_mouse(self) -> tuple:
        """Metodo para alinear el cursor con el jugador."""

        mouse_pos = pygame.mouse.get_pos()

        player_offset = pygame.math.Vector2()
        player_offset.x = SCREENWIDTH / 2 - self.rect.centerx
        player_offset.y = SCREENHEIGHT / 2 - self.rect.centery

        return (mouse_pos[0] - player_offset.x, mouse_pos[1] - player_offset.y)


    def get_block_pos(self, mouse_pos: tuple) -> tuple:
        """Devuelve el tile de la cuadrícula donde se encuentra la posición del mouse."""

        return (int((mouse_pos[0]//TILESIZE)*TILESIZE), int((mouse_pos[1]//TILESIZE)*TILESIZE))

    
    # def block_handling(self):
    #     placed = False
    #     collision = False
    #     mouse_pos = self.get_adjusted_mouse()

    #     if EventHandler.clicked_any():
    #         for block in self.block_group:
    #             if block.rect.collidepoint(mouse_pos):
    #                 collision = True
    #                 if EventHandler.clicked(1):
    #                     block.kill()
    #             if EventHandler.clicked(3):
    #                 if not collision:
    #                     placed = True
    #     if placed and not collision:
    #         Entity(block.in_groups,
    #                self.textures["cobblestone"], self.get_block_pos(mouse_pos))

   
    def update(self):
        """Actualiza el comportamiento del jugador."""
        
        self.input()
        self.move()
        # self.block_handling()

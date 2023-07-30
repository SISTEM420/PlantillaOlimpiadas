import pygame
import sys
from globals import *
from scene import Scene
from events import EventHandler


class Game():
    # Constructor
    def __init__(self):
        pygame.init()
        # Definimos el tamaño de la pantalla
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()  # Creamos un reloj para los fps
        self.scene = Scene(self)

        self.running = True  # Esta variable define si el programa esta andando actualmente

    # Metodo que define que el programa se ejecute
    def run(self):
        while (self.running):
            self.update()
            self.draw()
        self.close()

    # Metodo que actualiza el programa cada frame
    def update(self):
        EventHandler.poll_events()
        for event in EventHandler.events:
            if event.type == pygame.QUIT:
                self.running = False

        self.scene.update()

        pygame.display.update()
        self.clock.tick(FPS)
    # Metodo que dibuja en pantalla

    def draw(self):
        self.scene.draw()

    # Metodo que finaliza el programa
    def close(self):
        pygame.quit()
        sys.exit()


# Iniciar el programa
if __name__ == "__main__":
    game = Game()
    game.run()

import pygame
import sys
from globals import *
from scene import Scene
from events import EventHandler


class Game():
    """Clase del juego."""

    def __init__(self):  # constructor
        pygame.init()
        # definimos el tamaño de la pantalla
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()  # creamos un reloj para los fps
        self.scene = Scene(self)

        self.running = True  # esta variable define si el programa esta andando actualmente


    def run(self):
        """Inicia el mainloop del juego."""
        while (self.running):
            self.update()
            self.draw()
        self.close()

   
    def update(self):
        """Código que se ejecuta en cada frame."""
        EventHandler.poll_events()
        for event in EventHandler.events:
            if event.type == pygame.QUIT:
                self.running = False

        self.scene.update()

        pygame.display.update()
        self.clock.tick(FPS)


    def draw(self):
        """Método que dibuja en pantalla."""
        self.scene.draw()

 
    def close(self):
        """Finaliza el programa."""
        pygame.quit()
        sys.exit()


# Iniciar el programa
if __name__ == "__main__":
    game = Game()
    game.run()

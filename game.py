import pygame
from config import *


class Game:
    def __init__(self):


        self.screen = pygame.display.set_mode((anchodeventana,altodeventana))
        pygame.display.set_caption("PAC-MAN")
        #Controlamos el reloj del juego es decir la velodad
        self.clock = pygame.time.Clock()
        #Controlar el bucle del juego
        self.running = True
    def handle_events(self):
        "Manejar eventos de Pygame"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
    def updatde (self):
        pass
    def draw(self):
        self.screen.fill(Black)

        pygame.display.flip()
    def run(self):
        while self.running:
            self.handle_events()
            self.updatde()
            self.draw()
            self.clock.tick(FPS)


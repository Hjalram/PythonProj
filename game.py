import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.windowWidth = 1920/1.5
        self.windowHeight = 1080/1.5
        self.running = True
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight)) 
        self.clock = pygame.time.Clock()     #cum tastes very good
import pygame

class Object:
    def __init__(self, game, x, y, tiles):
        self.x = x
        self.y = y

        self.tiles = tiles

        self.textureWidth = 64 * 3
        self.textureHeight = 16 * 3

        self.width = self.textureWidth * self.tiles # for the hitbox
        self.height = self.textureHeight
        self.game = game

    def draw(self):
        for i in range(0, self.tiles):
            grass = pygame.transform.scale(pygame.image.load("C:/coding/vscode/codededeing/textures/grass_ground.png"), (self.textureWidth, self.textureHeight))

            self.game.window.blit(grass, (self.x + (i * self.textureWidth), self.y))
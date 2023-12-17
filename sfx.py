import pygame, random

class Particle:
    def __init__(self, game, pos):
        self.x, self.y = pos
        self.vx, self.vy = random.randint(-2, 2), random.randint(-50, -10) * 0.1
        self.rad = 5
        self.game = game

    def draw(self):
        pygame.draw.circle(self.game.window, (139, 69, 19), (int(self.x), int(self.y) + 40), self.rad)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if random.randint(0, 60) < 60:
            self.rad -= 1

class Dust:
    def __init__(self, game, pos):
        self.pos = pos
        self.game = game
        self.Particles = [Particle(self.game, pos) for _ in range(50)]

    def draw(self):
        for i in self.Particles:
            i.draw()

    def update(self):
        for i in self.Particles:
            i.update()
            if i.rad <= 0:
                self.Particles.remove(i)
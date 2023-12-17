import pygame
from sfx import Dust

class Player:
    def __init__(self, game): 
        self.x = 200
        self.y = 100
        self.width = 40
        self.height = 40
        self.xVel = 0
        self.yVel = 0 
        self.gravity = 1
        self.left = False
        self.right = False
        self.up = False
        self.maxSpeed = 20
        self.grounded = False
        self.game = game
        self.flipped = False
    
    def draw(self):
        self.character_image = pygame.transform.scale(pygame.image.load("assets/Character.png"), (40, 40))

        if self.xVel > 0:
            self.character_image = pygame.transform.flip(self.character_image, False, False)
            self.flipped = False
        if self.xVel < 0:
            self.character_image = pygame.transform.flip(self.character_image, True, False)
            self.flipped = True
        
        if self.xVel == 0:
            if self.flipped == True:
                self.character_image = pygame.transform.flip(self.character_image, True, False)
            else:
                self.character_image = pygame.transform.flip(self.character_image, False, False)

        self.game.window.blit(self.character_image, (self.x, self.y))

    def collision(self, obj):  # pass in static object 
        if (
            self.x + self.width > obj.x
            and self.x < obj.x + obj.width
            and self.y + self.height > obj.y
            and self.y < obj.y + obj.height
        ):  # collision self.x
            self.grounded = True
                            
            if self.xVel > self.maxSpeed:  # max speed cap
                self.xVel = self.maxSpeed
            if self.xVel < -self.maxSpeed:
                self.xVel = -self.maxSpeed
            
            self.y = obj.y - (self.height - 1)
            self.yVel = 0

            if self.up == True:
                self.grounded = False
                self.yVel = -14

                if self.xVel > 0:
                    self.xVel += 4.3
                if self.xVel < 0: 
                    self.xVel -= 4.3
        else:
            self.grounded = False

    def keybinds(self, event):  # for player movement
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                self.left = True
            if event.key == ord('d'):
                self.right = True
            if event.key == pygame.K_SPACE:
                self.up = True
            if event.key == ord('r'):
                self.x = 0
                self.y = 300
                self.xVel = 0
                self.yVel = 0

        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                self.left = False
            if event.key == ord('d'):
                self.right = False
            if event.key == pygame.K_SPACE:
                self.up = False

    def update(self):  # Player update loop
        self.x += self.xVel
        self.y += self.yVel

        self.yVel += self.gravity

        if self.x >= self.game.windowWidth:  # reset position when finished stage
            self.x = 0

        # movement
        if self.left == True and self.xVel >= 0:  # base jumping speed
            self.xVel = -5
        if self.right == True and self.xVel <= 0:
            self.xVel = 5

        if self.left == True:  # increase speed
            self.xVel -= 0.085
        if self.right == True:
            self.xVel += 0.085

        if self.left == False and self.right == False and self.xVel > 0:  # friction
            self.xVel -= 0.715
        if self.left == False and self.right == False and self.xVel < 0:
            self.xVel += 0.888

        if self.left == False and self.right == False:
            if self.xVel > -2 and self.xVel < 2:
                self.xVel = 0

        # Create dust when moving
        if self.xVel < 0 and self.yVel != 0:
            d = Dust(self.game, (self.x + 40, self.y))
            self.game.dust.append(d)

        if self.xVel > 0 and self.yVel != 0:
            d = Dust(self.game, (self.x, self.y))
            self.game.dust.append(d)


        self.draw()

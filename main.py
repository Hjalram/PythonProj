import pygame
from player import * 
from obj import *
from game import *

game = Game()
player = Player(game)
ground = Object(game, 0, 400, 15)

while game.running == True: #update loop
    game.window.fill((0, 0, 0))
    
    for event in pygame.event.get(): #pygame events
        if event.type == pygame.QUIT:
            game.running = False
                                       
        player.keybinds(event) #keybinds updater

    player.collision(ground)
    player.update()
    
    ground.draw()
                 
    pygame.display.flip()
    pygame.display.update()

    game.clock.tick(60)

pygame.quit()
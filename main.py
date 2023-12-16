import pygame
from player import * 
from obj import *
from game import *

game = Game()
player = Player(game)
ground = Object(game, 0, 400, 15)


 
while game.running == True: #update loop
    if game.menu == True:
        game.window.fill((100, 100, 100))


        game.hoverCheck()
        game.window.blit(game.menu_title, (game.windowWidth // 6 - 80, 100))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game.selected_option is not None:
                        if game.selected_option == 0:
                            game.menu = False  # Start slot machine
                        elif game.selected_option == 1:
                            pass  # Start Blackjack
                        elif game.selected_option == 2:
                            pass#start settings  
                        elif game.selected_option == 3:
                            game.running = False
    else:

        game.window.fill((0, 0, 0))
            
        for event in pygame.event.get(): #pygame events
            if event.type == pygame.QUIT:
                game.running = False
                                        
            player.keybinds(event) #keybinds updater

        player.collision(ground)
        player.update()

        for d in game.dust:
            d.draw()
            d.update()
        
        ground.draw()
                 
    pygame.display.flip()
    pygame.display.update()

    game.clock.tick(60)

pygame.quit()
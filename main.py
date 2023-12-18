import pygame
from player import * 
from obj import *
from game import *

game_background = pygame.transform.scale(pygame.image.load("assets/game_background.png"), (1280, 720))


game = Game()
player = Player(game)
ground = Object(game, 0, 400, 15)
platform = Object(game, 300, 300, 1)

while game.running == True: #update loop
    if game.menu == True:
        game.window.fill((100, 100, 100))
        menu_background = pygame.transform.scale(pygame.image.load("assets/menu_test.png"), (1280, 720))
        game.window.blit(menu_background, (0, 0))


        game.hoverCheck()
        game.window.blit(game.menu_title, (game.windowWidth // 6, 100))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game.selected_option is not None:
                        if game.selected_option == 0:
                            game.menu = False #start game
                        elif game.selected_option == 1:
                            pass
                        elif game.selected_option == 2:
                            pass
                        elif game.selected_option == 3:
                            game.running = False #exit game              
    else:

        game.window.fill((130, 130, 130))
        game.window.blit(game_background, (0, 0))

        for event in pygame.event.get(): #pygame events
            if event.type == pygame.QUIT:
                game.running = False
                                        
            player.keybinds(event) #keybinds updater

        player.collision(ground)
        player.collision(platform) 
        player.update()
        

        for d in game.dust:
            d.draw()
            d.update()
        
        ground.draw()
        platform.draw()
    
    fps_text = game.fps_font.render("fps: " + str(int(game.clock.get_fps())), 1, (255, 255, 255))
    target_text = game.fps_font.render("target fps: " + str(game.targetFPS), 1, (255, 255, 255))

    game.window.blit(fps_text, (10, 10))
    game.window.blit(target_text, (10, 30))
                 
    pygame.display.flip()
    pygame.display.update()

    game.clock.tick(game.targetFPS)

pygame.quit()
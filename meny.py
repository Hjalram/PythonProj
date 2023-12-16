import pygame

GOLD = (255, 215, 0)

font = pygame.font.Font("assets/pixel_font.TTF")

main_menu_title = ("CASINO")
main_menu_rect = main_menu_title = C_font.render(main_menu_title, True, GOLD)

menu_options = ["Slot Machines", "Blackjack", "Settings", "Quit"]
menu_texts = [font.render(option, True, GOLD) for option in menu_options]
menu_rects = [text.get_rect(center=(windowWidth // 2, game.windowHeight // 2 + i * 50)) for i, text in enumerate(menu_texts)]

while True:
    pygame.mixer.music.play(-1)
    game.window.blit(menu_background, (0, 0))
    game.window.blit(main_menu_title, (X // 2 - main_menu_title.get_width() // 2, 75))
    

    # Check for mouse hover over menu options
    mouse_pos = pygame.mouse.get_pos()
    for i, rect in enumerate(menu_rects):
        if rect.collidepoint(mouse_pos):
            selected_option = i
            pygame.draw.rect(game.window, BLACK, menu_rects[i])  # Highlight the selected option
        game.window.blit(menu_texts[i], menu_rects[i].topleft)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    slot_machine()  # Start slot machine
                elif selected_option == 1:
                    blackjack()  # Start Blackjack
                elif selected_option == 2:
                    settings() # start settings
                elif selected_option == 3:
                    pygame.quit()
                    quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if selected_option is not None:
                    if selected_option == 0:
                        slot_machine()  # Start slot machine
                    elif selected_option == 1:
                        blackjack()  # Start Blackjack
                    elif selected_option == 2:
                        settings() #start settings  
                    elif selected_option == 3:
                        pygame.quit()
                        quit()
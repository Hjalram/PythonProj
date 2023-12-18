import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.windowWidth = 1920/1.5
        self.windowHeight = 1080/1.5
        self.running = True
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight)) 
        self.caption = pygame.display.set_caption("Velocitiles")
        self.clock = pygame.time.Clock()
        self.dust = []
        self.menu = True
        self.font = pygame.font.Font("assets/pixel_font.TTF", 65)
        self.M_font = pygame.font.Font("assets/pixel_font.TTF", 100)
        self.fps_font = pygame.font.Font("assets/pixel_font.TTF", 15)
        self.menu_options = ["Start", "Settings", "test", "Quit"]
        self.M_menu_text = ("Velocitiles")
        self.menu_title = self.M_font.render(self.M_menu_text, True, (255, 255, 255))
        self.menu_texts = [self.font.render(option, True, (255, 255, 255)) for option in self.menu_options]
        self.menu_rects = [text.get_rect(center=(self.windowWidth // 2, self.windowHeight // 2 + i * 85)) for i, text in enumerate(self.menu_texts)]
        self.targetFPS = 60
        self.selected_option = None
        

    def hoverCheck(self):
        # Check for mouse hover over menu options
        mouse_pos = pygame.mouse.get_pos()
        for i, rect in enumerate(self.menu_rects):
            if rect.collidepoint(mouse_pos):
                self.selected_option = i
                pygame.draw.rect(self.window, (0, 0, 0), self.menu_rects[i])  # Highlight the selected option
            self.window.blit(self.menu_texts[i], self.menu_rects[i].topleft)
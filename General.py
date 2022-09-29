import pygame
from sys import exit
from Level_Map import *  # import everything in settings (*)
from level import Level


class GameState:  # GameState() ?
    def __init__(self):
        self.state = "cutscene"  # Variable

    # def menu(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             exit()

    def cutscene(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "main_game"

        screen.blit(cutscene_surf, (0, 0))
        screen.blit(opening_text_surf, opening_text_rect)
        screen.blit(game_title, game_title_rect)

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(background_surf_1, (0, 0))
        screen.blit(background_surf_2, (0, 0))
        screen.blit(background_surf_3, (0, 0))
        level.run()
        # return "sus": Daniel did this

    def state_manager(self):
        if self.state == "cutscene":
            self.cutscene()
        if self.state == "main_game":
            self.main_game()
        # if self.state == "menu":
        #     self.menu()
            # print(self.main_game()): Daniel did this


# General Setup
pygame.init()
game_state = GameState()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")
frames = pygame.time.Clock()
lemon_font = pygame.font.Font("lemonmilk-regular.otf", 55)
level = Level(level_map_1, screen)

# Background
background_surf_1 = pygame.image.load("oak_woods_v1.0/background/background_layer_1.png").convert_alpha()
background_surf_1 = pygame.transform.smoothscale(background_surf_1, (screen_width, screen_height))
background_surf_2 = pygame.image.load("oak_woods_v1.0/background/background_layer_2.png").convert_alpha()
background_surf_2 = pygame.transform.smoothscale(background_surf_2, (screen_width, screen_height))
background_surf_3 = pygame.image.load("oak_woods_v1.0/background/background_layer_3.png").convert_alpha()
background_surf_3 = pygame.transform.smoothscale(background_surf_3, (screen_width, screen_height))

# Cutscene
cutscene_surf = pygame.image.load("Truck-kun.jpg").convert()
cutscene_surf = pygame.transform.smoothscale(cutscene_surf, (screen_width, screen_height))

# Opening Text
opening_text_surf = lemon_font.render("Press Space...", True, "red")
opening_text_rect = opening_text_surf.get_rect(center=(screen_width / 2, 270))

game_title = lemon_font.render("Don't Stop Movin'", True, "black")
game_title_rect = game_title.get_rect(center=(screen_width / 2, 200))

while True:
    game_state.state_manager()
    pygame.display.update()
    frames.tick(60)

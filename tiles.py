import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):  # To tell position and size each tile
        super().__init__()

        # Draws the tiles and what they look like
        self.image = pygame.Surface((size, size))
        self.image = pygame.image.load("Tile.png").convert_alpha()
        self.final = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.final.get_rect(topleft=pos)

    def update(self, x_shift):  # how much shift screen left or right based on value given
        self.rect.x += x_shift  # when we call the function, the value in the brackets will = x_shift since self doesn't

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image = pygame.image.load("Character.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.rect = self.rect.inflate(-12.5, -7.5)

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3.5
        self.gravity = 0.8
        self.jump_speed = -15

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.direction.y == 0:
            self.jump()

    def apply_gravity(self):
        if self.direction.y < 30:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y
        else:
            self.direction.y = self.direction.y - 5

    def death(self):
        if self.rect.y > 704:
            self.rect.y = 0

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.death()

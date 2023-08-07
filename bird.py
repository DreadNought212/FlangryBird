import pygame

bird_image = pygame.image.load('bird.png')


class Bird(pygame.sprite.Sprite):
    def __init__(self, y, x, rotation_degree):
        pygame.sprite.Sprite.__init__(self)
        self.rotation_degree = rotation_degree
        self.bird_x = x
        self.bird_y = y
        self.bird_rect = pygame.transform.scale(bird_image, (40, 40))
        self.bird_rect1 = pygame.Rect((self.bird_x, self.bird_y, 40, 40))
        self.bird_rect = pygame.transform.rotate(self.bird_rect, self.rotation_degree)


    def draw_bird(self, win):
        win.blit(self.bird_rect, (self.bird_x, self.bird_y))
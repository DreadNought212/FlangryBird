import pygame
import random

pipe_spacing = 120

pipe_down_image = pygame.image.load('pipe_down.png')
pipe_down_rect = pygame.transform.scale(pipe_down_image, (100, 400))
pipe_down_rect.set_colorkey((255, 255, 255))

pipe_up_image = pygame.image.load('pipe_up.png')
pipe_up_rect = pygame.transform.scale(pipe_up_image, (100, 400))
pipe_up_rect.set_colorkey((255, 255, 255))

class Pipes(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.pipe_up_y = random.randint(-350, -150)
        self.pipe_down_y = self.pipe_up_y + 400 + pipe_spacing
        self.pipe_x = x
        self.pipe_up_rect = pygame.transform.scale(pipe_up_image, (100, 400))
        self.pipe_down_rect = pygame.transform.scale(pipe_down_image, (100, 400))
        self.pipe_up_rect1 = pygame.Rect((self.pipe_x, self.pipe_up_y, 100, 400))
        self.pipe_down_rect1 = pygame.Rect((self.pipe_x, self.pipe_down_y, 100, 400))

    def draw_pipes(self, win):
        win.blit(pipe_up_rect, (self.pipe_x, self.pipe_up_y))
        win.blit(pipe_down_rect, (self.pipe_x, self.pipe_down_y))
        self.pipe_up_rect1 = pygame.Rect((self.pipe_x, self.pipe_up_y, 100, 400))
        self.pipe_down_rect1 = pygame.Rect((self.pipe_x, self.pipe_down_y, 100, 400))

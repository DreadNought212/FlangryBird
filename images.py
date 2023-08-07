import pygame
game_over_surface_opacity = 0

bg_image = pygame.image.load('bg.png')
bg_rect = pygame.transform.scale(bg_image, (600, 560))

start_button_image = pygame.image.load('start_button.png')
start_button_rect = pygame.transform.scale(start_button_image, (150, 50))

start_button_image_pressed = pygame.image.load('start_button_pressed.png')
start_button_rect_pressed = pygame.transform.scale(start_button_image_pressed, (150, 50))
start_button_rect_pressed.set_colorkey((255, 255, 255))

home_button_image = pygame.image.load('home_button.png')
home_button_rect = pygame.transform.scale(home_button_image, (180, 80))

home_button_image_pressed = pygame.image.load('home_button_pressed.png')
home_button_rect_pressed = pygame.transform.scale(home_button_image_pressed, (180, 80))


footer_image = pygame.image.load('footer.png')
footer_rect = pygame.transform.scale(footer_image, (800, 200))

game_over_rect = pygame.image.load('game_over.png')
game_over_surface = pygame.Surface((400, 350))
game_over_surface.set_colorkey(0, 0)
game_over_surface.set_alpha(game_over_surface_opacity)

title_image = pygame.image.load('title_image.png')
title_rect = pygame.transform.scale(title_image, (400, 260))

title_bird_image = pygame.image.load('angry_bird.png')
title_bird_rect = pygame.transform.scale(title_bird_image, (120, 120))
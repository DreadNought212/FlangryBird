import pygame
from images import *
from pipes import *
from bird import *

pygame.init()

WIN_WIDTH = 400
WIN_HEIGHT = 600
blackout_opacity = 0
op = 25

blackout = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
blackout.fill((0, 0, 0))
blackout.set_alpha(blackout_opacity)

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

x_bird = 150

rotation_degree = 0

op = 0

run = False

y_bird = 300
footer_x = 0

pipes = []

def game_over(pipes_list):
    global x_bird
    global y_bird
    global game_over_surface_opacity
    global home_button_rect
    x_bird = 150
    gravity = -10
    game_over_surface_opacity = 0
    blackout_opacity = 0
    op = 0
    print(1)
    while True:
        print(game_over_surface_opacity)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    home_button_rect = home_button_rect_pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    home_button_rect = pygame.transform.scale(home_button_image, (180, 80))
                    op = 25
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 110 and pos[0] <= 290 and pos[1] >=280 and pos[1] < 360:
                        home_button_rect = home_button_rect_pressed
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if pos[0] >= 110 and pos[0] <= 290 and pos[1] >= 280 and pos[1] < 360:
                        home_button_rect = pygame.transform.scale(home_button_image, (180, 80))
                        op = 25

        if blackout_opacity == 250:
            menu(250)

        blackout_opacity += op
        game_over_fonr_score = pygame.font.Font(None, 40)
        game_over_text_score = game_over_fonr_score.render('score: ' + str(score), 1, (180, 0, 0))

        window.blit(bg_rect, (-80, 0))

        for el_pipe in pipes_list:
            el_pipe.draw_pipes(window)

        window.blit(footer_rect, (footer_x, 450))
        if x_bird >= 80:
            x_bird -= 3
        Bird(y_bird, x_bird, rotation_degree).draw_bird(window)


        y_bird += gravity
        if y_bird >= 412:
            gravity = 0
            y_bird = 412
        else:
            gravity += 1
        if game_over_surface_opacity == 255:
            window.blit(game_over_text_score, (150, 250))
            window.blit(home_button_rect, (110, 280))
        window.blit(game_over_surface, (10, 20))
        if game_over_surface_opacity < 255:
            game_over_surface_opacity += 5
        game_over_surface.blit(game_over_rect, (0, 0))
        game_over_surface.set_alpha(game_over_surface_opacity)
        blackout.set_alpha(blackout_opacity)
        window.blit(blackout, (0, 0))
        pygame.display.update()
        clock.tick(60)

def enter():
    global gravity
    x_bird = 150
    rotation_degree = 0
    y_bird = 300
    font_enter_text = 20
    x_enter_text = 120
    blackout_opacity = 250
    op = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gravity = -6
                    main()
        score_font = pygame.font.Font(None, font_enter_text)
        enter_text = score_font.render('Press SPACE to start', 1, (180, 0, 0))
        if font_enter_text == 20:
            l = 1
            k = -3
        elif font_enter_text == 45:
            l = -1
            k = 3
        if blackout_opacity != 0:
            op = - 25
        else:
            op = 0
        font_enter_text += l
        x_enter_text += k
        blackout_opacity += op
        window.blit(bg_rect, (-80, 0))
        window.blit(footer_rect, (footer_x, 450))
        Bird(y_bird, x_bird, rotation_degree).draw_bird(window)
        window.blit(enter_text, (x_enter_text, 200))
        blackout.set_alpha(blackout_opacity)
        window.blit(blackout, (0, 0))

        pygame.display.update()
        clock.tick(30)

def menu(blackout_opacity):
    global footer_x
    global start_button_rect
    global game_over_surface_opacity
    game_over_surface_opacity = 0
    game_over_surface.set_alpha(game_over_surface_opacity)
    pipes.clear()
    title_y = 0
    start = False
    op = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 125 and pos[0] <= 275 and pos[1] >=350 and pos[1] < 400:
                        start_button_rect = start_button_rect_pressed
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if pos[0] >= 125 and pos[0] <= 275 and pos[1] >= 350 and pos[1] < 400:
                        start = True
                        start_button_rect = pygame.transform.scale(start_button_image, (150, 50))
                        op = 25
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_button_rect = start_button_rect_pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    start = True
                    start_button_rect = pygame.transform.scale(start_button_image, (150, 50))
                    op = 25

        if title_y == 25:
            title_move = True
        elif title_y == 0:
            title_move = False

        if title_move:
            title_y -= 1
        else:
            title_y += 1
        blackout_opacity += op
        window.blit(bg_rect, (-80, 0))
        window.blit(footer_rect, (footer_x, 450))
        window.blit(title_rect, (0, title_y))
        window.blit(title_bird_rect, (240, title_y + 100))
        window.blit(start_button_rect, (125, 350))
        window.blit(blackout, (0, 0))
        blackout.set_alpha(blackout_opacity)
        footer_x -= 3
        if footer_x <= - 400:
            footer_x = 0
        if blackout_opacity == 250 and start == True:
            enter()
        if blackout_opacity == 250 and start == False:
            op = -25
        if blackout_opacity == 0 and start == False:
            op = 0
        if blackout_opacity > 250:
            op -= 25
        clock.tick(30)
        pygame.display.update()


def main():
    global pipes
    global score
    global footer_x
    global y_bird
    global run
    global gravity
    global rotation_degree

    rotation_degree = 0
    score_font = pygame.font.Font(None, 36)

    pipes.append(Pipes(400))

    y_bird = 300

    score = 0

    run = True

    while run:

        window.blit(bg_rect, (-80, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gravity = -6
                    if rotation_degree <= 70:
                        rotation_degree = 40

        gravity += 0.3
        for el_pipe in pipes:
            if el_pipe.pipe_up_rect1.colliderect(Bird(y_bird, 150, rotation_degree).bird_rect1) == True or el_pipe.pipe_down_rect1.colliderect(Bird(y_bird, 150, rotation_degree).bird_rect1) == True or y_bird >= 410:
                game_over(pipes)
                run = False
            if el_pipe.pipe_x == 60:
                score += 1
            if el_pipe.pipe_x == 200:
                pipes.append(Pipes(500))
            el_pipe.draw_pipes(window)
            if el_pipe.pipe_x > - 500:
                el_pipe.pipe_x -= 2.5
            else:
                pipes.pop(pipes.index(el_pipe))

        y_bird += gravity

        if rotation_degree > -90:
            rotation_degree -= 2

        score_text = score_font.render('score: ' + str(score), 1, (180, 0, 0))

        window.blit(score_text, (300, 30))

        Bird(y_bird, 150, rotation_degree).draw_bird(window)
        window.blit(footer_rect, (footer_x, 450))
        footer_x -= 3
        if footer_x <= - 400:
            footer_x = 0
        clock.tick(60)

        pygame.display.update()

menu(0)

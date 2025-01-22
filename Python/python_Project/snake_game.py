# import pygame as p
# from pygame.locals import *
# import time as t
# import random as r

# p.init()
# red = (255, 0, 0)
# blue = (51, 153, 255)
# gray = (192, 192, 192)
# snake_color = (73, 3, 252)
# green = (73, 3, 252)
# yellow = (252, 3, 28)  # Corrected yellow color

# win_width = 600
# win_height = 400
# window = p.display.set_mode((win_width, win_height))
# p.display.set_caption("Snake game")
# t.sleep(2)


# snake_size = 10
# snake_speed = 10

# clock = p.time.Clock()
# font_style = p.font.SysFont("calibri", 26)
# score_font = p.font.SysFont("comicsansms", 30)

# def user_score(score):
#     number = score_font.render(f"Score: {score} \t", True, red)
#     window.blit(number, [0, 0])

# def game_snake(snake_size, snake_length_list):
#     for x in snake_length_list:
#         p.draw.rect(window, green, [x[0], x[1], snake_size, snake_size])

# def message(msg):
#     msg = font_style.render(msg, True, red)  # Corrected from rander to render
#     window.blit(msg, [win_width / 6, win_height / 3])

# def game_loop():
#     gameover = False
#     gameclose = False
#     x1 = win_width / 2
#     y1 = win_height / 2
#     x1_change = 0
#     y1_change = 0
#     snake_length_list = []
#     snake_length = 1
#     foodx = round(r.randrange(0, win_width - snake_size) / 10.0) * 10.0
#     foody = round(r.randrange(0, win_height - snake_size) / 10.0) * 10.0

#     while not gameover:
#         while gameclose:
#             window.fill(gray)
#             message("You lost! Press P to play again or Q to quit.")
#             user_score(snake_length - 1)
#             p.display.update()

#             for event in p.event.get():
#                 if event.type == p.KEYDOWN:
#                     if event.key == p.K_q:
#                         gameover = True
#                         gameclose = False
#                     if event.key == p.K_p:
#                         game_loop()

#         for event in p.event.get():
#             if event.type == p.KEYDOWN:
#                 if event.key == K_LEFT:
#                     x1_change = -snake_size
#                     y1_change = 0
#                 if event.key == K_RIGHT:
#                     x1_change = snake_size
#                     y1_change = 0
#                 if event.key == K_UP:
#                     x1_change = 0
#                     y1_change = -snake_size
#                 if event.key == K_DOWN:
#                     x1_change = 0
#                     y1_change = snake_size

#         if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
#             gameclose = True

#         x1 += x1_change
#         y1 += y1_change
#         window.fill(gray)
#         p.draw.rect(window, yellow, [foodx, foody, snake_size, snake_size])
#         snake_head = [x1, y1]
#         snake_length_list.append(snake_head)

#         if len(snake_length_list) > snake_length:
#             del snake_length_list[0]

#         for block in snake_length_list[:-1]:
#             if block == snake_head:
#                 gameclose = True

#         game_snake(snake_size, snake_length_list)
#         user_score(snake_length - 1)
#         p.display.update()

#         if x1 == foodx and y1 == foody:
#             foodx = round(r.randrange(0, win_width - snake_size) / 10.0) * 10.0
#             foody = round(r.randrange(0, win_height - snake_size) / 10.0) * 10.0
#             snake_length += 1

#         clock.tick(snake_speed)

#     p.quit()
#     quit()

# game_loop()
import pygame as p
from pygame.locals import *
import time as t
import random as r

p.init()
red = (255, 0, 0)
blue = (51, 153, 255)
gray = (192, 192, 192)
snake_color = (73, 3, 252)
green = (73, 3, 252)
yellow = (252, 3, 28)  # Corrected yellow color

win_width = 600
win_height = 400
window = p.display.set_mode((win_width, win_height))
p.display.set_caption("Snake game")
t.sleep(2)

snake_size = 10

clock = p.time.Clock()
font_style = p.font.SysFont("calibri", 26)
score_font = p.font.SysFont("comicsansms", 30)

def user_score(score):
    number = score_font.render(f"Score: {score} \t", True, red)
    window.blit(number, [0, 0])

def display_speed(speed):
    speed_text = score_font.render(f"Speed: {speed}", True, red)
    window.blit(speed_text, [win_width - 150, 0])

def game_snake(snake_size, snake_length_list):
    for x in snake_length_list:
        p.draw.rect(window, green, [x[0], x[1], snake_size, snake_size])

def message(msg):
    msg = font_style.render(msg, True, red)  # Corrected from rander to render
    window.blit(msg, [win_width / 6, win_height / 3])

def get_speed():
    speed = ""
    input_active = True
    while input_active:
        window.fill(gray)
        message("Enter snake speed (1-20) and press Enter:")
        speed_text = font_style.render(speed, True, red)
        window.blit(speed_text, [win_width / 2.5, win_height / 2])
        p.display.update()

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    input_active = False
                elif event.key == p.K_BACKSPACE:
                    speed = speed[:-1]
                else:
                    speed += event.unicode
        
    return int(speed) if speed.isdigit() and 1 <= int(speed) <= 20 else 10

def game_loop():
    gameover = False
    gameclose = False
    x1 = win_width / 2
    y1 = win_height / 2
    x1_change = 0
    y1_change = 0
    snake_length_list = []
    snake_length = 1
    foodx = round(r.randrange(0, win_width - snake_size) / 10.0) * 10.0
    foody = round(r.randrange(0, win_height - snake_size) / 10.0) * 10.0

    snake_speed = get_speed()  # Get user input for snake speed

    while not gameover:
        while gameclose:
            window.fill(gray)
            message("You lost! Press P to play again or Q to quit.")
            user_score(snake_length - 1)
            p.display.update()

            for event in p.event.get():
                if event.type == p.KEYDOWN:
                    if event.key == p.K_q:
                        gameover = True
                        gameclose = False
                    if event.key == p.K_p:
                        game_loop()

        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameclose = True

        x1 += x1_change
        y1 += y1_change
        window.fill(gray)
        p.draw.rect(window, yellow, [foodx, foody, snake_size, snake_size])
        snake_head = [x1, y1]
        snake_length_list.append(snake_head)

        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        for block in snake_length_list[:-1]:
            if block == snake_head:
                gameclose = True

        game_snake(snake_size, snake_length_list)
        user_score(snake_length - 1)
        display_speed(snake_speed)  # Display the current snake speed
        p.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(r.randrange(0, win_width - snake_size) / 10.0) * 10.0
            foody = round(r.randrange(0, win_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    p.quit()
    quit()

game_loop()

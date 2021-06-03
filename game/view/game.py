import sys
# import game_over
from control.constants import *
# from game_over import *
import time
from random import *
import pygame
from pygame.locals import *


pygame.init()
x_snake_position = [0]
y_snake_position = [0]
window = pygame.display.set_mode(SIZE)
window_rect = window.get_rect()
pygame.display.set_caption("Snake Fire")
cover = pygame.Surface(window.get_size())
cover = cover.convert()

pygame.display.flip()


head_up = pygame.image.load("../assets/arthur_santos_head_snake_up.png").convert_alpha()  # The head
head_up = pygame.transform.scale(head_up, (30, 30))
head_left = pygame.image.load("../assets/arthur_santos_head_snake_left.png").convert_alpha()
head_left = pygame.transform.scale(head_left, (30, 30))
head_down = pygame.image.load("../assets/arthur_santos_head_snake_down.png").convert_alpha()
head_down = pygame.transform.scale(head_down, (30, 30))
head_right = pygame.image.load("../assets/arthur_santos_head_snake_right.png").convert_alpha()
head_right = pygame.transform.scale(head_right, (30, 30))
body_part_1 = pygame.image.load("../assets/arthur_santos_body.png").convert_alpha()  # The body
body_part_1 = pygame.transform.scale(body_part_1, (30, 30))
fruit = pygame.image.load("../assets/arthur_santos_apple.png").convert_alpha()  # The fruit
fruit = pygame.transform.scale(fruit, (30, 30))
wall = pygame.image.load("../assets/arthur_santos_wall.png").convert_alpha()
wall = pygame.transform.scale(wall, (25, 50))


"""Stores the head and fruit's coordinates in variables"""
position_1 = head_down.get_rect()
position_fruit = fruit.get_rect()

position_1.x = 250
position_1.y = 250

"""Stores the variables in the list variables created before"""
x_snake_position[0] = position_1.x
y_snake_position[0] = position_1.y


"""Gives random coordinates to the first fruit of the game"""
position_fruit.x = randint(2, 10) * STEP
position_fruit.y = randint(2, 10) * STEP


for i in range(0, 1000):
    x_snake_position.append(-100)
    y_snake_position.append(-100)


def collision(x_coordinates_1, y_coordinates_1, x_coordinates_2, y_coordinates_2, size_snake, size_fruit):
    if ((x_coordinates_1 + size_snake >= x_coordinates_2) or (x_coordinates_1 >= x_coordinates_2))\
            and x_coordinates_1 <= x_coordinates_2 + size_fruit:
        if ((y_coordinates_1 >= y_coordinates_2) or (
                y_coordinates_1 + size_snake >= y_coordinates_2)) and y_coordinates_1 <= y_coordinates_2 + size_fruit:
            return True
        return False


"""Score Text"""


def text_score(score_temp):
    font = pygame.font.SysFont("Arial", 20)
    text = font.render("Score: " + str(score_temp), True, (0, 0, 0))
    window.blit(text, (500, 0))


def main():
    playing = True
    score_temp = 0
    snake = SNAKE
    move_up = MOVE_UP
    move_down = MOVE_DOWN
    move_right = MOVE_RIGHT
    move_left = MOVE_LEFT
    move_init = MOVE_INIT
    while playing:
        for event in pygame.event.get():
            if event.type == QUIT or \
                    (event.type == KEYDOWN and event.key == K_ESCAPE):
                playing = False
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if move_up is False and move_init is True:
                        if move_down is True:
                            move_up = False
                        else:
                            move_down = move_right = move_left = False
                            move_up = move_init = True
                if event.key == K_DOWN:
                    if move_down is False:
                        if move_up is True:
                            move_down = False
                        else:
                            move_right = move_left = move_up = False
                            move_down = move_init = True
                if event.key == K_RIGHT:
                    if move_right is False:
                        if move_left is True:
                            move_right = False
                        else:
                            move_left = move_up = move_down = False
                            move_right = move_init = True
                if event.key == K_LEFT:
                    if move_left is False:
                        if move_right is True:
                            move_left = False
                        else:
                            move_right = move_down = move_up = False
                            move_left = move_init = True

        window.fill((144, 238, 144))
        window.blit(head_down, (250, 250))

        for i in range(snake - 1, 0, -1):
            x_snake_position[i] = x_snake_position[(i - 1)]
            y_snake_position[i] = y_snake_position[(i - 1)]

        cover.fill((144, 238, 144))

        for i in range(1, snake):
            cover.blit(body_part_1, (x_snake_position[i], y_snake_position[i]))

        if move_up:
            y_snake_position[0] = y_snake_position[0] - STEP
            window.blit(cover, (0, 0))
            window.blit(head_up, (x_snake_position[0], y_snake_position[0]))

        if move_down:
            y_snake_position[0] = y_snake_position[0] + STEP
            window.blit(cover, (0, 0))
            window.blit(head_down, (x_snake_position[0], y_snake_position[0]))

        if move_right:
            x_snake_position[0] = x_snake_position[0] + STEP
            window.blit(cover, (0, 0))
            window.blit(head_right, (x_snake_position[0], y_snake_position[0]))

        if move_left:
            x_snake_position[0] = x_snake_position[0] - STEP
            window.blit(cover, (0, 0))
            window.blit(head_left, (x_snake_position[0], y_snake_position[0]))

        if x_snake_position[0] < window_rect.left:
            x_snake_position[0] = position_1.x
            y_snake_position[0] = position_1.y
            # game_over(score_temp)
            # set_click()

        if x_snake_position[0] + 35 > window_rect.right:
            x_snake_position[0] = position_1.x
            y_snake_position[0] = position_1.y
            # game_over(score_temp)
            # set_click()

        if y_snake_position[0] <= window_rect.top:
            x_snake_position[0] = position_1.x
            y_snake_position[0] = position_1.y
            # game_over(score_temp)
            # set_click()

        if y_snake_position[0] + 35 >= window_rect.bottom:
            x_snake_position[0] = position_1.x
            y_snake_position[0] = position_1.y
            # game_over(score_temp)
            # set_click()

        size_snake = snake

        if collision(x_snake_position[0], y_snake_position[0], x_snake_position[i],
                     y_snake_position[i], size_snake, 0) and move_init:
            x_snake_position[0] = position_1.x
            y_snake_position[0] = position_1.y
            # game_over(score_temp)
            # set_click()
        for i in range (5):
            window.blit(fruit, position_fruit)

        if collision(x_snake_position[0], y_snake_position[0], position_fruit.x, position_fruit.y, 20, 30):

            position_fruit.x = randint(1, 20) * STEP
            position_fruit.y = randint(1, 20) * STEP

            for j in range(0, snake):

                while collision(position_fruit.x, position_fruit.y, x_snake_position[j], y_snake_position[j], 30,
                                30):
                    position_fruit.x = randint(1, 20) * STEP
                    position_fruit.y = randint(1, 20) * STEP

            snake = snake + 1
            score_temp = score_temp + 1
        text_score(score_temp)
        pygame.display.flip()
        time.sleep(SPEED / 1000)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

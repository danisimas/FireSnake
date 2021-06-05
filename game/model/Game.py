# Add background image and music

import pygame
from pygame.locals import *
import time
import random
from control.constants import *
from view.game_over import *

from model.Snake import Snake
from model.Apple import Apple
from model.Ball import Ball

size = SIZE_SNAKE
main_clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Fire")
        pygame.mixer.init()
        # self.play_background_music()

        self.surface = pygame.display.set_mode(SIZE)
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.ball = Ball(self.surface)
        self.ball.draw()

    '''def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)
        # pygame.mixer.music.stop()
'''
    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.ball = Ball(self.surface)
        self.display_score()

    def is_collision(self, x1, y1, x2, y2):
        if ((x1 + size >= x2) or (x1 >= x2)) and x1 < x2 + size:
            if ((y1 >= y2) or (y1 + size >= y2)) and y1 < y2 + size:
                return True
        return False

    def render_background(self):
        self.surface.fill((0, 0, 0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.ball.draw()
        self.display_score()
        pygame.display.update()

        # snake eating apple scenario
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.snake.score += 1
                # self.play_sound("ding")
                self.snake.increase_length()
                self.apple.move()

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                # self.play_sound('crash')
                self.show_game_over()

        if not (0 <= self.snake.x[0] <= 600 and 0 <= self.snake.y[0] <= 600):
            # self.play_sound('crash')
            self.show_game_over()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score_text = font.render("Score:" + str(self.snake.score), True, (200, 200, 200))
        self.surface.blit(score_text, (500, 10))
        pygame.display.update()

    def show_game_over(self):
        set_click()
        game_over(self.snake.score)

    def run(self):
        running = False
        while not running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.play()
            main_clock.tick(FPS)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()

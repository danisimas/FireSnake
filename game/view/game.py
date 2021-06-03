import sys

import pygame
from pygame.locals import *
from control.constants import *
import menu

pygame.init()


''''''
screen = pygame.display.set_mode(SIZE)

''''''
pygame.display.set_caption('Snake Fire')
background_color = (134, 250, 97)
screen.fill(background_color)


def main():
    while not GAME:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(text, text_rect)
        pygame.display.update()


if __name__ == '__main__':
    main()

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

font = pygame.font.SysFont('CLIQUE', 30)
text = font.render('CLIQUE', True, pygame.Color("Blue"))
text_rect = text.get_rect()


def main():
    CLICK = False
    while not GAME:
        text_rect.center = (300, 400)
        pos_x, pos_y = pygame.mouse.get_pos()

        if text_rect.collidepoint((pos_x, pos_y)):
            if CLICK:
                menu.main()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    CLICK = True

        screen.blit(text, text_rect)
        pygame.display.update()


if __name__ == '__main__':
    main()

import sys

import pygame
from control.constants import *
from pygame.locals import *
import game

pygame.init()


''''''
screen = pygame.display.set_mode(SIZE)

''''''
pygame.display.set_caption('Snake Fire')
background_color = (0, 0, 0)
screen.fill(background_color)

font = pygame.font.SysFont('CLIQUE', 30)
text = font.render('CLIQUE', True, pygame.Color("White"))
text_rect = text.get_rect()


def main():
    CLICK = False
    while not GAME:
        text_rect.center = (300, 400)
        pos_x, pos_y = pygame.mouse.get_pos()

        if text_rect.collidepoint((pos_x, pos_y)):
            if CLICK:
                game.main()

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
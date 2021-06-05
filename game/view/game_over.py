import pygame
import menu
from control.constants import *

pygame.init()
window = pygame.display.set_mode(SIZE)
window_rect = window.get_rect()
pygame.display.set_caption("Snake Fire")
score = 0
click = False


"""Game Over Function"""


def game_over(score):
    global click
    while not click:
        window.fill((0, 0, 0))
        font = pygame.font.SysFont("arial", 48)
        font_2 = pygame.font.SysFont("arial", 38)
        text_1 = 'GAME OVER'
        text_2 = "Press space to back menu"
        text_3 = 'Score:' + str(score)
        text_1 = font.render(text_1, True, (250, 250, 250))
        text_2 = font_2.render(text_2, True, (250, 250, 250))
        text_3 = font_2.render(text_3, True, (250, 250, 250))
        text_1_rect = text_1.get_rect()
        text_2_rect = text_2.get_rect()
        text_3_rect = text_3.get_rect()
        text_1_rect.center = (400, 200)
        text_2_rect.center = (400, 250)
        text_3_rect.center = (400, 350)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    menu.main()
                    click = True

        window.blit(text_1, text_1_rect)
        window.blit(text_2, text_2_rect)
        window.blit(text_3, text_3_rect)
        pygame.display.update()


def set_click():
    global click
    click = False


if __name__ == '__main__':
    game_over(score)

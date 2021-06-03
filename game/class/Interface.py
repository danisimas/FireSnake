import pygame

pygame.init()


class Interface:
    def __init__(self, image, x_position, y_position):
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect().move(x_position, y_position)
        self.x_position = x_position
        self.y_position = y_position

    def restart_position(self):
        self.rect.x, self.rect.y = self.x_position, self.y_position

    def render(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])

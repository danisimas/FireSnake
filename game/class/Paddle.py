import Interface


class Paddles(Interface):
    def __init__(self, image, x_position, y_position):
        super(Paddles, self).__init__(image, x_position, y_position)
        self.speed = 5

    def movement(self):
        if self.rect.centery + 30 < ball.rect.y:
            self.rect.y += self.speed
        elif self.rect.centery - 30 > ball.rect.y:
            self.rect.y -= self.speed

    def collides_with_walls(self):
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 420:
            self.rect.y = 420

    def update(self):
        self.movement()
        self.collides_with_walls()

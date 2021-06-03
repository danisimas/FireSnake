class Paddles:
    def __init__(self, image, x_start, y_start):
        super().__init__(image, x_start, y_start)
        self.speed = 4

    def update(self):
        self.movement()
        self.collides_with_walls()

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

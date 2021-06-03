import Interface


class Ball(Interface):
    def __init__(self, image, x_position, y_position):
        super(Ball, self).__init__(image, x_position, y_position)
        self.direction_x = 1
        self.direction_y = 1
        self.speed = 5
        self.MIN_SPEED = 5
        self.MAX_SPEED = 9

    def movement(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y

    def collision_with_wall(self):
        if self.rect.bottom > 720:
            ball.direction_y *= -1
        elif ball.rect.top <= 0:
            ball.direction_y *= -1

    def collision_with_paddles(self):
        if ball.rect.colliderect(paddles.rect) and self.direction_x < 0:
            self.MIN_SPEED = 5
            self.randomize_angle()
            self.change_angle(paddle.rect, 1)
        elif ball.rect.colliderect(paddles.rect) and self.direction_x > 0:
            self.MIN_SPEED = 5
            self.randomize_angle()
            self.change_angle(paddle.rect, 1)

    def randomize_angle(self):
        random_angle = randint(30, 40)
        angle = radians(random_angle)
        self.direction_x = cos(angle)
        self.direction_y = sin(angle)

    def change_angle(self, paddle_rect: pygame.rect.Rect, direction_x):
        if paddle_rect.top <= self.rect.bottom <= paddle_rect.top + 60:
            self.direction_y *= -1
            self.direction_x = direction_x
        elif paddle_rect.bottom >= self.rect.top >= paddle_rect.bottom - 60:
            self.direction_x *= direction_x
        elif paddle_rect.centery - 60 \
                < self.rect.centery < paddle_rect.centery + 60:
            self.direction_y = 0
            self.direction_x *= direction_x * 1.5

    def restart(self):
        self.restart()
        self.randomize_angle()
        self.direction_y = randint(-1, 1)
        self.MIN_SPEED = 5

    def update(self):
        self.movement()
        self.collision_with_wall()
        self.collision_with_paddles()

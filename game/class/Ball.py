class Ball:
    def __init__(self, image, x_start, y_start):
        super(Ball, self).__init__(image, x_start, y_start)
        self.dx = 1
        self.dy = 1
        self.speed = 5
        self.MIN_SPEED = 5
        self.MAX_SPEED = 9

    def update(self):
        self.movement()
        self.collision_with_wall()
        # Ball collision with the player 1 's paddle
        if self.rect.colliderect(player1.rect) and self.dx < 0:
            self.collision_with_paddles()
            self.change_angle(player1.rect, 1)
        # Ball collision with the player 2 's paddle
        elif ball.rect.colliderect(player2) and self.dx > 0:
            self.collision_with_paddles()
            self.change_angle(player2.rect, -1)

    def movement(self):
        # Ball movement
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

    def collision_with_paddles(self):
        self.speed = min(self.speed + 0.2, self.MAX_SPEED)
        self.randomize_angle()
        bounce_sound_effect.play()

    def collision_with_wall(self):
        # Ball collision with the wall
        if self.rect.bottom > 720:
            ball.dy *= -1
            bounce_sound_effect.play()
        elif ball.rect.top <= 0:
            ball.dy *= -1
            bounce_sound_effect.play()

    def randomize_angle(self):
        random_angle = randint(40, 50)
        angle = radians(random_angle)
        self.dx = cos(angle)
        self.dy = sin(angle)

    def change_angle(self, player_rect: pygame.rect.Rect, x_direction):
        if player_rect.top <= self.rect.bottom <= player_rect.top + 60:
            self.dy *= -1
            self.dx *= x_direction
        elif player_rect.bottom >= self.rect.top >= player_rect.bottom - 60:
            self.dx *= x_direction
        elif player_rect.centery - 60 < \
                self.rect.centery < player_rect.centery + 60:
            self.dy = 0
            self.dx *= x_direction * 1.5

    def restart_ball(self):
        self.restart_position()
        self.randomize_angle()
        self.dy = randint(-1, 1)
        self.speed = self.MIN_SPEED

import pygame
import config


class Bullet(pygame.sprite.Sprite):
    def __init__(self, sprite, player, posx, posy, spriteoffsetx, spriteoffsety, bullet_dir, direction, axisdir, joy):
        super().__init__()
        self.size = (20, 20)
        self.pos = (posx, posy)
        self.image = pygame.image.load(sprite)
        self.dir = pygame.math.Vector2()
        self.image_hor = pygame.transform.rotate(self.image, 90)
        self.rect = pygame.Rect(((posx + spriteoffsetx, posy + spriteoffsety), self.size))
        self.bullet_dir = bullet_dir
        self.player = player
        self.direction = direction
        self.joy = joy
        self.axisdir = axisdir
        self.image_cooldown = 200
        self.start = config.bullet_explosion[0]

    def update(self):
        if self.direction == "right" or self.direction == "still_right":
            self.image = self.image_hor
            self.rect.x += self.bullet_dir

        if self.direction == "left" or self.direction == "still_left":
            self.image = self.image_hor
            self.rect.x -= self.bullet_dir

        if self.direction == "up" or self.direction == "still_up":
            self.rect.y -= self.bullet_dir

        if self.direction == "down" or self.direction == "still_down":
            self.rect.y += self.bullet_dir

        if self.rect.x > config.screen_width + 100 or self.rect.x < 0:
            self.kill()

        if self.rect.y <= config.wall_upper_lim:
            self.kill()
        if self.rect.y >= config.wall_bottom_lim:
            self.kill()
        if self.rect.x <= config.wall_left_lim:
            self.kill()
        if self.rect.x >= config.wall_right_lim:
            self.kill()

import pygame
import config
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, sprite_sheet, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.size = (config.player_frame_width, config.playerspriteend[1])
        self.speed = speed
        self.dir = pygame.math.Vector2()
        self.rect = pygame.Rect(self.pos, self.size)
        self.player_sur = pygame.surface.Surface((config.player_frame_width, config.playerspriteend[1])).convert_alpha()
        self.player_sur.set_colorkey((0, 0, 0))
        self.sprite_sheet = sprite_sheet
        self.startx = startx
        self.starty = starty
        self.endx = config.playerspriteend[0]
        self.image = pygame.image.load(self.sprite_sheet).convert_alpha()
        self.image = pygame.transform.scale(self.image, [config.sprite_sheet_size[0] * config.scale,
                                                         config.sprite_sheet_size[1] * config.scale])
        self.player_sur.blit(self.image, (0, 0),
                             (self.startx, self.starty, config.playerspriteend[0], config.playerspriteend[1]))
        self.image = self.player_sur
        self.image_cooldown = 0
        self.frame = "still_right"
        self.points = 0
        self.lifes = 5

    def p_move(self, dt):
        if self.dir.magnitude() > 0:
            self.pos += self.speed * self.dir * dt
        self.rect = pygame.Rect(self.pos, self.size)

    def update_sprite(self, now, start, end):

        if self.startx < start:
            self.startx = start

        if now - self.image_cooldown >= config.player_img_cooldown:
            self.image_cooldown = now
            self.startx += config.player_frame_width
            self.image = pygame.image.load(self.sprite_sheet).convert_alpha()
            self.image = pygame.transform.scale(self.image, [config.sprite_sheet_size[0] * config.scale,
                                                             config.sprite_sheet_size[1] * config.scale])

        if self.startx >= end:
            self.startx = start
        self.player_sur.blit(self.image, (0, 0),
                             (self.startx, self.starty, config.playerspriteend[0], config.playerspriteend[1]))
        self.image = self.player_sur

    def still_player(self, startx):
        self.image = pygame.image.load(self.sprite_sheet).convert_alpha()
        self.image = pygame.transform.scale(self.image, [config.sprite_sheet_size[0] * config.scale,
                                                         config.sprite_sheet_size[1] * config.scale])
        self.player_sur.blit(self.image, (0, 0),
                             (startx, self.starty, config.playerspriteend[0], config.playerspriteend[1]))
        self.image = self.player_sur

    def sprite_check(self, now):
        if self.dir.x == 0 and self.dir.y == 0:
            if self.frame == "up":
                self.still_player(config.player_facing_up)
                self.frame = "still_up"

            if self.frame == "down":
                self.frame = "still_down"
                self.still_player(config.player_facing_down)

            if self.frame == "left":
                self.still_player(config.player_facing_left)
                self.frame = "still_left"

            if self.frame == "right":
                self.still_player(config.player_facing_right)
                self.frame = "still_right"

        if self.frame == "up":
            self.update_sprite(now, config.player_up[0], config.player_up[1])

        if self.frame == "right":
            self.update_sprite(now, config.player_right[0], config.player_right[1])

        if self.frame == "left":
            self.update_sprite(now, config.player_left[0], config.player_left[1])

        if self.frame == "down":
            self.update_sprite(now, config.player_down[0], config.player_down[1])

    def collision(self):
        if self.rect.y <= config.wall_upper_lim:
            self.pos.y = config.wall_upper_lim + 2
        if self.rect.y >= config.wall_bottom_lim:
            self.pos.y = config.wall_bottom_lim - 2
        if self.rect.x <= config.wall_left_lim:
            self.pos.x = config.wall_left_lim + 2
        if self.rect.x >= config.wall_right_lim:
            self.pos.x = config.wall_right_lim - 2

    def enemy_collision(self, player, enemygroup):
        if pygame.sprite.spritecollide(player, enemygroup, False):
            self.pos = (random.randint(10, 940), random.randint(85, 690))
            pygame.mixer.music.load(config.damage_sound)
            pygame.mixer.music.play()
            player.lifes -= 1

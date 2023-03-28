import pygame
import config


class Red_robot(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, sprite_sheet, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.size = (config.red_robot_frame_width, config.red_robotspriteend[1])
        self.speed = speed
        self.dir = pygame.math.Vector2()
        self.rect = pygame.Rect(self.pos, self.size)
        self.player_sur = pygame.surface.Surface((config.red_robot_frame_width, config.red_robotspriteend[1])).convert_alpha()
        self.player_sur.set_colorkey((0, 0, 0))
        self.sprite_sheet = sprite_sheet
        self.startx = startx
        self.starty = starty
        self.endx = config.playerspriteend[0]
        self.image = pygame.image.load(self.sprite_sheet).convert_alpha()
        self.image = pygame.transform.scale(self.image, [config.sprite_sheet_size[0] * config.scale, config.sprite_sheet_size[1] * config.scale])
        self.player_sur.blit(self.image, (0, 0),
                             (self.startx, self.starty, config.red_robotspriteend[0], config.red_robotspriteend[1]))
        self.image = self.player_sur
        self.image_cooldown = 0
        self.frame = "up"
        self.maxy = self.rect.y

    def p_move(self, player):
        if player.rect.x <= self.rect.x:
            self.rect.x += self.speed
        if player.rect.x >= self.rect.x:
            self.rect.x -= self.speed
        if player.rect.y <= self.rect.y:
            self.rect.y += self.speed
        if player.rect.y >= self.rect.y:
            self.rect.y -= self.speed

    def update_sprite(self, now, start, end):

        if self.startx < start:
            self.startx = start

        if now - self.image_cooldown >= config.red_robot_img_cooldown:
            self.image_cooldown = now
            self.startx += config.red_robot_frame_width
            self.image = pygame.image.load(self.sprite_sheet).convert_alpha()
            self.image = pygame.transform.scale(self.image, [config.sprite_sheet_size[0] * config.scale,
                                                             config.sprite_sheet_size[1] * config.scale])

        if self.startx >= end:
            self.startx = start
        self.player_sur.blit(self.image, (0, 0),
                             (self.startx, self.starty, config.red_robotspriteend[0], config.red_robotspriteend[1]))
        self.image = self.player_sur

    def sprite_check(self, now):

        if self.frame == "up":
            self.update_sprite(now, config.red_robot_up[0], config.red_robot_up[1])

        if self.frame == "down":
            self.update_sprite(now, config.red_robot_down[0], config.red_robot_down[1])

    def collision(self):
        if self.rect.y <= config.wall_upper_lim:
            self.rect.y += 7
            self.speed *= -1
            self.frame = "down"
        if self.rect.y >= config.wall_bottom_lim:
            self.rect.y -= 2
            self.speed *= -1
            self.frame = "up"
        if self.rect.x <= config.wall_left_lim:
            self.rect.x = config.wall_left_lim + 2
            self.speed *= -1
        if self.rect.x >= config.wall_right_lim:
            self.rect.x = config.wall_right_lim - 2
            self.speed *= -1



    def bullet_collide_red(self, bullet, player, group):
        if pygame.sprite.spritecollide(bullet, group, True):
            pygame.mixer.music.load(config.get_enemy)
            pygame.mixer.music.play()
            self.rect.y = config.screen_height +100
            player.points += 1500
            self.kill()
            bullet.kill()
import pygame
import config


class Displays:
    def __init__(self):
        self.colour_cont = 0
        self.colour_cont_cooldown = 0
        self.colour_cooldown = 250
        self.wall_num = 5
        self.wall_cont = 0
        self.wall_cont_cooldown = 0
        self.wall_cooldown = 250

    def scoring(self, points, font, size, pos, screen, now):
        font = pygame.font.Font(font, size)
        colour = ["white", "pink", "yellow", "orange", "purple"]

        if self.colour_cont >= len(colour) - 1:
            self.colour_cont = 0
        score1 = font.render(f"{points}", True, colour[self.colour_cont])
        screen.blit(score1, pos)
        if now - self.colour_cont_cooldown >= self.colour_cooldown:
            self.colour_cont_cooldown = now
            self.colour_cont += 1

    @staticmethod
    def lifes_display(screen, plife):
        for lifes in range(plife):
            icon_image_load = pygame.image.load(config.sprite_sheet)
            icon_image_load = pygame.transform.scale(icon_image_load,
                                                     [308 * config.icon_scale, 203 * config.icon_scale])
            icon = pygame.surface.Surface((25, 25))
            icon.blit(icon_image_load, (0, 0), (173 * config.icon_scale, 82 * config.icon_scale, 25, 25))
            screen.blit(icon, (210 + lifes * 26, 10))

    @staticmethod
    def starscreen(screen):
        startscreen = pygame.image.load(config.startscreen)
        startscreen = pygame.transform.scale(startscreen,  (config.screen_width, config.screen_height))
        screen.blit(startscreen, (0, 0))

    @staticmethod
    def walls(screen, wall):
        screen.blit(wall, (0, 0))

    def start(self, fonts, size, pos, screen, now):
        font = pygame.font.Font(fonts, size)
        fontsmall = pygame.font.Font(fonts, size - 15)

        colour = ["white", "pink", "yellow", "orange", "purple"]
        name = "ROBOTRON"

        for letters in range(len(name)):
            if self.colour_cont >= len(colour) - 1:
                self.colour_cont = 0
            score1 = font.render(f"{name[letters]}", True, colour[self.colour_cont - 1])
            text = "press R2 to start"
            press = fontsmall.render(f"{text}", True, colour[self.colour_cont])
            screen.blit(score1, (pos[0] + letters * size, pos[1]))
            screen.blit(press, (pos[0] - 60, pos[1] + size))

        if now - self.colour_cont_cooldown >= 40:
            self.colour_cont_cooldown = now
            self.colour_cont += 1

    @staticmethod
    def game_over(fonts, size, pos, screen):
        fontsmall = pygame.font.Font(fonts, size - 15)
        colour = "white"
        text = "GAME OVER"
        press = fontsmall.render(f"{text}", True, colour)
        screen.blit(press, (pos[0] + 70, pos[1] + size))

    @staticmethod
    def win(fonts, size, pos, screen):
        fontsmall = pygame.font.Font(fonts, size - 15)
        colour = "white"
        text = "YOU WIN"
        press = fontsmall.render(f"{text}", True, colour)
        screen.blit(press, (pos[0] + 70, pos[1] + size))

    def anim_walls(self, screen, wall, now):
        screen.blit(wall, (0, 0), (0, config.screen_height * self.wall_cont, config.screen_width, config.screen_height))
        if now - self.wall_cont_cooldown >= 40:
            self.wall_cont_cooldown = now
            self.wall_cont += 1

        if self.wall_cont > self.wall_num:
            self.wall_cont = 0

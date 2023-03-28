import pygame
import hulk
import bullets
import config
import controller
import player
import screens
import human
import red_robot

pygame.init()
pygame.joystick.init()
pygame.mixer.init()
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.joystick = pygame.joystick.Joystick(0)
        self.run = True
        self.screen = config.screen
        self.clock = pygame.time.Clock()
        self.hulkGroup = pygame.sprite.Group()
        self.playerGroup = pygame.sprite.Group()
        self.humanGroup = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.player = player.Player(350, 350, config.player_speed, config.player_spritesheet,
                                    config.playerspritestart[0], config.playerspritestart[1])
        self.enemyhulk = hulk.Hulk(500, 500, 2, config.player_spritesheet,
                                   config.hulkspritestart[0], config.hulkspritestart[1])
        self.enemyhulk1 = hulk.Hulk(360, 200, -config.hulk_speed, config.player_spritesheet,
                                    config.hulkspritestart[0], config.hulkspritestart[1])
        self.enemyhulk2 = hulk.Hulk(30, 130, config.hulk_speed + 1, config.player_spritesheet,
                                    config.hulkspritestart[0], config.hulkspritestart[1])
        self.enemyhulk3 = hulk.Hulk(100, 590, config.hulk_speed + 3, config.player_spritesheet,
                                    config.hulkspritestart[0], config.hulkspritestart[1])
        self.enemyhulk4 = hulk.Hulk(745, 590, -config.hulk_speed - 1, config.player_spritesheet,
                                    config.hulkspritestart[0], config.hulkspritestart[1])
        self.woman = human.Human(400, 590, config.hulk_speed, config.player_spritesheet,
                                 config.humanspritestart[0], config.humanspritestart[1])
        self.woman2 = human.Human(600, 150, -config.hulk_speed, config.player_spritesheet,
                                  config.humanspritestart[0], config.humanspritestart[1])
        self.woman3 = human.Human(60, 700, -config.hulk_speed, config.player_spritesheet,
                                  config.humanspritestart[0], config.humanspritestart[1])
        self.woman4 = human.Human(700, 400, -config.hulk_speed, config.player_spritesheet,
                                  config.humanspritestart[0], config.humanspritestart[1])
        self.red_robot = red_robot.Red_robot(800, 150, -config.red_robot_speed, config.player_spritesheet,
                                             config.red_robotspritestart[0], config.red_robotspritestart[1])
        self.red_robot1 = red_robot.Red_robot(100, 500, -config.red_robot_speed + 0.4, config.player_spritesheet,
                                              config.red_robotspritestart[0], config.red_robotspritestart[1])
        self.red_robot2 = red_robot.Red_robot(750, 750, -config.red_robot_speed + 0.3, config.player_spritesheet,
                                              config.red_robotspritestart[0], config.red_robotspritestart[1])
        self.hulkGroup.add(self.enemyhulk, self.enemyhulk1, self.enemyhulk2, self.enemyhulk3, self.enemyhulk4,
                           self.red_robot, self.red_robot1, self.red_robot2)
        self.humanGroup.add(self.woman, self.woman2, self.woman3, self.woman4)
        self.joy_axis = 0
        self.axis_value = 0
        self.player_joy = 0
        self.bullet = bullets.Bullet(config.bullet_sprite, self.player, self.player.rect.x,
                                     self.player.rect.y, 0, 0, 10, self.player.frame, self.axis_value, self.joy_axis)

        self.scoring = screens.Displays()
        self.lifedis = screens.Displays()
        self.start = False
        self.wscreen = screens.Displays()
        self.start_wall = screens.Displays()
        self.wall = pygame.image.load(config.wall_img)
        self.wall = pygame.transform.scale(self.wall, (config.screen_width, config.screen_height * 5))
        self.stage = 1

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
                exit()

            if event.type == pygame.JOYAXISMOTION:
                self.joy_axis = event.axis
                self.axis_value = event.value
                self.player_joy = event.joy
                controller.Controller.move_player(self.player, self.player_joy, self.joy_axis, self.axis_value, 0, 1, 0,
                                                  config.player_speed)

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 10 and event.joy == 0 and self.start:
                    pygame.mixer.music.load(config.bullet_sound)
                    pygame.mixer.music.play()
                    self.bullet = bullets.Bullet(config.bullet_sprite, self.player, self.player.rect.x,
                                                 self.player.rect.y, 0, 0, 10, self.player.frame, self.axis_value,
                                                 self.joy_axis)
                    self.bullet_group.add(self.bullet)

                if event.button == 10 and event.joy == 0 and not self.start:
                    pygame.mixer.music.load(config.get_human_sound)
                    pygame.mixer.music.play()
                    self.start = True

    def game1(self):

        self.dt = clock.tick() / 100
        self.now = pygame.time.get_ticks()
        self.sprite_update = pygame.time.get_ticks()
        self.cool_down = pygame.time.get_ticks()
        self.screen.fill("black")

        # bullet checks
        self.bullet_group.draw(self.screen)
        self.bullet_group.update()

        # player checks

        self.player.sprite_check(self.now)
        self.player.p_move(self.dt)
        self.player.collision()
        self.player.enemy_collision(self.player, self.hulkGroup)

        self.playerGroup.add(self.player)
        self.playerGroup.draw(self.screen)
        self.playerGroup.update()

        # screens check

        self.scoring.scoring(self.player.points, config.game_font, 30, (30, 10), self.screen, self.now)
        self.lifedis.lifes_display(self.screen, self.player.lifes)
        self.wscreen.walls(self.screen, self.wall)

        # ### enemy checks #### #

        # green robots
        self.enemyhulk.sprite_check(self.now)
        self.enemyhulk.p_move()
        self.enemyhulk.collision()
        self.enemyhulk.bullet_collide(self.bullet, self.hulkGroup)

        self.enemyhulk1.sprite_check(self.now)
        self.enemyhulk1.p_move()
        self.enemyhulk1.collision()
        self.enemyhulk1.bullet_collide(self.bullet, self.hulkGroup)

        self.enemyhulk2.sprite_check(self.now)
        self.enemyhulk2.p_move()
        self.enemyhulk2.collision()
        self.enemyhulk2.bullet_collide(self.bullet, self.hulkGroup)

        self.enemyhulk3.sprite_check(self.now)
        self.enemyhulk3.p_move()
        self.enemyhulk3.collision()
        self.enemyhulk3.bullet_collide(self.bullet, self.hulkGroup)

        self.enemyhulk4.sprite_check(self.now)
        self.enemyhulk4.p_move()
        self.enemyhulk4.collision()
        self.enemyhulk4.bullet_collide(self.bullet, self.hulkGroup)

        # red robots
        self.red_robot.sprite_check(self.now)
        self.red_robot.p_move(self.player)
        self.red_robot.collision()
        self.red_robot.bullet_collide_red(self.red_robot, self.player, self.bullet_group)

        self.red_robot1.sprite_check(self.now)
        self.red_robot1.p_move(self.player)
        self.red_robot1.collision()
        self.red_robot1.bullet_collide_red(self.red_robot1, self.player, self.bullet_group)

        self.red_robot2.sprite_check(self.now)
        self.red_robot2.p_move(self.player)
        self.red_robot2.collision()
        self.red_robot2.bullet_collide_red(self.red_robot2, self.player, self.bullet_group)

        self.hulkGroup.draw(self.screen)
        self.hulkGroup.update()

        # human checks
        self.woman.sprite_check(self.now)
        self.woman.p_move()
        self.woman.collision()
        self.woman.player_collide(self.woman, self.player, self.playerGroup)

        self.woman2.sprite_check(self.now)
        self.woman2.p_move()
        self.woman2.collision()
        self.woman2.player_collide(self.woman2, self.player, self.playerGroup)

        self.woman3.sprite_check(self.now)
        self.woman3.p_move()
        self.woman3.collision()
        self.woman3.player_collide(self.woman3, self.player, self.playerGroup)

        self.woman4.sprite_check(self.now)
        self.woman4.p_move()
        self.woman4.collision()
        self.woman4.player_collide(self.woman4, self.player, self.playerGroup)

        self.humanGroup.draw(self.screen)

        clock.tick(60)
        pygame.display.flip()

        if self.player.lifes == 0:
            pygame.mixer.music.load(config.bullet_sound)
            pygame.mixer.music.play()
            self.screen.fill("black")
            self.scoring.game_over(config.game_font, 50,
                                   (config.screen_width - config.screen_width / 2 - (50 * 9) / 2,
                                    config.screen_height - config.screen_height / 2 - 50 * 2),
                                   self.screen)
            pygame.display.flip()
            pygame.time.wait(1000)
            pygame.quit()

        if len(self.humanGroup) == 0:
            pygame.mixer.music.load(config.victory_sound)
            pygame.mixer.music.play()
            self.screen.fill("black")
            self.scoring.win(config.game_font, 50,
                             (config.screen_width - config.screen_width / 2 - (50 * 9) / 2,
                              config.screen_height - config.screen_height / 2 - 50 * 2),
                             self.screen)
            pygame.display.flip()
            pygame.time.wait(1000)
            pygame.quit()

    def run_game(self):
        while self.run:
            self.check_events()
            self.now1 = pygame.time.get_ticks()
            if not self.start:
                self.start_wall.anim_walls(self.screen, self.wall, self.now1)
                self.scoring.start(config.game_font, 50, (config.screen_width - config.screen_width / 2 - (50 * 9) / 2,
                                                          config.screen_height - config.screen_height / 2 - 50 * 2),
                                   self.screen, self.now1)

                pygame.display.flip()
            if self.start:
                if self.stage == 1:
                    self.game1()

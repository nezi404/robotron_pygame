import random
import pygame
import config
import game


class Controller:

    def __init__(self):
        super().__init__()

    def move_player(self, player_control, coor_axis, valoreve, axisnumx, axisnumy, joynum, speed):
        if player_control == joynum:
            if coor_axis == axisnumx:
                if abs(valoreve) > 0.5:
                    if valoreve > 0.7:
                        self.frame = "right"

                    if valoreve < 0.7:
                        self.frame = "left"
                    self.dir.x = valoreve * speed

                else:
                    self.dir.x = 0

            if coor_axis == axisnumy:
                if abs(valoreve) > 0.5:

                    self.dir.y = valoreve * speed
                    if valoreve > 0.5:
                        self.frame = "down"
                    if valoreve < 0.5:
                        self.frame = "up"

                else:
                    self.dir.y = 0

    def move_bullet(self, player_control, coor_axis, valoreve, axisnumx, axisnumy, joynum, speed):
        if player_control == joynum:
            if coor_axis == axisnumx:
                if abs(valoreve) > 0.5:
                    self.dir.x = valoreve * speed

                else:
                    self.dir.x = 0

            if coor_axis == axisnumy:
                if abs(valoreve) > 0.5:
                    self.dir.y = valoreve * speed

                else:
                    self.dir.y = 0







   

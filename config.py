import pygame

pygame.display.init()

# Game display
game_name = "Robotron 2084"
screen_height = 800
screen_width = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)
sprite_sheet = "assets/sprites/Robotron-Sprites.jpg"
sprite_sheet_size = [308, 203]
icon_scale = 3
icon_image_load = pygame.image.load(sprite_sheet)
icon_image_load = pygame.transform.scale(icon_image_load, [308 * icon_scale, 203 * icon_scale])
icon = pygame.surface.Surface((25, 25))
icon.blit(icon_image_load, (0, 0), (173*icon_scale, 82*icon_scale, 25, 25))
pygame.display.set_icon(icon)
game_font = "assets/font/PressStart2P.ttf"
startscreen = "assets/sprites/start_img.png"

# sounds
bullet_sound = "assets/sounds/shot_sound.mp3"
get_human_sound = "assets/sounds/get_human_sound.mp3"
damage_sound = "assets/sounds/damaged_sound.mp3"
get_enemy = "assets/sounds/get_enemy.mp3"
victory_sound = "assets/sounds/victory_sound.mp3"


# Player
player_spritesheet = "assets/sprites/Robotron-Sprites.jpg"
scale = 2.6
player_frame_width = 14 * scale
playerspritestart = (92 * scale, 80 * scale)
playerspriteend = (14 * scale, 15 * scale)
player_left = (92 * scale, 132 * scale)
player_right = (130 * scale, 158 * scale)
player_down = (170 * scale, 198 * scale)
player_up = (208 * scale, 248 * scale)
player_speed = 25
player_img_cooldown = 80
player_facing_down = 172 * scale
player_facing_right = 130 * scale
player_facing_left = 92 * scale
player_facing_up = 208 * scale

# Bullet
bullet_sprite = "assets/sprites/bullet_sprite.png"
bulletspritestart = (233 * scale, 0 * scale)
bulletspriteend = (13 * scale, 15 * scale)
bullet_frame_width = 13 * scale
bullet_explosion = (217 * scale, 243 * scale)

# Wall
wall_img = "assets/sprites/walls.png"
wall_upper_lim = 60
wall_bottom_lim = 725
wall_left_lim = 7
wall_right_lim = 960

# Hulk
hulkspritestart = (0 * scale, 40 * scale)
hulkspriteend = (15 * scale, 18 * scale)
hulk_frame_width = 18 * scale
hulk_up = (20 * scale, 40 * scale)
hulk_down = (20 * scale, 40 * scale)
hulk_img_cooldown = 160
hulk_walk_dis = 200
hulk_speed = 2

# Red robot
red_robotspritestart = (160 * scale, 115 * scale)
red_robotspriteend = (15 * scale, 18 * scale)
red_robot_frame_width = 15 * scale
red_robot_up = (70 * scale, 100 * scale)
red_robot_down = (70 * scale, 100 * scale)
red_robot_img_cooldown = 160
red_robot_walk_dis = 100
red_robot_speed = 3

# Human
humanspritestart = (233 * scale, 0 * scale)
humanspriteend = (13 * scale, 15 * scale)
human_frame_width = 13 * scale
human_up = (217 * scale, 243 * scale)
human_down = (178 * scale, 204 * scale)
human_img_cooldown = 160
human_walk_dis = 100
humanpoints = 2000

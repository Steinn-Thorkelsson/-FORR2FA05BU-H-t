import pygame
import sys

# General setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1 = pygame.image.load('cloud1.png')
cloud2 = pygame.image.load('cloud2.png')
crosshair = pygame.image.load('crosshair.png')

land_position_y = 560
land_speed = 1
water_position_y = 640
water_speed = 1.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)

    screen.blit(wood_bg, (0, 0))

    # Animation
    land_position_y += land_speed
    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))

    water_position_y += water_speed
    if water_position_y <= 620 or water_position_y >= 680:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))

    screen.blit(crosshair, crosshair_rect)
    # Clouds
    screen.blit(cloud1, (50, 80))
    screen.blit(cloud2, (190, 20))
    screen.blit(cloud1, (500, 80))
    screen.blit(cloud2, (800, 20))
    screen.blit(cloud1, (1100, 60))

    pygame.display.update()
    clock.tick(120)

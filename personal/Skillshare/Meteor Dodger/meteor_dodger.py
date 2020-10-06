import pygame
import sys


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constraint()

    def screen_constraint(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280

        if self.rect.left <= 0:
            self.rect.left = 0


class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

spaceship = SpaceShip('Spaceship.png', 640, 500, 7)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_1 = Meteor('Meteor1.png', 400, -100, 1, 10)
meteor_group = pygame.sprite.GroupSingle()
meteor_group.add(meteor_1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    screen.fill((42, 45, 51))

    spaceship_group.draw(screen)
    meteor_group.draw(screen)
    spaceship_group.update()
    meteor_group.update()
    pygame.display.update()
    clock.tick(120)

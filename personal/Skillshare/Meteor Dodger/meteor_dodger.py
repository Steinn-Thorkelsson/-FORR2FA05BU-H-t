import pygame
import sys
import random


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.shield_surface = pygame.image.load('shield.png')
        self.health = 5

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constraint()
        self.display_health()

    def screen_constraint(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280

        if self.rect.left <= 0:
            self.rect.left = 0

    def display_health(self):
        for index, shield in enumerate(range(self.health)):
            screen.blit(self.shield_surface, (10 + index * 40, 10))

    def get_damage(self, damage_amaount):
        self.health -= damage_amaount


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

        if self.rect.centery >= 800:
            self.kill()


class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed

        if self.rect.centery <= -10:
            self.kill()


def main_game():
    laser_group.draw(screen)
    spaceship_group.draw(screen)
    meteor_group.draw(screen)

    laser_group.update()
    spaceship_group.update()
    meteor_group.update()

    # Collision
    if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
        spaceship_group.sprite.get_damage(1)
        pygame.mixer.Sound.play(meteor_impact_spaceship)
    for laser in laser_group:
        pygame.sprite.spritecollide(laser, meteor_group, True)
        pygame.mixer.Sound.play(laser_impact_meteor)

    return 1


def end_game():
    retry_surface = retry_font.render('Press SPACE to Restart', True, (200, 255, 255))
    retry_rect = retry_surface.get_rect(center=(640, 560))
    screen.blit(retry_surface, retry_rect)

    gover_surface = game_font.render('Game Over :(', True, (200, 255, 5))
    gover_rect = gover_surface.get_rect(center=(640, 360))
    screen.blit(gover_surface, gover_rect)

    score_surface = retry_font.render(f'Score: {score}', True, (200, 255, 5))
    score_rect = score_surface.get_rect(center=(640, 450))
    screen.blit(score_surface, score_rect)


def score_text(score_live):
    score_surface = score_font.render(f'Score: {score_live}', True, (200, 255, 5))
    score_rect = score_surface.get_rect(center=(1200, 15))
    screen.blit(score_surface, score_rect)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 100)
retry_font = pygame.font.Font(None, 40)
score_font = pygame.font.Font(None, 30)
score = 0

spaceship = SpaceShip('Spaceship.png', 640, 500, 7)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_group = pygame.sprite.Group()

METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, 250)

laser_group = pygame.sprite.Group()

# Sounds
laser_shoot = pygame.mixer.Sound('laser_shoot.wav')
laser_impact_meteor = pygame.mixer.Sound('laser_impact_meteor.wav')
meteor_impact_spaceship = pygame.mixer.Sound('meteor_impact_spaceship.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == METEOR_EVENT:
            meteor_path = random.choice(('Meteor1.png', 'Meteor2.png', 'Meteor3.png'))
            random_x_pos = random.randrange(0, 1280)
            random_y_pos = random.randrange(-500, -50)
            random_x_speed = random.randrange(-1, 1)
            random_y_speed = random.randrange(4, 10)
            meteor = Meteor(meteor_path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)
            meteor_group.add(meteor)

        if event.type == pygame.MOUSEBUTTONDOWN:
            new_laser = Laser('Laser.png', event.pos, 15)
            laser_group.add(new_laser)
            pygame.mixer.Sound.play(laser_shoot)

        if event.type == pygame.KEYDOWN and spaceship_group.sprite.health <= 0:
            if event.key == pygame.K_SPACE:
                spaceship_group.sprite.health = 5
                meteor_group.empty()
                score = 0

    screen.fill((42, 45, 51))

    if spaceship_group.sprite.health > 0:
        score += main_game()
        score_text(score)

    else:
        end_game()

    pygame.display.update()
    clock.tick(120)

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroidfield import AsteroidField
from constants import *
from asteroid import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0
    game_time = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable,drawable,shots)
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    p1 = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if p1.collision_check(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()

        for x in drawable:
            x.draw(screen)
        pygame.display.flip()
        dt = (game_time.tick(60)) / 1000

if __name__ == "__main__":
    main()
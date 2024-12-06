import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

    Shot.containers = (updatable_group, drawable_group, shots)
    
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable_group:
            obj.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

            if asteroid.collides_with(player):
                exit("Game Over!!")
    
        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__=="__main__":
    main()

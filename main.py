# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    clock = pygame.time.Clock()
    dt = 0
    player = Player(CENTER_W, CENTER_H)
    field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        #print(f"dt: {dt}")
        #print(f"Number of asteroids: {len(asteroids)}")
        #print(f"Number of updatable objects: {len(updatable)}")
        for a in asteroids:
            if a.check_collision(player):
                print ("Game over!")
                return
        for a in asteroids:
            for s in shots:
                if a.check_collision(s):
                    a.split()
                    s.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()

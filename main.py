# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *


def main():
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    player = Player(CENTER_W, CENTER_H)
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
        pygame.display.flip()
        clock.tick(60)
        dt = 60/1000



if __name__ == "__main__":
    main()

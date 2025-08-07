import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            a = random.uniform(20, 50)
            p = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
            p.velocity = self.velocity.rotate(a) * 1.2
            n = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
            n.velocity = self.velocity.rotate(-a) * 1.2
            self.kill()
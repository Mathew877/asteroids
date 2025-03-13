import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # this was small asteroid
        
        # asteroids that were not small need to spawn 2 new asteroids
        # that go off at random angles
        angle = random.uniform(20, 50)
        v1 = self.position.rotate(-angle)
        v2 = self.position.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1 * NEW_ASTEROID_SPEED_INCREASE
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2 * NEW_ASTEROID_SPEED_INCREASE

import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        left_velocity = self.velocity.rotate(angle)
        right_velocity = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity += left_velocity * 1.2
        right_asteroid.velocity += right_velocity * 1.2
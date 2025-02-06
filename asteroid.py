import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        #self.x = x
        #self.y = y
        #self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position), self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x,self.position.y, new_radius)
            a2 = Asteroid(self.position.x,self.position.y, new_radius)
            a1.velocity = vector1 * 1.2
            a2.velocity = vector2 * 1.2

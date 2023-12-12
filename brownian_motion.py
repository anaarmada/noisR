import pygame
import sys
import random
import math
from math import cos,sin,sqrt

pygame.init()

# Constants
WIDTH, HEIGHT = 800 , 600
FPS = 60
PARTICLE_RADIUS = 10
NUM_PARTICLES = 50
MAX_SPEED = 2

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

#Particle class
class Particle:
    def __init__ (self, x, y, r, c, v, a, bool, lst):
        self.x = x
        self.y = y
        self.radius = r
        self.color = c
        self.speed = v 
        self.angle = a
        self.is_tracer = bool
        self.path = lst
    
    def move(self):
        t=1
        if self.is_tracer:
            self.color=BLUE
            while t<=FPS:    
                if self.x<=0 or self.x>=WIDTH:
                    self.speed=-self.speed
                elif self.y>=HEIGHT or self.y<=0:                    
                    self.speed=-self.speed
                for i in range(0,len(particles)):
                    particle=particles[i]
                    bool=check_collision(self,particle)
                    if bool:
                        continue
                self.path=[]
                self.x=self.x+cos(self.angle)*self.speed*t
                self.y=self.y+sin(self.angle)*self.speed*t
                position=(self.x,self.y)
                self.path.append(position)
                t+=0.01
    
    
def check_collision(self,other_particle):
    distance=sqrt((self.x-other_particle.x)**2+(self.y-other_particle.y)**2)
    if self!=other_particle and distance<=PARTICLE_RADIUS:
        return True
    else:
        return False
    
# Create particles   
particles=[]
for i in range(0,NUM_PARTICLES-1):
    x=random.randint(0,800)
    y=random.randint(0,600)
    angle=random.randint(0,180)
    speed=random.randint(-MAX_SPEED,MAX_SPEED)
    colour=RED
    particle=Particle(x, y, PARTICLE_RADIUS, colour, speed, angle, False, [])
    particles.append(particle)

# Choose one particle as a tracer
tracer_index = random.randint(0, NUM_PARTICLES - 1)
tracker=particles[tracer_index]
tracker.is_tracer=True

# Set up Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brownian Motion Simulaton")
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move particles and check collisions
    for particle in particles:
        particle.move()

    # Draw particles and paths
    screen.fill (WHITE)
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.radius)
        
        # Draw path for the tracer
        if particle.is_tracer and len(particle.path) >= 2:
            pygame.draw.lines( screen, particle.color, False, particle.path , 2)
    
    pygame.display.flip()
    clock.tick(FPS)
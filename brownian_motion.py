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
MAX_SPEED = 0.5

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

#Particle class
class Particle:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.radius = PARTICLE_RADIUS
        self.color = RED
        self.speed = random.uniform(-MAX_SPEED,MAX_SPEED)
        self.angle = random.uniform(0,180)
        self.is_tracer = False
        self.path = []
    
    def move(self):
        t=1
        while t<=FPS:    
            if self.x<=PARTICLE_RADIUS:
                self.speed=-self.speed
                self.x=PARTICLE_RADIUS
            elif self.x>=WIDTH-PARTICLE_RADIUS:
                self.speed=-self.speed
                self.x=WIDTH-PARTICLE_RADIUS
            elif self.y>=HEIGHT-PARTICLE_RADIUS:
                self.speed=-self.speed             
                self.y=HEIGHT-PARTICLE_RADIUS
            elif self.y<=PARTICLE_RADIUS:
                self.speed=-self.speed
                self.y=PARTICLE_RADIUS    
            for i in range(0,len(particles)):
                other_part=particles[i]
                bool=check_collision(self,other_part)
                if bool:
                    self.speed,other_part.speed=other_part.speed,self.speed
                    self.angle,other_part.angle=other_part.angle,self.angle
                else:
                    continue
            self.x+=cos(self.angle)*self.speed
            self.y+=sin(self.angle)*self.speed
            if self.is_tracer:
                position=(self.x,self.y)
                self.path.append(position)
            t+=1
    
    
def check_collision(self,other_particle):
    distance=sqrt((self.x-other_particle.x)**2+(self.y-other_particle.y)**2)
    if self!=other_particle and distance<=PARTICLE_RADIUS*2:
        return True
    else:
        return False
    
# Create particles   
particles=[]
for i in range(0,NUM_PARTICLES-1):
    par=Particle(random.uniform(0,800),random.uniform(0,600))
    particles.append(par)

# Choose one particle as a tracer
tracer_index = random.randint(0, NUM_PARTICLES - 1)
tracker=particles[tracer_index]
tracker.is_tracer=True
tracker.color=BLUE

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
    screen.fill(WHITE)
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.radius)
        
        # Draw path for the tracer
        if particle.is_tracer and len(particle.path) >= 2:
            pygame.draw.lines( screen, particle.color, False, particle.path, 2)
    
    pygame.display.flip()
    clock.tick(FPS)
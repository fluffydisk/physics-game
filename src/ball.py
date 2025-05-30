from __future__ import annotations
import pygame, random, math
from physics import Physics
import utils

class Ball:
    all_balls = []
    def __init__(self, size):
        self.is_colliding_borders=False
        self.id=len(Ball.all_balls)
        self.size = size
        self.position = pygame.Vector2( random.randint(self.size, (int)(utils.screenSize.x-self.size-1)), 0)
        self.color = pygame.Color(255,0,0,255)
        self.velocity = pygame.Vector2(0,0)

        Ball.all_balls.append(self)

    def check_borders_collision(self):
        collision = {
            "left": self.position.x-self.size <= 0,
            "right": self.position.x+self.size >= utils.screenSize.x,
            "top": self.position.y-self.size <= 0,
            "bottom": self.position.y+self.size >= utils.screenSize.y
        }
        if collision["bottom"] or collision["top"] or collision["right"] or collision["left"]:
            self.is_colliding_borders=True
        else:
            self.is_colliding_borders=False

        return collision
 

    def update(self):
        self.position.x+=self.velocity.x*utils.deltaTime
        self.position.y+=self.velocity.y*utils.deltaTime
        
        self.draw(utils.screen)

    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.size)


import utils
import pygame
import pygame.camera
from ball import Ball
from physics import Physics
import time

ball2 = Ball(15)
ball1 = Ball(15)
ball3 = Ball(15)
ball4 = Ball(15)
ball5 = Ball(15)
ball6 = Ball(15)
ball7 = Ball(15)
ball8 = Ball(15)

def start():
    pygame.init()


def loop():
    running = True
    spawn_ball = False
    last_check=time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEWHEEL:
                if event.y<0:
                    for ball in Ball.all_balls:
                        ball.size-=1
                elif event.y>0:
                    for ball in Ball.all_balls:
                        ball.size+=1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    spawn_ball=True

            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_w:
                    spawn_ball=False

            current_time=time.time()
            if(spawn_ball and (current_time-last_check)>0.1):
                Ball(Ball.all_balls[0].size)
                last_check=current_time

                    
        utils.update()

        utils.screen.fill((0, 0, 0))
        #print(ball1.velocity.x," " , ball1.velocity.y)
        Physics.update()

        for ball in Ball.all_balls:
            ball.update()

        pygame.display.flip()
        utils.clock.tick(utils.FPS)
        
    pygame.quit()

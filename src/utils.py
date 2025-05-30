import pygame
import time

screen = None
clock = None
screenSize = pygame.Vector2()
deltaTime = None
last_fps_check = time.time()
FPS = 60

def loading_screen():
    surface = pygame.image.load("res/loading.png")
    surface = pygame.transform.scale(surface, (300, 300))

    screen.fill((255, 255, 255))
    screen.blit(surface, ((screenSize.x/2)-150, (screenSize.y/2)-150))
    pygame.display.flip()

def start():
    global screen, clock, screenSize, deltaTime
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    screenSize = pygame.Vector2(screen.get_size())
    deltaTime = 0

    loading_screen()


def update():
    global screenSize, clock, deltaTime, last_fps_check
    deltaTime = clock.get_time()/1000
    screenSize = pygame.Vector2(screen.get_size())

    current_time = time.time()
    if current_time - last_fps_check >= 1.0:
        fps = clock.get_fps()
        #print(f"FPS: {fps:.2f}")
        last_fps_check = current_time

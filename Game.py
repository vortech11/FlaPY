import pygame
import random
import time

height = 400
length = 400

pygame.init()
window = pygame.display.set_mode((height, length))
clock = pygame.time.Clock()

player = pygame.Rect(0, 0, 50, 50)
player.x = 100
player.y = height/2
yspeed = 0

bottom_pipe = pygame.Rect(0, 0, 50, 300)
top_pipe = pygame.Rect(0, 100, 50, 400)
positions = []
positions.append(400)
positions.append(random.randrange(-130, 30))
start = time.time()

game_over = False
while not(game_over):
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                yspeed = 5
            
    yspeed -= 0.2

    if abs(yspeed) > 7.5:
        if yspeed > 0:
            yspeed = 7.5
        else:
            yspeed = -7.5

    player.y -= yspeed

    if  time.time() - start > 3:
        positions.append(400)
        positions.append(random.randrange(-130, 30))
        start = time.time()
    
    window.fill(0)
    
    for x in range(0, len(positions), 2):
        positions[x] -= 1.5
        bottom_pipe.x = positions[x]
        top_pipe.x = positions[x]
        bottom_pipe.y = -235 - positions[x + 1]
        top_pipe.y = 235 - positions[x + 1]
        if bottom_pipe.colliderect(player) or top_pipe.colliderect(player):
            game_over = True
        pygame.draw.rect(window, (19, 156, 9), bottom_pipe)
        pygame.draw.rect(window, (19, 156, 9), top_pipe)

    pygame.draw.rect(window, (222, 200, 0), player)
    pygame.display.flip()

pygame.quit()
exit()

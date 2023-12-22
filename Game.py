import pygame
import os

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
positions.append(50)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                yspeed = 7.5
            
    yspeed -= 0.25

    if abs(yspeed) > 7.5:
        if yspeed > 0:
            yspeed = 7.5
        else:
            yspeed = -7.5

    player.y -= yspeed
    
    window.fill(0)
    
    for x in range(0, len(positions), 2):
        positions[x] -= 0.5
        bottom_pipe.x = positions[x]
        top_pipe.x = positions[x]
        bottom_pipe.y = 0 - positions[x + 1]
        top_pipe.y = 0 - positions[x + 1]
        pygame.draw.rect(window, 999, bottom_pipe)
        pygame.draw.rect(window, 999, top_pipe)

    pygame.draw.rect(window, 999, player)
    pygame.display.flip()

pygame.quit()
exit()

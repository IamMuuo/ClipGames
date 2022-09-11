#!/usr/bin/python

import pygame
from pygame import Vector2


player_texture = "player.png"

pygame.init()

# setup the screen display

screen = pygame.display.set_mode((800, 600),depth=32)
pygame.display.set_caption("Using vectors in pygame")

# setup the player sprite for rendering
player = pygame.image.load(player_texture)

# variables to store position ..

position = Vector2(0,0)
speed, speed_y = 100, 100
clock = pygame.time.Clock()


# game event loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # display the sprite
    screen.fill((0,0,0))
    screen.blit(player, position)

    pygame.display.update()

    elapsed = clock.tick(30)  # set fps
    elapsed_seconds = elapsed / 1000

    # move the sprite
    if position.x > 800 - player.get_width():
        speed = -speed

    elif position.x < 0:
        speed = -speed

    if position.y > 600 - player.get_height():
        speed_y = -speed_y
    elif position.y < 0:
        speed_y = -speed_y

    
    position.x += elapsed_seconds * speed
    position.y += elapsed_seconds * speed_y 
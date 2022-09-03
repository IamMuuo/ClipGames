#!/usr/bin/python

# Demonstrates single movement

import pygame

pygame.init()

sprite_path = 'img/player.png'

# setup the screen
screen = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Simple movement')


# setup the sprite for drawing
sprite = pygame.image.load(sprite_path).convert_alpha()
x = 0

# game event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    screen.blit(sprite,(x,100))

    x += 1

    if x > 800:
        x -= 800

    pygame.display.update()

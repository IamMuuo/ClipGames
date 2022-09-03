#!/usr/bin/python

# Compares frame rates on two different machines

import pygame
pygame.init()

# setup the display
screen = pygame.display.set_mode((800,600))

sprite_path = 'img/player.png'

sprite = pygame.image.load(sprite_path)

pygame.display.set_icon(sprite)


# the clock object
clock = pygame.time.Clock()

# coordinates
x1 = 0
x2 = 0

# speed in pixels per second
speed = 250
frames = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    screen.blit(sprite, (x1, 50))
    screen.blit(sprite, (x2, 250))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000

    distance_moved = time_passed_seconds * speed
    x1 +=distance_moved


    if (frames % 5 == 0):
        distance_moved = time_passed_seconds * speed
        x2 += distance_moved * 5

    if x1 > 800:
        x1 -= 800
    if x2 > 800:
        x2 -= 800

    pygame.display.update()



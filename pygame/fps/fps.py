#!/usr/bin/python

# Demonstrates how to use fps

import pygame

pygame.init()

sprite_path = 'img/player.png'

# setup the display
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Time based movement')


# setup the sprite for rendering
sprite = pygame.image.load(sprite_path).convert_alpha()

# the clock object
clock = pygame.time.Clock()

# the coordinate for the sprite
x = 0

# speed
speed = 100

while True:

    # check for events
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()

    time_passed_seconds = time_passed / 1000

    distance_moved = time_passed_seconds * speed

    x += distance_moved

    if x > 800:
        x -= 800

    pygame.display.update()

'''
Author: Erick Muuo
Copyright (C) 2022

Description: This program generates all colors and
            saves the output in a file
'''


import pygame

pygame.init()   #initialize pygame


all_colors  = pygame.Surface((4096, 4096), depth=32)

for r in range(256):
    print(r+1, "of 256")

    x = (r & 15) * 256
    y = (r >> 4) * 256

    for g in range(256):
        for b in range(256):
            all_colors.set_at((x + g, y + b ), (r, g, b))

# saving
pygame.image.save(all_colors, "colors.bmp")
pygame.quit()

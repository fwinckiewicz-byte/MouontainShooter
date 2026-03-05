import sys

import pygame
pygame.init()
window = pygame.display.set_mode((600, 480))
print('setup end')

print('loop start')
while True:
    #check for aall events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            sys.exit()

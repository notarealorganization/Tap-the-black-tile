import pygame, random, sys
from pygame.locals import *

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 300
TILE_WIDTH = WINDOW_WIDTH / 4
TILE_HEIGHT = WINDOW_HEIGHT / 5

def pickRandomTile ():
    tile = random.randint(1,4)
    if tile == 1:
        return 0
    elif tile == 2:
        return TILE_WIDTH
    elif tile == 3:
        return TILE_WIDTH * 2
    elif tile == 4:
        return TILE_WIDTH * 3
    else:
        return 215
        
#set up pygame
pygame.init()

#set up window
window = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT), 0 , 32)
pygame.display.set_caption('Tap the Black Tiles')

#colors
BLACK= (0,0,0)
WHITE = (255,255,255)

#fill in window white
window.fill (WHITE)

#draw guide lines

#vertical
pygame.draw.line(window, BLACK,(TILE_WIDTH,0),(TILE_WIDTH,500),4)
pygame.draw.line(window, BLACK,(TILE_WIDTH * 2,0),(TILE_WIDTH * 2,500),4)
pygame.draw.line(window, BLACK,(TILE_WIDTH * 3 ,0),(TILE_WIDTH * 3,500),4)
pygame.draw.line(window, BLACK,(TILE_WIDTH * 4, 0),(TILE_WIDTH * 4,500),4)

#horazonatl
pygame.draw.line(window, BLACK,(0, TILE_HEIGHT),(300, TILE_HEIGHT),4)
pygame.draw.line(window, BLACK,(0, TILE_HEIGHT * 2),(300, TILE_HEIGHT * 2),4)
pygame.draw.line(window, BLACK,(0, TILE_HEIGHT * 3),(300, TILE_HEIGHT * 3),4)
pygame.draw.line(window, BLACK,(0, TILE_HEIGHT * 4),(300, TILE_HEIGHT * 4),4)
pygame.draw.line(window, BLACK,(0, TILE_HEIGHT * 5),(300, TILE_HEIGHT * 5),4)


# draw the squares
pygame.draw.rect (window, BLACK, (pickRandomTile(),0, TILE_WIDTH, TILE_HEIGHT))
pygame.draw.rect (window, BLACK, (pickRandomTile(),TILE_HEIGHT , TILE_WIDTH, TILE_HEIGHT))
pygame.draw.rect (window, BLACK, (pickRandomTile(),TILE_HEIGHT * 2, TILE_WIDTH, TILE_HEIGHT))
pygame.draw.rect (window, BLACK, (pickRandomTile(),TILE_HEIGHT * 3, TILE_WIDTH, TILE_HEIGHT))
pygame.draw.rect (window, BLACK, (pickRandomTile(),TILE_HEIGHT * 4, TILE_WIDTH, TILE_HEIGHT))


#update window
pygame.display.update()

#run the game loop
while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            sys.exit ()

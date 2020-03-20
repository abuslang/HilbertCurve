import pygame
import math

pygame.init()

# define color values for ease of use
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# initialize 800 x 600 pixel window
gameDisplay = pygame.display.set_mode((512,512))
gameDisplay.fill(black)



def Hilbert(i):
    points = [[0,0], [0,1], [1,1], [1,0]]
    return points[i]

order = 1
n = math.pow(2, order)
total = n * n           # total number of points
total = int(total)

path = [[0,0] for i in range(int(total))]

for i in range(0,int(total)):
    path[i] = Hilbert(i)
    len = 512 / n
    path[i][0] *= len
    path[i][1] *= len
    path[i][0] += len/2
    path[i][1] += len/2


for i in range (0, total-1):
    pygame.draw.line(gameDisplay, white, path[i], path[i+1], 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()


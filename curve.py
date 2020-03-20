import pygame
import math

pygame.init()

# define color values for ease of use
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

colors = [white,red,green,blue]

width = 1024
height = 1024

gameDisplay = pygame.display.set_mode((width,height))
gameDisplay.fill(black)


order = 8
n = math.pow(2, order)
total = n * n           # total number of points
total = int(total)


def Hilbert(i):
    points = [[0,0], [0,1], [1,1], [1,0]]

    index = i & 3
    returnPoint = points[index]

    for j in range(1, order):

        i = i >> 2
        index = i & 3
        lent = math.pow(2,j)

        if index == 0:
            temp = returnPoint[0]
            returnPoint[0] = returnPoint[1]
            returnPoint[1] = temp
        elif index == 1:
            returnPoint[1] += lent
        elif index == 2:
            returnPoint[0] += lent
            returnPoint[1] += lent
        elif index == 3:
            temp = lent - 1 - returnPoint[0]
            returnPoint[0] = lent - 1 - returnPoint[1]
            returnPoint[1] = temp
            returnPoint[0] += lent

    return returnPoint


path = [[0,0] for i in range(total)]

for i in range(0,total):
    path[i] = Hilbert(i)
    len = width / n
    path[i][0] *= len
    path[i][1] *= len
    path[i][0] += len/2
    path[i][1] += len/2


#for i in range (0, total-1):
 #   pygame.draw.line(gameDisplay, white, path[i], path[i+1], 2)

counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    if counter < total-1:
        pygame.draw.line(gameDisplay, colors[3], path[counter], path[counter + 1], 2)
        counter += 1


   # pygame.time.delay(50)
    pygame.display.update()


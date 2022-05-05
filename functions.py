import pygame

def euclideanDist(locale, goal): # use a euclidean measurement to use as a fee
    xy1 = locale
    xy2 = goal
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5


def create_grid(w, chain, side):
    BSize = w // chain

    x = 0
    y = 0
    for l in range(chain):
        x = x + BSize
        y = y + BSize

        pygame.draw.line(side, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(side, (255, 255, 255), (0, y), (w, y))

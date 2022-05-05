import pygame

class square(object):
    chain = 20
    w = 500

    def __init__(self, start, xasis=1, yasis=0, tone=(255, 0, 0)):
        self.pos = start
        self.xasis = 1
        self.yasis = 0
        self.tone = tone

    def motion(self, xasis, yasis):
        self.xasis = xasis
        self.yasis = yasis
        self.pos = (self.pos[0] + self.xasis, self.pos[1] + self.yasis)

    def draw(self, side, scan=False):
        d = self.w // self.chain
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(side, self.tone, (i * d + 1, j * d + 1, d - 2, d - 2))
        if scan:
            nucleus = d // 2
            rad = 3
            MidwayClique = (i * d + nucleus - rad, j * d + 8)
            SecondMidwayClique = (i * d + d - rad * 2, j * d + 8)
            pygame.draw.circle(side, (0, 0, 0), MidwayClique, rad)
            pygame.draw.circle(side, (0, 0, 0), SecondMidwayClique, rad)
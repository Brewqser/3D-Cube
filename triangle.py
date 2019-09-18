import pygame
from pygame import Vector3
from object import Object


class Triangle(Object):
    def __init__(self,
                 a=Vector3(0, 0, 0),
                 b=Vector3(1, 1, 0),
                 c=Vector3(2, 0, 0),
                 color=(255, 255, 255),
                 scale=40,
                 fill=False,
                 width=1):
        super().__init__()
        self.vertex.append(a)
        self.vertex.append(b)
        self.vertex.append(c)

        self.color = color
        self.scale = scale
        self.fill = fill
        self.width = width

    def setA(self, a=Vector3(0, 0, 0)):
        self.vertex[0] = a

    def setB(self, b=Vector3(1, 1, 0)):
        self.vertex[1] = b

    def setC(self, c=Vector3(2, 0, 0)):
        self.vertex[2] = c

    def set_tri(self, a=Vector3(0, 0, 0), b=Vector3(1, 1, 0), c=Vector3(2, 0, 0)):
        self.setA(a)
        self.setB(b)
        self.setC(c)

    def draw(self, sur, mat=0):
        pointlist = [(i[0], i[1]) for i in self.vertex]

        if self.fill:
            pygame.draw.polygon(sur, self.color, pointlist)
        else:
            pygame.draw.polygon(sur, self.color, pointlist, self.width)

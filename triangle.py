import pygame
from pygame import Vector3
from object import Object


class Triangle(Object):
    def __init__(self, scale=40, fill=False, width=2):
        super().__init__()
        self.vertex.append(Vector3(0, 0, 0))
        self.vertex.append(Vector3(1, 1, 0))
        self.vertex.append(Vector3(2, 0, 0))

        self.scale = scale
        self.fill = fill
        self.width = width

    def setA(self, a=Vector3(0, 0, 0)):
        self.vertex[0] = a

    def setB(self, b=Vector3(1, 1, 0)):
        self.vertex[1] = b

    def setC(self, c=Vector3(2, 0, 0)):
        self.vertex[2] = c

    def draw(self, sur):
        if self.fill:
            pygame.draw.polygon(sur, (255, 255, 255),
                                [(i[0] * self.scale + 400, i[1] * self.scale + 200) for i in self.vertex])
        else:
            pygame.draw.polygon(sur, (255, 255, 255),
                                [(i[0]*self.scale + 400, i[1]*self.scale + 200) for i in self.vertex], self.width)

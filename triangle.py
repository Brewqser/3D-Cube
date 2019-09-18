

import pygame
from copy import deepcopy
from object import Object
from matrixop import *


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

        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0

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

    def rotX(self, p):
        p[0] = rotateX(p[0], self.x_angle)
        p[1] = rotateX(p[1], self.x_angle)
        p[2] = rotateX(p[2], self.x_angle)

    def rotY(self, p):
        p[0] = rotateY(p[0], self.y_angle)
        p[1] = rotateY(p[1], self.y_angle)
        p[2] = rotateY(p[2], self.y_angle)

    def rotZ(self, p):
        p[0] = rotateZ(p[0], self.z_angle)
        p[1] = rotateZ(p[1], self.z_angle)
        p[2] = rotateZ(p[2], self.z_angle)

    def draw(self, eng):

        p = deepcopy(self.vertex)

        self.rotZ(p)
        self.rotX(p)
        self.rotY(p)

        p[0][2] += 3
        p[1][2] += 3
        p[2][2] += 3

        pro = [project3Dto2D(p[0], eng.matrix),
               project3Dto2D(p[1], eng.matrix),
               project3Dto2D(p[2], eng.matrix)]

        pro[0][0] += 1
        pro[0][1] += 1
        pro[1][0] += 1
        pro[1][1] += 1
        pro[2][0] += 1
        pro[2][1] += 1

        pro[0][0] *= 0.5 * eng.screen.get_width()
        pro[0][1] *= 0.5 * eng.screen.get_height()
        pro[1][0] *= 0.5 * eng.screen.get_width()
        pro[1][1] *= 0.5 * eng.screen.get_height()
        pro[2][0] *= 0.5 * eng.screen.get_width()
        pro[2][1] *= 0.5 * eng.screen.get_height()

        pointlist = [(i[0], i[1]) for i in pro]

        if self.fill:
            pygame.draw.polygon(eng.screen, self.color, pointlist)
        else:
            pygame.draw.polygon(eng.screen, self.color, pointlist, self.width)

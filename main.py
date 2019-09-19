import math

from engine3D import Engine3D
import pygame
from pygame import Vector3
from triangle import Triangle
from cube import Cube


class Engine(Engine3D):
    def __init__(self):
        super().__init__()
        self.objects.append(Cube(2, 2, 2))
        #
        # self.objects[0].angleX = 90
        # self.objects[0].angleY = 180
        # self.a = Cube()

    def update(self):
        pass

    def tick(self):
        # self.objects.x += 1
        self.objects[0].angleZ += 1
        self.objects[0].angleX += 0.5
        self.objects[0].angleY -= 0.8
        pass

    def draw(self):
        # self.a.draw(self)
        pass

#
# print(math.cos(math.radians(60)))

engine = Engine()

engine.construct_console(800, 800)

engine.start()

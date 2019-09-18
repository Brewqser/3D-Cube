from engine3D import Engine3D
import pygame
from pygame import Vector3
from triangle import Triangle
from cube import Cube


class Engine(Engine3D):
    def __init__(self):
        super().__init__()
        self.objects.append(Cube())
        # self.a = Cube()

    def update(self):
        pass

    def tick(self):
        # self.objects.x += 1
        self.objects[0].angleZ += 0.05
        self.objects[0].angleX += 0.01
        self.objects[0].angleY -= 0.02

    def draw(self):
        # self.a.draw(self)
        pass


engine = Engine()

engine.construct_console(800, 800)

engine.start()

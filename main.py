from engine3D import Engine3D
import pygame
from pygame import Vector3
from triangle import Triangle
from cube import Cube


class Engine(Engine3D):
    def __init__(self):
        super().__init__()
        self.objects.append(Cube())

    def update(self):
        pass

    def tick(self):
        # self.objects.x += 1
        pass


engine = Engine()

engine.construct_console(800, 800)

engine.start()

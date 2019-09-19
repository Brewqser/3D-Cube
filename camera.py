import pygame
import sys
import numpy as np
from math import tan, pi, radians
from pygame import Vector3


class Camera:
    def __init__(self, pos=Vector3(0, 0, 0)):
        self.pos = pos

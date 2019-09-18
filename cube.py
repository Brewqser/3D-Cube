from copy import deepcopy
from pygame import Vector3
from object import Object
from triangle import Triangle


class Cube(Object):
    def __init__(self, color=(255, 255, 255), scale=40, fill=False, width=2):
        super().__init__()
        self.mesh = []
        # Front
        tri = Triangle(a=Vector3(0, 0, 0), b=Vector3(0, 1, 0), c=Vector3(1, 1, 0))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(0, 0, 0), b=Vector3(1, 1, 0), c=Vector3(1, 0, 0))
        self.mesh.append(tri)
        # Right
        tri = Triangle(a=Vector3(1, 0, 0), b=Vector3(1, 1, 0), c=Vector3(1, 1, 1))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(1, 0, 0), b=Vector3(1, 1, 1), c=Vector3(1, 0, 1))
        self.mesh.append(tri)
        # Back
        tri = Triangle(a=Vector3(1, 0, 1), b=Vector3(1, 1, 1), c=Vector3(0, 1, 1))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(1, 0, 1), b=Vector3(0, 1, 1), c=Vector3(0, 0, 1))
        self.mesh.append(tri)
        # Left
        tri = Triangle(a=Vector3(0, 0, 1), b=Vector3(0, 1, 1), c=Vector3(0, 1, 0))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(0, 0, 1), b=Vector3(0, 1, 0), c=Vector3(0, 0, 0))
        self.mesh.append(tri)
        # Top
        tri = Triangle(a=Vector3(0, 1, 0), b=Vector3(0, 1, 1), c=Vector3(1, 1, 1))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(0, 1, 0), b=Vector3(1, 1, 1), c=Vector3(1, 1, 0))
        self.mesh.append(tri)
        # Bottom
        tri = Triangle(a=Vector3(1, 0, 1), b=Vector3(0, 0, 1), c=Vector3(0, 0, 0))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(1, 0, 1), b=Vector3(0, 0, 0), c=Vector3(1, 0, 0))
        self.mesh.append(tri)

        self.angleX = 0.0
        self.angleY = 0.0
        self.angleZ = 0.0

    def draw(self, eng):
        self.angleX %= 360.0
        self.angleY %= 360.0
        self.angleZ %= 360.0

        for tri in self.mesh:
            tri.z_angle = self.angleZ
            tri.x_angle = self.angleX
            tri.y_angle = self.angleY
            tri.draw(eng)
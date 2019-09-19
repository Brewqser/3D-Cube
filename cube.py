from copy import deepcopy

from pygame import Vector3
from object import Object
from triangle import Triangle


class Cube(Object):
    def __init__(self, w, h, d, color=(255, 255, 255), fill=False, width=2):
        super().__init__()
        self.mesh = []
        self.make_cube(w, h, d, color, fill, width)

        self.angleX = 0.0
        self.angleY = 0.0
        self.angleZ = 0.0

    def make_cube(self, w, h, d, color, fill, width):
        # Front
        tri = Triangle(a=Vector3(0, 0, 0), b=Vector3(w, 0, 0), c=Vector3(w, h, 0))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(0, 0, 0), b=Vector3(w, h, 0), c=Vector3(0, h, 0))
        self.mesh.append(tri)
        # Right
        tri = Triangle(a=Vector3(w, 0, 0), b=Vector3(w, 0, d), c=Vector3(w, h, d))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(w, 0, 0), b=Vector3(w, h, d), c=Vector3(w, h, 0))
        self.mesh.append(tri)
        # Back
        tri = Triangle(a=Vector3(w, 0, d), b=Vector3(0, 0, d), c=Vector3(0, h, d))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(w, 0, d), b=Vector3(0, h, d), c=Vector3(w, h, d))
        self.mesh.append(tri)
        # Left
        tri = Triangle(a=Vector3(0, 0, d), b=Vector3(0, 0, 0), c=Vector3(0, h, 0))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(0, 0, d), b=Vector3(0, h, 0), c=Vector3(0, h, d))
        self.mesh.append(tri)
        # Top
        tri = Triangle(a=Vector3(0, 0, 0), b=Vector3(0, 0, d), c=Vector3(w, 0, d))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(0, 0, 0), b=Vector3(w, 0, d), c=Vector3(w, 0, 0))
        self.mesh.append(tri)
        # Bottom
        tri = Triangle(a=Vector3(w, h, d), b=Vector3(0, h, d), c=Vector3(0, h, 0))
        self.mesh.append(tri)
        tri = Triangle(a=Vector3(w, h, d), b=Vector3(0, h, 0), c=Vector3(w, h, 0))
        self.mesh.append(tri)

    def draw(self, eng):
        self.angleX %= 360.0
        self.angleY %= 360.0
        self.angleZ %= 360.0

        for tri in self.mesh:
            t = deepcopy(tri)

            t.z_angle = self.angleZ
            t.x_angle = self.angleX
            t.y_angle = self.angleY
            t.fill = True
            # t.draw(eng)

            # t.fill = False
            # t.color = Vector3(255,0,0)
            t.draw(eng)

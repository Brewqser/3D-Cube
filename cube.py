from copy import deepcopy
from pygame import Vector3
from object import Object
from triangle import Triangle
from matrixop import MatrixOp


class Cube(Object):
    def __init__(self, color=(255, 255, 255), scale=40, fill=False, width=2):
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

    def draw(self, scr, mat):
        for tri in self.mesh:
            tp = deepcopy(tri)
            # tp.set_tri(tri.vertex[0], tri.vertex[1], tri.vertex[2])

            # print(tp is tri)
            tp.vertex[0][2] += 3
            tp.vertex[1][2] += 3
            tp.vertex[2][2] += 3
            # print(tp.vertex)
            #
            # print(tp.vertex)
            tp.set_tri(mat.get_projected(tp.vertex[0]),
                       mat.get_projected(tp.vertex[1]),
                       mat.get_projected(tp.vertex[2]))
            # print(tp.vertex)

            # scale for now
            tp.vertex[0][0] += 1
            tp.vertex[0][1] += 1
            tp.vertex[1][0] += 1
            tp.vertex[1][1] += 1
            tp.vertex[2][0] += 1
            tp.vertex[2][1] += 1

            tp.vertex[0][0] *= 0.5 * scr.get_width()
            tp.vertex[0][1] *= 0.5 * scr.get_height()
            tp.vertex[1][0] *= 0.5 * scr.get_width()
            tp.vertex[1][1] *= 0.5 * scr.get_height()
            tp.vertex[2][0] *= 0.5 * scr.get_width()
            tp.vertex[2][1] *= 0.5 * scr.get_height()

            tp.draw(scr)

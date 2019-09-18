import numpy as np
from pygame import Vector3
from math import tan, pi


class MatrixOp:
    def __init__(self, width, height):
        fNear = 0.1
        fFar = 1000.0
        fFov = 90.0
        fAspectRatio = float(height) / float(width)
        fFovRad = 1.0 / tan(fFov * 0.5 / 180.0 * pi)

        self.projection_matrix = np.array([[fAspectRatio * fFovRad, 0, 0, 0],
                                           [0, fFovRad, 0, 0],
                                           [0, 0, fFar / (fFar - fNear), 1],
                                           [0, 0, (-fFar * fNear) / (fFar - fNear), 0]])
        print(self.projection_matrix)

    def get_projected(self, a=Vector3(0, 0, 0)):
        # print("a" , a)
        b = np.array([a[0], a[1], a[2], 1])
        tmp = np.matmul(b, self.projection_matrix)
        if tmp[3] != 0:
            tmp = [i/tmp[3] for i in tmp]

        # print(tmp[:])

        return Vector3(tmp[0], tmp[1], tmp[2])


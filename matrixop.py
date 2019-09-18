import numpy as np
from pygame import Vector3
from math import sin, cos


def matmul(a, b):
    a = np.array([a[0], a[1], a[2], 1])
    tmp = np.matmul(a, b)
    if tmp[3] != 0:
        tmp = [i / tmp[3] for i in tmp]
    return Vector3(tmp[0], tmp[1], tmp[2])


def rotateX(a=Vector3(0, 0, 0), angle=0):
    matrix = np.array([[1, 0, 0, 0],
                       [0, cos(angle), -sin(angle), 0],
                       [0, sin(angle), cos(angle), 0],
                       [0, 0, 0, 1]])
    return matmul(a, matrix)


def rotateY(a=Vector3(0, 0, 0), angle=0):
    matrix = np.array([[cos(angle), 0, sin(angle), 0],
                       [0, 1, 0, 0],
                       [-sin(angle), 0, cos(angle), 0],
                       [0, 0, 0, 1]])
    return matmul(a, matrix)


def rotateZ(a=Vector3(0, 0, 0), angle=0):
    matrix = np.array([[cos(angle), -sin(angle), 0, 0],
                       [sin(angle), cos(angle), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    return matmul(a, matrix)


def project3Dto2D(a=Vector3(0, 0, 0), matrix=[]):

    return matmul(a, matrix)


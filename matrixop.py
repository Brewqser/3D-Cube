import numpy as np
from pygame import Vector3
from math import sin, cos, radians


def matmul(a, b):
    a = np.array([a[0], a[1], a[2], 1])
    tmp = np.matmul(a, b)
    if tmp[3] != 0:
        tmp = [i / tmp[3] for i in tmp]
    return Vector3(tmp[0], tmp[1], tmp[2])


def rotateX(a=Vector3(0, 0, 0), angle=0):
    ang = radians(angle)
    matrix = np.array([[1, 0, 0, 0],
                       [0, cos(ang), -sin(ang), 0],
                       [0, sin(ang), cos(ang), 0],
                       [0, 0, 0, 1]])
    return matmul(a, matrix)


def rotateY(a=Vector3(0, 0, 0), angle=0):
    ang = radians(angle)
    matrix = np.array([[cos(ang), 0, sin(ang), 0],
                       [0, 1, 0, 0],
                       [-sin(ang), 0, cos(ang), 0],
                       [0, 0, 0, 1]])
    return matmul(a, matrix)


def rotateZ(a=Vector3(0, 0, 0), angle=0):
    ang = radians(angle)
    matrix = np.array([[cos(ang), -sin(ang), 0, 0],
                       [sin(ang), cos(ang), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    return matmul(a, matrix)


def project3Dto2D(a=Vector3(0, 0, 0), matrix=[]):

    return matmul(a, matrix)


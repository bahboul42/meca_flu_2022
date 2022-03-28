import numpy as np


def circu(u, v, x, y):

    circ = np.zeros(len(x))

    for i in range(0, len(x) - 1):
        if y[i] != y[i + 1]:
            circ[i] = (y[i + 1] - y[i]) * ((v[i + 1] + v[i]) / 2)
        else:
            circ[i] = (x[i + 1] - x[i]) * ((u[i + 1] + u[i]) / 2)

    c = sum(circ)

    return c


def getCircu(dom, u, v, h):
    c = 0
    return c

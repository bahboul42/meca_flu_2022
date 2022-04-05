import numpy as np


def pressure(dom, s, rho):
    row = np.size(dom, 0)
    col = np.size(dom, 1)

    p = np.zeros((row, col))
    p[:] = np.nan

    g = 9.81
    c = 0
    s = np.square(s)

    for i in range(0, row - 1):
        for j in range(0, col - 1):
            if dom[i, j] != 0:
                p[i, j] = rho * g * (c - (s[i, j] / (2 * g)))
    return p

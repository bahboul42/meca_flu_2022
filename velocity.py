import numpy as np

from meca_flu_2022.deriv import deriv


def velocity(psi, dom, h):
    row = np.size(dom, 0)
    col = np.size(dom, 1)
    u = np.zeros((row, col))
    v = np.zeros((row, col))
    s = np.zeros((row, col))
    u[:] = np.nan
    v[:] = np.nan
    s[:] = np.nan

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if dom[i, j] != 0:
                u[i, j] = deriv(psi[i, j - 1], psi[i, j], psi[i, j + 1], dom[i, j - 1], dom[i, j], dom[i, j + 1], h)
                v[i, j] = -deriv(psi[i - 1, j], psi[i, j], psi[i + 1, j], dom[i - 1, j], dom[i, j], dom[i + 1, j], h)
                s[i, j] = np.sqrt((u[i, j])*(u[i, j]) + v[i, j]*v[i, j])
    return u, v, s


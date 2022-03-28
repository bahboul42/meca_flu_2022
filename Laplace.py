import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve as slv

from meca_flu_2022.getCoeff import getCoeff


def solver(dom, num, cl):
    row = np.size(num, 0)
    col = np.size(num, 1)

    n = np.count_nonzero(dom)

    b = np.ones(n)
    lap = np.zeros((n, n))

    # Laplace
    for i in range(0, row - 1):
        for k in range(0, col - 1):
            if num[i][k] > 0:
                j, a, b_i = getCoeff(num[i - 1, k], num[i + 1, k], num[i, k - 1], num[i, k + 1], num[i, k], dom[i, k],
                                     cl[i, k])
                b[int((num[i, k] - 1))] = b_i
                lap[(num[i, k] - 1).astype(np.int32), (j - 1).astype(np.int32)] = a

    lap = sparse.csc_matrix(lap)

    # System solver
    x = slv(lap, b)
    psi = np.zeros((row, col))
    psi[:] = np.nan

    for i in range(0, row - 1):
        for k in range(0, col - 1):
            if num[i, k] != 0:
                psi[i, k] = x[(num[i, k] - 1).astype(np.int32)]

    return psi

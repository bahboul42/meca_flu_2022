import numpy as np


def computecl(dom, h, Qin, f):

    row = np.size(dom, 0)
    col = np.size(dom, 1)

    len_in = 0
    lens_in = []
    k = 1

    lens_in[1] = 0

    for j in range(2, col):
        if dom[2, j] == 2:
            len_in = len_in + 1
            lens_in[k + 1] = k * h
            k = k + 1

    nodes_in = len_in
    len_in = len_in * h - h
    U_in = Qin / len_in

    len_out = 0
    lens_out = []
    k = 1

    lens_out[1] = 0

    for j in range(2, col):
        if dom[201, j] == 2:
            len_out = len_out + 1
            lens_out[k + 1] = k * h
            k = k + 1

    nodes_out = len_out
    len_out = len_out * h - h
    U_out = Qin / len_out

    CL = np.zeros((row, col))
    CL[:] = np.nan

    for i in range(1, row):
        for j in range(1, col):
            if dom[i, j] == 0 or dom[i, j] == 1:
                CL[i, j] = 0

    k = 1
    i = 2

    for j in range(2, col):
        if dom[i, j] == 2:
            if k <= nodes_in:
                CL[i, j] = (Qin / len_in) * lens_in[k]
                k = k + 1

    CL[2:22, 14] = CL[2, 14]
    CL[2:22, 39] = CL[2, 39]

    CL[22, 2: 14] = CL[22, 14]
    CL[22, 39: 51] = CL[22, 39]

    CL[22: 181, 2] = CL[22, 2]
    CL[22: 181, 51] = CL[22, 51]

    CL[181, 2: 19] = CL[181, 2]
    CL[181, 34: 51] = CL[181, 51]

    CL[181: 201, 19] = CL[181, 19]
    CL[181: 201, 34] = CL[181, 34]

    k = 1
    i = 201

    for j in range(1, col):
        if dom[i, j] == 2:
            if k <= nodes_out:
                CL[i, j] = (Qin / len_out) * lens_out[k]
                k = k + 1

    if f > 0:
        C = 0
        cl = f * Qin + C
        CL[36: 108, 11: 42] = cl
        CL[37: 107, 12: 41] = 0

    return cl

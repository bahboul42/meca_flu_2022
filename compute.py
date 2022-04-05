import numpy as np


def computecl(dom, h, Qin, f):
    row = np.size(dom, 0)
    col = np.size(dom, 1)

    k = 1
    foo = 1

    intake = []
    outtake = []

    intake.append(0)
    outtake.append(0)

    for j in range(1, col - 1):
        if dom[1, j] == 2:
            intake.append(k * h)
            k = k + 1
        if dom[200, j] == 2:
            outtake.append(foo * h)
            foo = foo + 1

    intake_len = len(intake) * h - h
    outtake_len = len(outtake) * h - h

    CL = np.zeros((row, col))
    CL[:] = np.nan

    for i in range(np.size(dom, 0)):
        for j in range(np.size(dom, 1)):
            if dom[i, j] == 0 or dom[i, j] == 1:
                CL[i, j] = 0

    for j in range(1, col - 1):
        if dom[1, j] == 2 and len(intake) - 1 > 0:
            CL[1, j] = (Qin / intake_len) * intake.pop(0)

        if dom[200, j] == 2 and len(outtake) - 1 > 0:
            CL[200, j] = (Qin / outtake_len) * outtake.pop(0)

    CL[1:21, 13] = CL[1, 13]
    CL[1:21, 38] = CL[1, 38]

    CL[21, 1: 14] = CL[20, 13]
    CL[21, 38: 51] = CL[20, 38]

    CL[21: 181, 1] = CL[21, 1]
    CL[21: 181, 50] = CL[21, 50]

    CL[180, 1: 19] = CL[180, 1]
    CL[180, 33: 51] = CL[180, 50]

    CL[180: 201, 18] = CL[180, 18]
    CL[180: 201, 33] = CL[180, 33]

    if f > 0:
        cl = f * Qin
        CL[35: 108, 10: 42] = cl
        CL[36: 107, 10: 41] = 0

    return CL


def computecircu(dom, u, v, h):
    c = 0
    return c


def computeforce(dom, p, Qin):
    fx, fy = 0, 0
    return fx, fy

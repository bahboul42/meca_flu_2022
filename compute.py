import math

import numpy as np

from meca_flu_2022.circu import circu
from meca_flu_2022.force import force


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
        CL[36: 107, 11: 41] = 0

    return CL


def computecircu(dom, u, v, h):
    x, y = [], []

    x.extend(np.arange(1, 21, 1))
    x.extend(np.ones(13) * 21)
    x.extend(np.arange(22, 180))
    x.extend(np.ones(18) * 180)
    x.extend(np.arange(181, 200))
    x.extend(np.ones(16) * 200)
    x.extend(np.arange(199, 178, -1))
    x.extend(np.ones(18) * 180)
    x.extend(np.arange(179, 21, -1))
    x.extend(np.ones(13) * 21)
    x.extend(np.arange(20, 0, -1))
    x.extend(np.ones(26) * 1)

    y.extend(np.ones(20) * 13)
    y.extend(np.arange(13, 0, -1))
    y.extend(np.ones(158) * 1)
    y.extend(np.arange(1, 19))
    y.extend(np.ones(19) * 18)
    y.extend(np.arange(18, 34))
    y.extend(np.ones(21) * 33)
    y.extend(np.arange(33, 51))
    y.extend(np.ones(158) * 50)
    y.extend(np.arange(50, 37, -1))
    y.extend(np.ones(20) * 38)
    y.extend(np.arange(38, 12, -1))

    U, V = np.zeros(len(x)), np.zeros(len(x))

    for i in range(len(x) - 1):
        U[i] = u[int(x[i]), int(y[i])]
        V[i] = v[int(x[i]), int(y[i])]

    return h * circu(U, V, x, y)


def computeforce(dom, p, Qin):
    x = np.arange(35, 108, 1, dtype=int)
    y1 = np.ones(73, dtype=int)
    y1[:] *= 10
    y2 = np.ones(73, dtype=int)
    y2[:] *= 41

    y = np.arange(10, 42, 1, dtype=int)
    x1 = np.ones(32, dtype=int)
    x1[:] = 35
    x2 = np.ones(32, dtype=int)
    x2[:] = 107

    portancey1, portancey2 = np.zeros(len(x)), np.zeros(len(x))
    for i in range(len(x) - 1):
        portancey1[i] = p[x[i], y1[i]]
        portancey2[i] = p[x[i], y2[i]]

    portancex1, portancex2 = np.zeros(len(y)), np.zeros(len(y))
    for i in range(len(y) - 1):
        portancex1[i] = p[x1[i], y[i]]
        portancex2[i] = p[x2[i], y[i]]

    fy1, foo = force(portancey1, x, y1)
    fy2, foo = force(portancey2, x, y2)

    foo, fx1 = force(portancex1, x1, y)
    foo, fx2 = force(portancex2, x2, y)

    fx = (fx1 - fx2) * np.sign(Qin)
    fx = math.copysign(fx, Qin)

    fy = fy1 - fy2

    return fx, fy

    # for i in range(0, 20):
    #     x[i] = i + 1
    #     y[i] = 13
    #
    # incr = 13
    # for i in range(20, 33):
    #     x[i] = 21
    #     y[i] = incr
    #     incr -= 1
    #
    # incr = 21
    # for i in range(33, 193):
    #     x[i] = incr
    #     incr += 1
    #     y[i] = 1
    #
    # incr = 1
    # for i in range(193, 211):
    #     x[i] = 180
    #     y[i] = incr
    #     incr += 1
    #
    # incr = 180
    # for i in range(211, 232):
    #     x[i] = incr
    #     incr += 1
    #     y[i] = 18
    #
    # incr = 18
    # for i in range(232, 248):
    #     x[i] = 200
    #     y[i] = incr
    #     incr += 1
    #
    # incr = 200
    # for i in range(248, 268):
    #     x[i] = incr
    #     incr -= 1
    #     y[i] = 33
    #
    # incr = 33
    # for i in range(269, 287):
    #     x[i] = 187
    #     y[i] = incr
    #     incr += 1
    #
    # incr = 180
    # for i in range(287, 447):
    #     x[i] = incr
    #     incr -= 1
    #     y[i] = 50
    #
    # incr = 50
    # for i in range(447, 460):
    #     x[i] = 21
    #     y[i] = incr
    #     incr -= 1
    #
    # incr = 21
    # for i in range(460, 480):
    #     x[i] = incr
    #     incr -= 1
    #     y[i] = 38
    #
    # incr = 38
    # for i in range(480, 506):
    #     x[i] = 1
    #     y[i] = incr
    #     incr -= 1

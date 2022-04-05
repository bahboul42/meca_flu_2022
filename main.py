import numpy as np
import matplotlib.pyplot as plt
from meca_flu_2022 import Laplace
import meca_flu_2022.velocity as vel
from meca_flu_2022.compute import computecl, computecircu, computeforce
from meca_flu_2022.pressure import pressure

if __name__ == "__main__":

    case = 4
    rho = 1000
    x_gp = 2
    y_gp = 2
    Qin = (10 * x_gp + 5 * y_gp) * (10 ** -3)
    p = np.zeros((2, 2))
    p[:] = np.nan

    if case == 1:
        dom = np.loadtxt('1-dom.txt', delimiter='\t')
        num = np.loadtxt('1-num.txt', delimiter='\t')
        h = 0.5
        cl = np.loadtxt('1-cl.txt', delimiter='\t')

    elif case == 2:
        dom = np.loadtxt('2-dom.txt', delimiter='\t')
        num = np.loadtxt('2-num.txt', delimiter='\t')
        h = 0.01
        F = -1
        cl = computecl(dom, h, Qin, F)

    elif case == 3:
        dom = np.loadtxt('2-dom.txt', delimiter='\t')
        num = np.loadtxt('2-num.txt', delimiter='\t')
        h = 0.01
        F = -1
        Qin = -Qin
        cl = computecl(dom, h, Qin, F)

    elif case == 4:
        dom = np.loadtxt('3-dom.txt', delimiter='\t')
        num = np.loadtxt('3-num.txt', delimiter='\t')
        h = 0.01
        F = 0.5
        cl = computecl(dom, h, Qin, F)

    else:
        dom = np.loadtxt('3-dom.txt', delimiter='\t')
        num = np.loadtxt('3-num.txt', delimiter='\t')
        h = 0.01
        F = 15 + 0.3 * 22
        cl = computecl(dom, h, Qin, F)

    psi = Laplace.solver(dom, num, cl)
    u, v, s = vel.velocity(psi, dom, h)

    if case > 1:
        p = pressure(dom, s, rho)
        c = computecircu(dom, u, v, h)
        fx, fy = computeforce(dom, p, Qin)

        u = u.T
        v = v.T
        s = s.T
        p = p.T
        psi = psi.T

    fig, axs = plt.subplots(3, 2, dpi=250)

    fig.suptitle(case)

    axs[0, 0].pcolor(u)
    axs[0, 0].set_title('Horizontal Velocity')

    axs[1, 0].pcolor(v)
    axs[1, 0].set_title('Vertical Velocity')

    axs[2, 0].pcolor(s)
    axs[2, 0].set_title('Mean Velocity')

    axs[0, 1].quiver(u, v)
    axs[0, 1].set_title('Velocity Field')

    if case > 1:
        x = np.arange(1, 203)
        y = np.arange(1, 53)
    else:
        x = np.arange(1, 6)
        y = np.arange(1, 6)

    X, Y = np.meshgrid(x, y, indexing='xy', sparse=False)
    u = np.array(u)
    v = np.array(v)

    axs[1, 1].pcolor(psi)
    axs[1, 1].streamplot(X, Y, u, v, density=1, linewidth=.10, arrowsize=.5, arrowstyle='Fancy')
    axs[1, 1].set_title('Stream-function')

    axs[2, 1].pcolor(p)
    axs[2, 1].set_title('Pressure')

    fig.tight_layout()
    plt.savefig("test.svg")

    plt.show()

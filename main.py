#from solveLaplace import solveLaplace
import numpy as np

def getCL(dom, h, Qin, coef, F):
    pass


if __name__ == "__main__":
    coef = 1
    rho = 1000
    Qin = 55 * 10 ^ -3

    if coef == 1:
        dom = np.loadtxt('1-dom.txt', delimiter='\t')
        num = np.loadtxt('1-num.txt', delimiter='\t')
        h = 0.5
        F = -1
        cl = getCL(dom, h, Qin, coef, F)

    elif coef == 2:
        dom = np.loadtxt('2-dom.txt', delimiter='\t')
        num = np.loadtxt('2-num.txt', delimiter='\t')
        h = 0.01
        F = -1
        cl = getCL(dom, h, Qin, coef, F)
    elif coef == 3:
        dom = np.loadtxt('2-dom.txt', delimiter='\t')
        num = np.loadtxt('2-num.txt', delimiter='\t')
        h = 0.01
        F = -1
        Qin = -Qin
        cl = getCL(dom, h, Qin, coef, F)
    elif coef == 4:
        dom = np.loadtxt('3-dom.txt', delimiter='\t')
        num = np.loadtxt('3-num.txt', delimiter='\t')
        h = 0.01
        F = 0.5
        cl = getCL(dom, h, Qin, coef, F);
    else:
        dom = np.loadtxt('3-dom.txt', delimiter='\t')
        num = np.loadtxt('3-num.txt', delimiter='\t')
        h = 0.01
        F = 0.207
        cl = getCL(dom, h, Qin, coef, F)

    psi = solveLaplace(dom, num, cl)

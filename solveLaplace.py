import numpy as np
from scipy import sparse
import scipy.sparse.linalg.solve as slv
from getCoeff import getCoeff


def solveLaplace(dom, num, cl):
    
    row = np.size(num, 0)
    column = np.size(num, 1)
    
    n = np.count_nonzero(dom)
    
    b = np.ones(n)
    Laplacian = sparse.csc_matrix(row, column)

    #Laplace  
    for l in range(1, row):
        for k in range(1, column):
            if num[l][k] > 0:
                j, a, b_i = getCoeff(num(l-1,k), num(l+1,k), num(l,k-1), num(l,k+1), num(l,k), dom(l,k), cl(l,k))
                b(num(l,k),1) = b_i
                Laplacian(num(l,k),j(:,1)) = a(:,1)

    #System solver
    X = slv(Laplacian,b)
    psi = np.empty((row, column)) 
    psi[:] = np.nan

    for l in range(1, row):
        for k in range(1, column):
            if num[l][k] != 0:
                psi[l][k] = X[num[l][k]]

    return psi
import numpy as np
import scypi.sparse.linalg

def solveLaplace(dom,num,cl):
    
    row = np.size(num, 0)
    column = np.size(num, 1)
    
    n = np.count_nonzero(dom)
    
    b = np.ones(n)
    L = sparse.csr_matrix()

    return psi
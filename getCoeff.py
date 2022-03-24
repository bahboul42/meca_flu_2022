import numpy as np

def getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent):
    
    j = 0
    b = 0
    
    if type_cent == 1:
        a = np.array([1, 1, 1, 1, -4], ndmin = 2).T
        j = np.array([num_left, num_right, num_down, num_up, num_cent], ndmin = 2).T
        
    elif type_cent == 2:
        b = cl_cent;
        a = 1;
        j = num_cent;

    else:
        a = 0

    return j, a, b
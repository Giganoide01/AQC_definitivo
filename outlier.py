import numpy as np
from scipy import misc


def outlier(a):
    b  = np. mean(a)
    dp = np.std(a)
    j = 0
    cont = 0
    mais = b + 3*dp
    menos = b - 3*dp
    
    for i in range(0, len(a)):
        f = a[j]
        j = j + 1

        if f > mais:
            cont = cont+1
        elif f < menos:
            cont = cont + 1
    return cont 
    

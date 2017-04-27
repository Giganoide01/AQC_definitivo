import random
import numpy as np

def spearman(x,y):
    a = np.argsort(x)
    b = np.argsort(y)

    aa = np.argsort(a)
    bb = np.argsort(b)
    
    rank1 = aa + 1.0
    rank2 = bb + 1.0

    d = rank1 - rank2
    d2 = d**2
    soma = np.sum(d2)

    t = len(x)
    coef  = 1 - ((6.0 *soma)/(t**3 - t))
    return coef

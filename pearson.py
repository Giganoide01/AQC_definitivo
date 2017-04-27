import random
import numpy as np

def pearson(x,y):
    
    xb = np.mean(x)
    yb = np.mean(y)

    x1 = xb - x
    y1 = yb - y

    num = np.sum(x1*y1)

    b = np.sum(x1**2)
    c = np.sum(y1**2)
    d = c*b
    den = d**0.5

    r = num/den

    return r

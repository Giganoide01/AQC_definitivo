import numpy as np
import random
import matplotlib.pyplot as plt

def regressaoLinear(x,y):
    

    XiYi = np.sum(x*y)
    Xi2 = np.sum(x**2)

    Ym =  np.mean(y)
    Xm = np.mean(x)

    n = len(x)
    c = n*Xm*Ym

    b = (XiYi - c)/ (Xi2 - n*(Xm**2))

    a = Ym - b*Xm
    y2 = b*x + a

    return b, a


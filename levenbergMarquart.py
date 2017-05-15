from numpy import arange, sin, pi, random, array
import numpy as np
import matplotlib.pyplot as plt

def levenberg(x, y, metrica):
    

    def residuals(p, y, x):
        b1, b2, b3, b4, b5 = p
        err = y - (b1*(0.5 - 1/(1+np.exp(b2*(x -b3)))) + b4*x +b5)
        return err

    def peval(x, p):
        return p[0]*(0.5 - 1/(1+np.exp(p[1]*(x -p[2])))) + p[3]*x +p[4]
    
    if (metrica == 1):
        p0 = [-6, 1.3, 3, 0.4, 3]
    if (metrica == 2):
        p0 = [-9, 0.67, -1, 0.57, 3]
    if (metrica == 3):
        p0 = [-5, 1.3, 1, 0.28, 13]
    if (metrica == 4):
        p0 = [-6, 2.6, 1, 0.4, 3]
    if (metrica == 5):
        p0 = [-21, 0.5, 10, -0.25, 19]
    if (metrica == 6):
        p0 = [-6, 2.6, 1, 0.4, 3]
    if (metrica == 7):
        p0 = [-21, 0.5, 10, -0.25, 19]
    if (metrica == 8):
        p0 = [-6, 2.6, 1, 0.4, 3]


    from scipy.optimize import leastsq
    plsq = leastsq(residuals, p0, args=(y, x))
    
    t = peval(np.sort(x), plsq[0])
    plt.plot(np.sort(x), t,x,y,'o')
    plt.title('Otimizacao')
    return x, t, y, plsq[0]



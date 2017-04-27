import scipy.ndimage
import matplotlib.pyplot as plt
from numpy.ma.core import exp
from scipy.constants.constants import pi
from scipy import signal,misc, ndimage
import matplotlib.pyplot as plt
import scipy
import numpy as np

def psnr(l, k):

    # RFZ: o cálculo de n deve ser parametrizado, para imagens de diferentes dimensões
    n = float(len(l)*len(l[0])) #len(l)  
    L = 2**8 - 1
    aa = (l - k)**2
    ba = np.sum(aa)
    MSE1 = (1/n)*ba

    if MSE1==0:
        PSNRaleat = float('inf')
    else:
        PSNRaleat = 10.0 * np.log10(((L**2.0)/MSE1))
    
    return PSNRaleat

def msim(img_mat_1, img_mat_2):

    # RFZ: # L e window dever ser passados como parâmetros da função. Valores default devem ser fornecidos
    # Valores default devem ser fornecidos
    std =3
    L = 6*std +1 # comprimento do filtro
    window = signal.gaussian(L, std) # vetor Gaussiano unidimensional
    #x = misc.lena()                  # imagem de entrada

    # kernel 2d (usando fft)
    w = window.reshape((L,1))
    wt = np.transpose(w)
    h = w * wt
    soma = np.sum(h)
    h = h/soma
    
    #print(h.shape)

    #convertere para float
    img_mat_1=img_mat_1.astype(np.float)
    img_mat_2=img_mat_2.astype(np.float)

    #Squares of input matrices
    img_mat_1_sq=img_mat_1**2
    img_mat_2_sq=img_mat_2**2
    img_mat_12=img_mat_1*img_mat_2
    
    #Means obtained by Gaussian filtering of inputs
    img_mat_mu_1=scipy.ndimage.filters.convolve(img_mat_1,h)
    img_mat_mu_2=scipy.ndimage.filters.convolve(img_mat_2,h)
        
    #Squares of means
    img_mat_mu_1_sq=img_mat_mu_1**2
    img_mat_mu_2_sq=img_mat_mu_2**2
    img_mat_mu_12=img_mat_mu_1*img_mat_mu_2
    
    #Variances obtained by Gaussian filtering of inputs' squares
    img_mat_sigma_1_sq=scipy.ndimage.filters.convolve(img_mat_1_sq,h)
    img_mat_sigma_2_sq=scipy.ndimage.filters.convolve(img_mat_2_sq,h)
    
    #Covariance
    img_mat_sigma_12=scipy.ndimage.filters.convolve(img_mat_12,h)

    #Centered squares of variances
    img_mat_sigma_1_sq=img_mat_sigma_1_sq-img_mat_mu_1_sq
    img_mat_sigma_2_sq=img_mat_sigma_2_sq-img_mat_mu_2_sq
    img_mat_sigma_12=img_mat_sigma_12-img_mat_mu_12;

    
    #c1/c2 constants
    #First use: manual fitting
    c_1=6.5025
    c_2=58.5225
    
    #Second use: change k1,k2 & c1,c2 depend on L (width of color map)
    l=255
    k_1=0.01
    c_1=(k_1*l)**2
    k_2=0.03
    c_2=(k_2*l)**2
    
    #Numerator of SSIM
    num_ssim=(2*img_mat_mu_12+c_1)*(2*img_mat_sigma_12+c_2)
    #Denominator of SSIM
    den_ssim=(img_mat_mu_1_sq+img_mat_mu_2_sq+c_1)*\
    (img_mat_sigma_1_sq+img_mat_sigma_2_sq+c_2)
    #SSIM
    ssim_map=num_ssim/den_ssim
    #print ssim_map
    index=np.average(ssim_map)
    return index
'''
def mae(a, b):
    n = float(len(a)*len(a[0]))
    mae = np.sum(np.abs((a-b)))*(1/n)
    return mae
'''
def mse(a, b):
    n = float(len(a)*len(a[0]))
    mse = np.sum(np.abs((a-b)))*(1/n)
    return mse

'''
def snrNo(a):
    snr = (np.mean(a))/(np.std(a))
    return snr
def snrFull(l,k):
    N = len(l)*len(l[0])
    mse = np.sum(np.abs((k-l)))*(1/N)
    snr = 10*np.log10(np.sum((l**2))/(N*mse))
    return snr
def cc(l,k):
    cc = pearson.pearson(l,k)
    return cc
'''




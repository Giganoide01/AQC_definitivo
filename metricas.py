import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
#import funcaoPM
import metrica
import metrikz

#import ssim


def metricas (orig, test):

    subjectscores = open('jpeginfo.txt', 'r')
    conteudo_texto1 = subjectscores.read()
    aa = conteudo_texto1.split('\n')                
    cc = aa[:-1]                                       
    subjectscores.close()
    

    for i in xrange(0, len(cc)):
        a = aa[i].split()
        dirOrig = orig
        imag = a[0]
        e =  dirOrig+'/'+imag
        ref = plt.imread(e)
        dirTest = test
        imag = a[1]
        ee = dirTest + '/'+imag
        teste = plt.imread(ee)
        
        psrn = metrica.psnr(ref, teste)
        
        mse  = metrica.mse(ref, teste)
        
        j = 0
        a = ref[:,:,j]
        b = teste[:,:,j]
        ssim0 = metrica.msim(a, b)

        j = j+1
        a = ref[:,:,j]
        b = teste[:,:,j]
        ssim1 = metrica.msim(a, b)

        j = j+1
        a = ref[:,:,j]
        b = teste[:,:,j]
        ssim2 = metrica.msim(a, b)
        ssim = (ssim0 + ssim1 + ssim2)/3

        uqi = metrikz.uqi(ref, teste)

        snr = metrikz.snr(ref, teste)

        pbvif = metrikz.pbvif(ref, teste)

        nqm = metrikz.nqm(ref, teste)

        rmse = metrikz.rmse(ref, teste)
        
        psrn2 = str(psrn)
        ssim2 = str(ssim)
        mse2 = str(mse)
        uqi2 = str(uqi)
        snr2 = str(snr)
        pbvif2 = str(pbvif)
        nqm2 = str(nqm)
        rmse2 = str(rmse)
        f = open('metricas.txt','a')
        f.write('img' + str(i+1) + ';' + psrn2 + ';' + ssim2 + ';' + mse2 + ';' + uqi2 + ';' + snr2 + ';' + pbvif2 + ';' + nqm2 + ';' + rmse2 + '\n' )
        f.close()
        


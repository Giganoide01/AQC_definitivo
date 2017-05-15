import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pearson
import spearman
import outlier
import regressaoLinear
import levenbergMarquart
import anova
import eliminador_outlier

def avaliacao(metrica, arq):
    # abrir arquivo de avaliacoes objetivas (metricas)
    arquivo = open('metricas.txt', 'r')
    conteudo_texto = arquivo.read()
    a = conteudo_texto.split('\n')                 
    c = a[:-1]
    arquivo.close()    
    
    # abrir aquivo de avaliacoes subjetivas
    subjectscores = open(arq, 'r')                          
    conteudo_texto1 = subjectscores.read()          
    aa = conteudo_texto1.split('\n')              
    cc = aa[:-1]        
    subjectscores.close()
    
    # abrir arquivo de avaliacoes objetivas (metricas)
    arquivo2 = open('jpeginfo.txt', 'r')
    conteudo_texto2 = arquivo2.read()
    aaa = conteudo_texto2.split('\n')                 
    ccc = aaa[:-1]
    arquivo2.close()

    #inicializacao das variaveis
    x = np.array([])
    y = np.array([])
    x0 = np.array([])
    y0 = np.array([])
    l = np.array([])
    total_pontos = 0
    ref = ''
    ab = ''
    
#plot METRICA X DMOS
    for i in xrange(0, len(cc)):
        w = aa[i].split('\t')
        for line in ccc:
            if w[0] in line:
                #print line 
                cond  = line.split()
                #print cond[2]
                if cond[2] == '0':
                    ab = cond[1]
        #q = len(w)                                  
        for line in cc:
            if ab in line:
               w0 = line

               
        w1 = w0.split('\t')
        ww = w[2:(len(w))]
        ww1 = w1[2:(len(w))]
        #print ww1
        total_pontos = len(ww) + total_pontos
        b = c[i].split(';')                         
        psnr = b[metrica]
        #substituir numeracao por eliminacao de valores nulos
        h = np.asarray([e for e in ww if (e != str(''))])
        h1 = np.asarray([e for e in ww1 if (e != str(''))])
        
        #t = h.astype(np.float)
        v2 = np.mean(h1.astype(np.float))
        v1 = np.mean(h.astype(np.float))
        v=v2-v1
        if (psnr !=str('inf')):
            x0 = np.insert(x0,0,psnr)         
            y0 = np.insert(y0,0,v)           
        r = float(psnr)                     
        #p = (len(w))-1.0
        
        #outlier
        out = outlier.outlier(eliminador_outlier.reject_outliers(y0))                   
        l = np.append(l, out)

    u = np.median(y0)
    s = np.std(y0) 
    for j in xrange(0, len(y0)):
        if (u - 2 * s < y0[j] < u + 2 * s):
            y = np.insert(y,0,y0[j])
            x = np.insert(x,0,x0[j])

    razao_outliers = np.sum(l)/total_pontos
    coeficiente_spearman = spearman.spearman(x,y)   #spearman/s = stats.spearmanr(x,y)
    coeficiente_pearson = pearson.pearson(x,y)      #pearson/p = stats.pearsonr(x,y)
    coeficiente_anova_F, coeficiente_anova_p, relacao_anova = anova.anova(x,y)
    
    a, b = regressaoLinear.regressaoLinear(x,y)     #regressao linear
    x, t, y, v = levenbergMarquart.levenberg(x,y,metrica)   #funcao logistica
    linear = '(' + str(a) + ')*x + (' + str(b) + ')'
    logistica = '(' + str(v[0])+ ') * (' + str(0.5) + '-(' + str(v[1]) + ')/(exp(' + str(v[1]) + '*(x-(' + str(v[2])+ '))))) + (' + str(v[3])+ ') * x+(' + str(v[4]) + ')'

    return razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear




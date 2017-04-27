import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pearson
import spearman
import outlier
import regressaoLinear
import levenbergMarquart
import anova

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
        h = np.asarray(ww[0:12])          #substituir numeracao por eliminacao de valores nulos          
        h1 = np.asarray(ww1[0:12])
        #t = h.astype(np.float)
        v2 = np.mean(h1.astype(np.float))
        v1 = np.mean(h.astype(np.float))
        v=v2-v1
        if (psnr !=str('inf')):
            x = np.insert(x,0,psnr)         
            y = np.insert(y,0,v1)           
        r = float(psnr)                     
        #p = (len(w))-1.0                   
                                 
        #outlier
        out = outlier.outlier(h.astype(np.float))                   
        l = np.append(l, out)                       

    razao_outliers = np.sum(l)/total_pontos
    coeficiente_spearman = spearman.spearman(x,y)   #spearman/s = stats.spearmanr(x,y)
    coeficiente_pearson = pearson.pearson(x,y)      #pearson/p = stats.pearsonr(x,y)
    coeficiente_anova_F, coeficiente_anova_p, relacao_anova = anova.anova(x,y)

    
    
    
    a, b = regressaoLinear.regressaoLinear(x,y)     #regressao linear
    x, t, y, v = levenbergMarquart.levenberg(x,y)   #funcao logistica
    linear = '(' + str(a) + ')*x + (' + str(b) + ')'
    logistica = '(' + str(v[0])+ ') * (' + str(0.5) + '-(' + str(v[1]) + ')/(exp(' + str(v[1]) + '*(x-(' + str(v[2])+ '))))) + (' + str(v[3])+ ') * x+(' + str(v[4]) + ')'

    return razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear




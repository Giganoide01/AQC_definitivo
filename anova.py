from  scipy import stats

def anova(x,y):
    
    F, p = stats.f_oneway(x,y)
    
    if p<0.05:
        relacao = 'Os dados nao possuem a mesma media'
    else:
        relacao = 'Os dados possuem a mesma media'
        
    return F, p, relacao

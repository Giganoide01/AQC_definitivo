import numpy as np
import metricas as p
import avaliacao

def aqv(orig, teste, arquivo, psnr, mse, msim, uqi, snr, pbvif, nqm, rmse, lin, log, pearson, spearman, out, anova):
    f = open('Avaliacao de Desempenho de Metricas de Qualidade Visual.txt', 'a')
    a = p.metricas(orig, teste)
    if psnr:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(1, arquivo)
        f.write('PSNR' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if mse:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(2, arquivo)
        f.write('MSE' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if msim:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(3, arquivo)
        f.write('MSIM' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if uqi:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(4, arquivo)
        f.write('UQI' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if snr:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(5, arquivo)
        f.write('SNR' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if pbvif:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(6, arquivo)
        f.write('PVIF' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if nqm:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(7, arquivo)
        f.write('NQM' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if rmse:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear = avaliacao.avaliacao(8, arquivo)
        f.write('RMSE' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if anova:
            f.write('Coeficientes da Analise de variancia (F,p): ' + str(coeficiente_anova_F) + ', ' + str(coeficiente_anova_p) + '; ' + str(relacao_anova) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    f.close()

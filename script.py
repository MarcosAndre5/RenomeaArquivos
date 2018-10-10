# -*- coding: utf-8 -*-
'''
27/09/18 - Criação.
09/10/18 - Atualizado para não renomear os arquivos caso algum deles já esteja com seu nome renomeado.
Marcos.
Versão do Python: 3.7.
'''
import os
pre = 'iedf200.bco001.'
pos = '.xjucern.c093757'
cont = 0
for i in os.listdir('.'):
    if i.startswith('iedf200.bco001.'):
        cont += 1       
if(cont == 0):
    for i in os.listdir('.'):
        if i.startswith('IED'):
            os.rename(i, i[12:])
    [os.rename(i, pre + str(i)) for i in os.listdir('.')
     if ((not i.startswith('.')) and i.endswith('.ret'))]
    for i in os.listdir('.'):
        if i.startswith('ied'):
            os.rename(i, i[:-3])
    for i in os.listdir('.'):
        if i.startswith('ied'):
            os.rename(i, i + pos)

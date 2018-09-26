# -*- coding: utf-8 -*-
import os
import shutil

pre = 'iedf200.bco001.'
pos = '.xjucern.c093757'


for i in os.listdir('.'):
    if i.startswith('IED'):
        os.rename(i, i[12:])

[os.rename(i, 'iedf200.bco001.' + str(i)) for i in os.listdir('.') 
if ((not i.startswith('.')) and i.endswith(".ret"))]

for i in os.listdir('.'):
    if i.startswith('ied'):
        os.rename(i, i[:-3])

for i in os.listdir('.'):
    if i.startswith('ied'):
        os.rename(i, i + pos)


#shutil.copyfile('Users/Suporte/Desktop/deve', os.path.join(arquivo,'Users/Suporte/Desktop/destino')
            
# pre = 'iedf200.bco001.'
# pos = '.xjucern.c093757'

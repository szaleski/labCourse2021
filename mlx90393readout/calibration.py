# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:05:47 2021

@author: Sebastian
"""

import os
import numpy as np
import matplotlib.pyplot as plt



calpath = 'calibrationdata/'

files = os.listdir(calpath)
files = [entry for entry in files if entry[0].isdigit()]
bfields = np.sort(np.array(files, dtype=float))

absfields = np.zeros(len(bfields))
xfields = np.zeros(len(bfields))
yfields = np.zeros(len(bfields))
zfields = np.zeros(len(bfields))


for i, file in enumerate(bfields):
    data = np.loadtxt(calpath+str(int(file)), delimiter=' ' )
    xfields[i], yfields[i], zfields[i], absfields[i] = np.mean(data, axis=0) / 1000 #in mT
    
    with open(calpath+str(int(file))) as f:
        realfield = float(f.readline().split(' ')[1])
        bfields[i] = realfield
        
        
plt.figure('Hallvoltages')
plt.ylabel('Sensor output in V')
plt.xlabel('B-Field in mT')
plt.plot(bfields, absfields, 'o')


# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:15:09 2021

@author: Sebastian
"""

import numpy as np
import matplotlib.pyplot as plt
import os

datapath = 'fieldmapping/'+ ['rectangular_magnet/', 'round_magnet/', 'round_magnet_upright/'][2]
foldercontent = os.listdir(datapath)

xinds = []
yinds = []
xfield = []
yfield = []
zfield = []
absfield = []

for file in foldercontent:
    if file[0].isdigit():
        data = np.loadtxt(datapath+file)
        xind, yind = np.array( file.split('_')[0].split('-'), dtype=int)
        
        newname = f'{xind}-{yind}'
        os.rename(datapath+file, datapath+newname )

for file in foldercontent:
    if file[0].isdigit() or file[0] == '_':
        data = np.loadtxt(datapath+file)
        
        
        xind, yind = np.array( file.split('.')[0].split('-'), dtype=int)
        x, y, z, total = np.mean(data, axis=0)
        
        xinds.append(xind)
        yinds.append(yind)
        
        xfield.append(x)
        yfield.append(y)
        zfield.append(z)
        absfield.append(total)
        
xinds = np.array(xinds)
yinds = np.array(yinds)        

xfield = np.array(xfield)#*-1
yfield = np.array(yfield)
zfield = np.array(zfield)
absfield = np.array(absfield)




#Meshgrid in cm
x, y = np.arange(8, -1, -1), np.arange(0,9,1)

x = x[xinds]
y = y[yinds]


# Plotting Vector Field with QUIVER
plt.figure()
plt.title(datapath[13:-1].replace('_',' '))
plt.quiver(y, x, yfield, xfield, color='g', pivot='middle')
plt.xlabel('horizontal position in cm')
plt.ylabel('vertical position in cm')
  
  
# Show plot with gird
plt.grid()
plt.show()

# plt.figure()
# plt.streamplot(np.arange(0,10), np.linspace(0,1e-2,10), u, v, density=1.4, minlength=0.5, maxlength=5)

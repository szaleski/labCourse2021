# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:53:38 2021

@author: Sebastian
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.optimize import curve_fit




def gerade(x, m, b):
    return x*m+b

def exponential(x, a, b):
    # print(x, a, b)
    return a*np.exp( b*x )


def getDerivative(model, params, x):
    '''
    Bestimmt die Ableitung eines beliebigen Modells. Für model == exponential und
    model == gaussian wird die analytische Lösung verwendet
    '''
    
    if model == exponential:
        return exponential(x, *params)*params[1]
    
    elif model == gerade:
        return params[0]
    
    else:
        print('scipy.misc.derivative was called')
        return derivative(lambda y: model(y, *params), x)


def chi2(func, fitparams, xdata, ydata, yerr, xerr=None ):
    '''
        Bestimmt chi^2 für ein gegebenes Modell mit y-Fehlern und optionalen x-Fehlern
    '''
    
    val = func(xdata, *fitparams)
    if xerr is not None:
        effVar = yerr**2 +  ( getDerivative(func, fitparams, xdata)*xerr )**2
    else:
        effVar = yerr**2
    return np.sum((ydata - val)**2 / effVar)





def fitPlot(model, param, xdata, ydata, yerr, xerr=None, \
            labels= { 'xlabel': 'B-Field in mT', 'ylabel': 'reziprokal ouput voltage in 1/V', \
                     'data': 'Measured Values', 'fitmodel': None, 'chipos': None}):
    '''
    Erzeugt vollen Anpassungsplot mit Residuen und Fehlern.
    Achsenbeschriftungen werden mit dem dictionary labels übergeben. Für die
    notwendigen keywords siehe Code. Das keyword 'chipos' mit beliebigem inhalt 
    triggert das Zeigen des chi/ndof.
    
    Anwendung bereits in gaussAnpassung und expFit.

    '''
    
    fig, (ax1, ax2) = plt.subplots(2,1, sharex='col', figsize=(10, 8), \
          gridspec_kw={'height_ratios': [4, 1]})
    fig.subplots_adjust(hspace=0.05)
    ax2.set(xlabel = labels['xlabel'], \
            ylabel = r'Residuals')
    ax1.set(ylabel = labels['ylabel'])
    
    if 'title' in labels.keys():
        ax1.set(title= labels['title'])
    
    x = np.linspace(min(xdata), max(xdata), int(1e5))
    
    ax1.errorbar(xdata, ydata, yerr=yerr, xerr=xerr, label=labels['data'], fmt='o', capsize=2)
    ax1.plot(x, model(x, *param), label=labels['fitmodel'])
    
    ax1.legend()
    
    if 'chipos' in labels.keys():
        chiq = chi2(model, param, xdata, ydata, yerr, xerr)
        ndof = len(xdata) - len(param)
        chiqdof = chiq / ndof
        boxtext = '$\chi^2$/dof = %g / %g = %3.2f' % (chiq, ndof, chiqdof)
        xbox=(max(xdata) - min(xdata))*1/100 + min(xdata)
        ybox=(max(ydata) - min(ydata))*5/10 + min(ydata)
        ax1.text(xbox,ybox,boxtext, bbox={'facecolor': 'aqua', 'alpha': 0.8, 'pad': 10})
    
    #Residuenplot
    if type(xerr) == np.ndarray:
        deriv = getDerivative(model, param, xdata)
        res = np.sqrt( yerr**2 + (deriv*xerr)**2 )
    else:
        res = yerr
        
    ax2.errorbar(xdata, ydata - model(xdata, *param), yerr=res, fmt='o', capsize=2)
    ax2.grid()
    plt.show()
    return fig, (ax1, ax2)


calpath = 'calibrationdata1/'

files = os.listdir(calpath)
files = [entry for entry in files if entry[0].isdigit()]
bfields = np.sort(np.array(files, dtype=float))

hallvolts = np.zeros(len(bfields))
ihallvolts = np.zeros(len(bfields))

for i, file in enumerate(bfields):
    data = np.loadtxt(calpath+str(int(file)), delimiter=' ' )
    hallvolts[i], ihallvolts[i] = np.mean(data, axis=0)
    
plt.figure('Hallvoltages')
plt.ylabel('Sensor output in V')
plt.xlabel('B-Field in mT')
plt.plot(bfields, hallvolts, 'o')

plt.figure('inversed Hall Voltages2')
plt.ylabel('reciprocal Sensor Output in 1/V')
plt.xlabel('B-Field in mT')
plt.plot(bfields, ihallvolts, 'o')

# dU = 5/4096
# dihall = dU / (hallvolts*(hallvolts+dU))

# mask = bfields < 150
# bfields, ihallvolts, dihall = bfields[mask], ihallvolts[mask], dihall[mask] 

# popt, pcorr = curve_fit(gerade, bfields, ihallvolts, sigma=dihall)
# fitPlot(gerade, popt, bfields, ihallvolts, dihall)



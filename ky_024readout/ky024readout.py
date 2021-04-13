# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 08:58:15 2021

@author: Sebastian Kock
"""


import serial
import time
import numpy as np
import matplotlib.pyplot as plt



def measure(number, name, datapath = 'calibration data/', save=True):
    '''
    Takes number measurements from arduino and saves the results in the folder
    specified in datapath with filename name
    '''
    global ser
    
    hallvoltages = []      #list with measured voltages in Volt
    
    for c in range(number):
       line = str(ser.readline(), 'utf-8')
       
       splitline = line.split('.')
       if splitline[0].isdigit() and len(splitline)< 3:
           
           hallvoltage = float(line)
           hallvoltages.append(hallvoltage)
       
           print('U={:.4f}V b={:.4f}'.format(hallvoltage, 1/hallvoltage))
       
    hallvoltages = np.array(hallvoltages)
    output = np.stack((hallvoltages, 1 / hallvoltages), axis=1)
        
    if save:
        np.savetxt(datapath+name, output)
    
    return hallvoltages, 1/hallvoltages

def fastEval():
    global ser
    hallvoltages = []
    ihallvoltages = []
        
    try:
             
        while True:
            hallv, ihallv= np.mean(measure(10, 'latest hallvolts', save=True), axis=1)
            hallvoltages.append(np.mean(hallv))
            ihallvoltages.append(np.mean(ihallv))
            
            print('{:.4f}'.format(ihallv))
            time.sleep(0.2)
    except:
        ser.close()
    
    plt.figure('hallvoltage')
    plt.plot(hallvoltages, 'o')
    
    plt.figure('inverse hallvoltage')
    plt.plot(ihallvoltages, 'o')
        



ser = serial.Serial('COM3', 9600)
number = 100      #number of data points to be collected

try:

    while True:
        inputstr = input('For next measurement type in current B-Field in mT:')
        
        measure(number, inputstr)

    # fastEval()    
    ser.close()
                
except KeyboardInterrupt:
    ser.close()
    print('serial connection closed by user')

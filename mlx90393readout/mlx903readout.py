# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:06:09 2021

@author: Sebastian
"""

import serial
import time
import numpy as np
import matplotlib.pyplot as plt



def measure(number, name, datapath = 'calibrationdata/', save=True):
    '''
    Takes number measurements from arduino and saves the results in the folder
    specified in datapath with filename name
    '''
    ser = serial.Serial('COM3', 9600)
    
    hallvoltages = []      #list with measured voltages in Volt
    xvals = []
    yvals = []
    zvals = []
    
    try:
        for c in range(number):
            line = str(ser.readline(), 'utf-8')
           
            splitline = np.array(line.split(' '))
            if len(splitline) == 9:
                X, Y, Z = np.array(splitline[[1,4,7]], dtype=float)
                abs_value = np.sqrt( X**2 + Y**2 + Z**2)
                
                print(line + f'abs: {round(abs_value,4)} uT')
                
                xvals.append(X)
                yvals.append(Y)
                zvals.append(Z)
                hallvoltages.append(abs_value)
              
    except Exception as err:
        ser.close()
        print('Serial connection closed because of ',err)
        
    ser.close()   
    xvals = np.array(xvals)
    yvals = np.array(yvals)
    zvals = np.array(zvals)
    hallvoltages = np.array(hallvoltages)
    
    output = np.stack((xvals, yvals, zvals, hallvoltages), axis=1)
    np.savetxt(datapath+name.split('.')[0], output, header=str(name))
    
    
    
    return #hallvoltages, 1/hallvoltages

def fastEval():
    global ser
    hallvoltages = []
    ihallvoltages = []
        
    try:
             
        while True:
            measure(10, 'latest hallvolts', save=True)
            
            time.sleep(1)
    except:
        pass
        # ser.close()
    
    # plt.figure('hallvoltage')
    # plt.plot(hallvoltages, 'o')
    
    # plt.figure('inverse hallvoltage')
    # plt.plot(ihallvoltages, 'o')
        



# ser = serial.Serial('COM3', 9600)
number = 10      #number of data points to be collected

try:
        while True:
            inputstr = input('For next measurement type in current B-Field in mT:')
            
            measure(number, inputstr)

       
                
except KeyboardInterrupt:
    # ser.close()
    print('serial connection closed by user')
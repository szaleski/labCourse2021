from subprocess import Popen, PIPE, TimeoutExpired
import time
import pandas as pd
import numpy as np


def readPort(streamfile, comname):
    
    line = str(streamfile.readline(), 'utf-8')
    print(f"received from {comname}: %s" % line) # print output from COMreadout.py  
    
    elements = line.split(' ')
    # print(elements)
    if elements[0].isnumeric():
        return np.array(elements, dtype=float)
    else:
        return ''


# call subprocess
# pass the serial object to subprocess
# read out serial port


# HOW TO PASS SERIAL OBJECT HERE to stdin
p1 = Popen(['python', './COMreadout.py', "COM5", "9600"], stdin=PIPE, stdout=PIPE, stderr=PIPE) # read COM1 permanently
p2 = Popen(['python', './COMreadout.py', "COM6", "9600"], stdin=PIPE, stdout=PIPE, stderr=PIPE) # read COM2 permanently


arr1 = np.zeros((0,2))
arr2 = np.zeros((0,2))


try:
    t0 =round(time.time(), 0)
    
    while True:
        P1datapoint = readPort(p1.stdout, 'COM5')
        if type(P1datapoint) != str:
            arr1 = np.concatenate((arr1, P1datapoint[np.newaxis,:2]), axis=0)
        
        P2datapoint = readPort(p2.stdout, 'COM6')
        if type(P2datapoint) != str:
            arr2 = np.concatenate((arr2, P2datapoint[np.newaxis,:]), axis=0)
        
        time.sleep(0.1) 
    
except KeyboardInterrupt:
    t1 = round(time.time(),0) #stop timer

    print('[Keyboard Interrupt] terminating measurement')
    # restbuffer1 = ''
    # if p1.stdout.readable():
    #     print('restbuffer1')
    #     restbuffer1 = p1.stdout.readlines() 
    #     print(restbuffer1)
        
    for i in range(2):
        try:
            arr = [arr1, arr2][i]
            p = [p1, p2][0]
            
            restbuffer = str(p.communicate(timeout=20)[0], 'utf-8')
            print(restbuffer)
        
            for line in restbuffer.split('\n'):
                datapoint = np.array( line.split(' '), dtype=float)
                arr = np.concatenate((arr, datapoint[np.newaxis,:2]), axis=0)
            
        except TimeoutExpired:
            print(f'No further buffer for COM{5+i}')
        # except:
        #     print('[ERROR] an error ocurred during termination. Continuing anyway')

    p1.terminate()
    p2.terminate()

print('saving data...')
p1Data = pd.DataFrame(arr1, columns = ['counts1', 'time1'])
p2Data = pd.DataFrame(arr2, columns = ['counts2', 'time2'])

p1Data[['counts2', 'time2']] = p2Data
p1Data.to_csv('measurement2.csv', sep=';')


rate1 = arr1[-1,0]/(t1-t0) #watch
rate2 = arr2[-1,0]/(t1-t0) #pin

print(f'The final rates are: \nWatch: f={round(rate1, 3)} Hz\tPIN: f={round(rate2, 3)} Hz')
    
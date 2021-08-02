'''
@autor: Sebastian Kock

seperate COM readout programm to use in an own subprocess (see compare.py)
'''

import sys
import serial

with serial.Serial(port=sys.argv[1],baudrate=int(sys.argv[2])) as ser:
    with open(sys.argv[1]+'data.txt', 'w') as file:
        while True:  # The program never ends... will be killed when master is over.

            output = ser.readline() # read output

            file.write(str(output, 'utf-8'))

            sys.stdout.write(str(output, 'utf-8')) # write output to stdout
            sys.stdout.flush()
import serial

with serial.Serial('COM5') as ser:

    while True:
        output = str(ser.readline(), 'utf8')
        print(output)

        #print rate
        splitlist = output.split(' ')

        if len(splitlist) > 2:
            count, time, *_ = splitlist
            if count.isnumeric():
                #this rate is only reliable for longer measurements
                print('current rate ', round(int(count) / float(time), 3), 'Hz' )   


import numpy as np

# data = np.loadtxt('measurement1.csv', delimiter=';', skiprows=2)[:,2]

timestamps = []
with open('measurement1.csv', 'r') as f:
    for line in f:
        element = line.split(';')[4]
        if not element == '' and element[0].isnumeric():
            timestamps.append(float(element))

close = np.array([ (i if timestamps[i+1] - timestamps[i] < 1 else False ) \
    for i in range(len(timestamps)-1) ] )

diffs = np.diff(timestamps)
mindiff = min(diffs)
count = np.sum( close > 0)

print(close, count)
print(diffs, mindiff)



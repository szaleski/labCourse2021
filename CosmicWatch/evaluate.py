import numpy as np

filepath =  './CosmicWatch/measurements/CosmicWatch2_tests/' #'./measurements/PIN-Cosmic_comparison/'#

# data = np.loadtxt('measurement1.csv', delimiter=';', skiprows=2)[:,2]

threshold = 20 #0.02 #s

timestamps = []
with open(filepath+'measurement1.csv', 'r') as f:
    for line in f:
        element = line.split(';')[4]
        if not element == '' and element[0].isnumeric():
            timestamps.append(float(element))

close = np.array([ (i if timestamps[i+1] - timestamps[i] < threshold else False ) \
    for i in range(len(timestamps)-1) ] )

diffs = np.diff(timestamps)
mindiff = min(diffs)
count = np.sum( close > 0)

print(diffs)
print('length of data: ', len(diffs))
print('smallest time difference: ', mindiff, 'ms')
print(f'percentage of events below {threshold}s time diff: ', count / len(diffs))



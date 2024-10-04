# Graph of
# Performance (y-axis)
# Number of Cores (x-axis)

#import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt


#import os.path
#from os import path
#import pandas as pd
#import numpy as np

# Gather performance results from log files
log_files = ['./logs/apoa1-1.log', './logs/apoa1-2.log', './logs/apoa1-4.log', './logs/apoa1-8.log', './logs/apoa1-16.log']
#log_files = glob.glob('./logs/*.log', recursive=False)

num_cpus_arr = np.array([])
s_step_arr = np.array([])

for filename in log_files:
    file = open(filename, 'r')
    for line in file:
        if re.search('Benchmark', line):
            num_cpus = int(line.split(' ')[3])
            s_step = float(line.split(' ')[5])
            num_cpus_arr = np.append(num_cpus_arr, np.array([num_cpus]))
            s_step_arr = np.append(s_step_arr, np.array([s_step]))
            break
            
# Hardcode results of ns_per_day.py  
ns_day_arr = np.array([0.0754122, 0.153103, 0.285054, 0.973057, 1.75722])

eff_arr = np.array([0.0754122/1, 0.153103/2, 0.285054/4, 0.973057/8, 1.75722/16])
eff_arr = np.divide(eff_arr, 0.973057/8)
            
# Create a plot of performance results in s/step
x = num_cpus_arr
y = s_step_arr

plt.figure()
plt.plot(x, y)
plt.title('Scaling Performance of ApoA1 Benchmark')
plt.xlabel('Number of CPUs')
plt.ylabel('Performance (s/step)')
plt.grid()
plt.xlim(0,16)
#plt.ylim(0,2)

plt.savefig('performance_s_step.png')


# Create a plot of performance results in ns/day
x = num_cpus_arr
y = ns_day_arr

plt.figure()
plt.plot(x, y)
plt.title('Scaling Performance of ApoA1 Benchmark')
plt.xlabel('Number of CPUs')
plt.ylabel('Performance (ns/day)')
plt.grid()
plt.xlim(0,16)
plt.ylim(0,2)

plt.savefig('performance_ns_day.png')


# Create a plot of efficiency results
x = num_cpus_arr
y = eff_arr

plt.figure()
plt.plot(x, y)
plt.title('Scaling Efficiency of ApoA1 Benchmark')
plt.xlabel('Number of CPUs')
plt.ylabel('Efficiency')
plt.grid()
plt.xlim(0,16)
plt.ylim(0,1)

plt.savefig('efficiency_plot.png')




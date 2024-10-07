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

# Gather performance results from CPU-only log files
log_files_C = ['./logs/apoa1-1.log', './logs/apoa1-2.log', './logs/apoa1-4.log', './logs/apoa1-8.log', './logs/apoa1-16.log']
#log_files = glob.glob('./logs/*.log', recursive=False)

num_cpus_arr_C = np.array([])
s_step_arr_C = np.array([])

for filename in log_files_C:
    file = open(filename, 'r')
    for line in file:
        if re.search('Benchmark', line):
            num_cpus_C = int(line.split(' ')[3])
            s_step_C = float(line.split(' ')[5])
            num_cpus_arr_C = np.append(num_cpus_arr_C, np.array([num_cpus_C]))
            s_step_arr_C = np.append(s_step_arr_C, np.array([s_step_C]))
            break
            
# Gather performance results from single-node GPU log files
log_files_G = ['./logs/apoa1-GPU-1.log', './logs/apoa1-GPU-2.log', './logs/apoa1-GPU-4.log', './logs/apoa1-GPU-8.log', './logs/apoa1-GPU-16.log']
#log_files = glob.glob('./logs/*.log', recursive=False)

num_cpus_arr_G = np.array([])
s_step_arr_G = np.array([])

for filename in log_files_G:
    file = open(filename, 'r')
    for line in file:
        if re.search('Benchmark', line):
            num_cpus_G = int(line.split(' ')[3])
            s_step_G = float(line.split(' ')[5])
            num_cpus_arr_G = np.append(num_cpus_arr_G, np.array([num_cpus_G]))
            s_step_arr_G = np.append(s_step_arr_G, np.array([s_step_G]))
            break
            
# Hardcode results of ns_per_day.py
ns_day_arr_C = np.array([0.0754122, 0.153103, 0.285054, 0.973057, 1.75722])
ns_day_arr_G = np.array([7.44807, 13.4145, 20.0439, 21.5405, 18.2305])

eff_arr_C = np.array([0.0754122/1, 0.153103/2, 0.285054/4, 0.973057/8, 1.75722/16])
eff_arr_C = np.divide(eff_arr_C, 0.973057/8)

eff_arr_G = np.array([7.44807/1, 13.4145/2, 20.0439/4, 21.5405/8, 18.2305/16])
eff_arr_G = np.divide(eff_arr_G, 7.44807/1)
            
# Create a plot of performance results in s/step
x1 = num_cpus_arr_C
y1 = s_step_arr_C
x2 = num_cpus_arr_G
y2 = s_step_arr_G

plt.figure()
plt.plot(x1, y1, label="CPU-only")
plt.plot(x2, y2, label="single-node CPU+GPU")
plt.title('Scaling Performance of ApoA1 Benchmark')
plt.xlabel('Number of CPUs')
plt.ylabel('Performance (s/step)')
plt.grid()
plt.xlim(0,16)
#plt.ylim(0,2)
plt.legend()

plt.savefig('performance_s_step.png')


# Create a plot of performance results in ns/day
x1 = num_cpus_arr_C
y1 = ns_day_arr_C
x2 = num_cpus_arr_G
y2 = ns_day_arr_G

plt.figure()
plt.plot(x1, y1, label="CPU-only")
plt.plot(x2, y2, label="single-node CPU+GPU")
plt.title('Scaling Performance of ApoA1 Benchmark')
plt.xlabel('Number of CPUs')
plt.ylabel('Performance (ns/day)')
plt.grid()
plt.xlim(0,16)
#plt.ylim(0,2)
plt.legend()

plt.savefig('performance_ns_day.png')


# Create a plot of efficiency results
x1 = num_cpus_arr_C
y1 = eff_arr_C
x2 = num_cpus_arr_G
y2 = eff_arr_G

plt.figure()
plt.plot(x1, y1, label="CPU-only")
plt.plot(x2, y2, label="single-node CPU+GPU")
plt.title('Scaling Efficiency of ApoA1 Benchmark')
plt.xlabel('Number of CPUs')
plt.ylabel('Efficiency')
plt.grid()
plt.xlim(0,16)
plt.ylim(0,1)
plt.legend()

plt.savefig('efficiency_plot.png')




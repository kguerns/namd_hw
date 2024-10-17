# Graph of
# Performance (y-axis)
# Number of Cores (x-axis)

#import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import subprocess


# Gather performance results from CPU-only log files
log_files_C = ['./logs/apoa1-1.log', './logs/apoa1-2.log', './logs/apoa1-4.log', './logs/apoa1-8.log', './logs/apoa1-16.log']
#log_files = glob.glob('./logs/*.log', recursive=False)
num_cpus_arr_C = np.array([])
s_step_arr_C = np.array([])
ns_day_arr_C = np.array([])

for filename in log_files_C:
    # Benchmark result
    file = open(filename, 'r')
    for line in file:
        if re.search('Benchmark', line):
            num_cpus_arr_C = np.append(num_cpus_arr_C, np.array([int(line.split(' ')[3])]))
            s_step_arr_C = np.append(s_step_arr_C, np.array([float(line.split(' ')[5])]))
            file.close()
            break
    # ns_per_day.py result
    output = subprocess.run(['python3', 'ns_per_day.py', filename], stdout=subprocess.PIPE)
    value = str(output.stdout)
    ns_day_arr_C = np.append(ns_day_arr_C, np.array([float(value.split('\\')[0].split(':')[1].strip())]))

            
# Gather performance results from single-node GPU-offload log files
log_files_G = ['./logs/apoa1-GPU-1.log', './logs/apoa1-GPU-2.log', './logs/apoa1-GPU-4.log', './logs/apoa1-GPU-8.log', './logs/apoa1-GPU-16.log']
num_cpus_arr_G = np.array([])
s_step_arr_G = np.array([])
ns_day_arr_G = np.array([])

for filename in log_files_G:
    # Benchmark result
    file = open(filename, 'r')
    for line in file:
        if re.search('Benchmark', line):
            num_cpus_arr_G = np.append(num_cpus_arr_G, np.array([int(line.split(' ')[3])]))
            s_step_arr_G = np.append(s_step_arr_G, np.array([float(line.split(' ')[5])]))
            file.close()
            break
    # ns_per_day.py result
    output = subprocess.run(['python3', 'ns_per_day.py', filename], stdout=subprocess.PIPE)
    value = str(output.stdout)
    ns_day_arr_G = np.append(ns_day_arr_G, np.array([float(value.split('\\')[0].split(':')[1].strip())]))

            
# Gather performance results from single-node GPU-resident log files
log_files_GR = ['./logs/apoa1-GPU-Res-1.log', './logs/apoa1-GPU-Res-2.log', './logs/apoa1-GPU-Res-4.log', './logs/apoa1-GPU-Res-8.log', './logs/apoa1-GPU-Res-16.log']
num_cpus_arr_GR = np.array([])
s_step_arr_GR = np.array([])
ns_day_arr_GR = np.array([])

for filename in log_files_GR:
    # Benchmark result
    file = open(filename, 'r')
    for line in file:
        if re.search('Benchmark', line):
            num_cpus_arr_GR = np.append(num_cpus_arr_GR, np.array([int(line.split(' ')[3])]))
            s_step_arr_GR = np.append(s_step_arr_GR, np.array([float(line.split(' ')[5])]))
            file.close()
            break
    # ns_per_day.py result
    output = subprocess.run(['python3', 'ns_per_day.py', filename], stdout=subprocess.PIPE)
    value = str(output.stdout)
    ns_day_arr_GR = np.append(ns_day_arr_GR, np.array([float(value.split('\\')[0].split(':')[1].strip())]))

            
# Calculate Efficiency Results
eff_arr_C = np.divide(ns_day_arr_C, num_cpus_arr_C)
eff_arr_C = np.divide(eff_arr_C, np.max(eff_arr_C))

eff_arr_G = np.divide(ns_day_arr_G, num_cpus_arr_G)
eff_arr_G = np.divide(eff_arr_G, np.max(eff_arr_G))

eff_arr_GR = np.divide(ns_day_arr_GR, num_cpus_arr_GR)
eff_arr_GR = np.divide(eff_arr_GR, np.max(eff_arr_GR))

            
# Create a plot of performance results in s/step
x1 = num_cpus_arr_C
y1 = s_step_arr_C
x2 = num_cpus_arr_G
y2 = s_step_arr_G
x3 = num_cpus_arr_GR
y3 = s_step_arr_GR

plt.figure()
plt.plot(x1, y1, label="CPU-only")
plt.plot(x2, y2, label="single-node GPU-offload")
plt.plot(x3, y3, label="single-node GPU-resident")
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
x3 = num_cpus_arr_GR
y3 = ns_day_arr_GR

plt.figure()
plt.plot(x1, y1, label="CPU-only")
plt.plot(x2, y2, label="single-node GPU-offload")
plt.plot(x3, y3, label="single-node GPU-resident")
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
x3 = num_cpus_arr_GR
y3 = eff_arr_GR

plt.figure()
plt.plot(x1, y1, label="CPU-only")
plt.plot(x2, y2, label="single-node GPU-offload")
plt.plot(x3, y3, label="single-node GPU-resident")
plt.title('Scaling Efficiency of ApoA1 Benchmark')
plt.xlabel('Number of CPUs')
plt.ylabel('Efficiency')
plt.grid()
plt.xlim(0,16)
plt.ylim(0,1)
plt.legend()

plt.savefig('efficiency_plot.png')




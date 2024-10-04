#!/bin/bash

#SBATCH --job-name namd_p4
#SBATCH --nodes 1
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 4
#SBATCH --mem 16gb
#SBATCH --time 00:20:00

config_path=$HOME/namd_hw/apoa1/apoa1.namd
log_path=$HOME/namd_hw/logs/apoa1-$SLURM_CPUS_PER_TASK.log

srun $HOME/namd_hw/NAMD_3.0_Linux-x86_64-multicore/namd3 +p$SLURM_CPUS_PER_TASK ${config_path} > ${log_path}

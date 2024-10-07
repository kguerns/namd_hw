#!/bin/bash

#SBATCH --job-name namd_GPU_Res_p1
#SBATCH --nodes 1
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 16gb
#SBATCH --gpus a100:1
#SBATCH --time 00:10:00

config_path=$HOME/namd_hw/apoa1/apoa1.namd
log_path=$HOME/namd_hw/logs/apoa1-GPU-Res-${SLURM_CPUS_PER_TASK}.log

srun $HOME/namd_hw/NAMD_3.0_Linux-x86_64-multicore-CUDA/namd3 +p${SLURM_CPUS_PER_TASK} ${config_path} > ${log_path}

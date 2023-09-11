#!/bin/bash
#SBATCH --job-name=graphium_training_depth_6
#SBATCH --output=graphium_train_output_depth_6.txt
#SBATCH --error=graphium_train_error_depth_6.txt
#SBATCH --ntasks=1
#SBATCH --time=48:00:00   
#SBATCH --mem=32Gb
#SBATCH --partition=unkillable
#SBATCH --gres=gpu:a100l:1
#SBATCH --cpus-per-task=6

# Activate the conda environment
source /home/mila/h/hussein-mohamu.jama/miniconda3/etc/profile.d/conda.sh
conda activate graphium
# Execute the training command
graphium-train --config-path=$(pwd)/expts/hydra-configs_depth_6 --config-name=main model=gated_gcn accelerator=gpu +hparam_search=optuna


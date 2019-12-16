#!/bin/bash
#SBATCH --account={account}
#SBATCH --time={time_limit}
#SBATCH --gres=gpu:{gpu_type}:{num_gpu}
#SBATCH --cpus-per-task={cpus_per_task}
#SBATCH --output=logs/{OUTPUT_FILE_NAME}.out
#SBATCH --mem={mem}

# source env/bin/activate

echo "JOB STARTED"
date
SECONDS=0

sh sample_job.sh {model} {learning_rate} {seed}

echo "JOB FINISHED"
date
duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."

# deactivate

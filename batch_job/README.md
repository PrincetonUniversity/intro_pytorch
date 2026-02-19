# Example of Running a PyTorch Job on Adroit

Connect to Adroit and obtain the files (for account submit [this form](https://forms.rc.princeton.edu/registration/?q=adroit)):

```
$ ssh <YourNetID>@adroit.princeton.edu
$ cd /scratch/network/$USER
$ git clone https://github.com/PrincetonUniversity/intro_pytorch
$ cd intro_pytorch/batch_job
```

The job will run on one of the compute nodes. The compute nodes do not have internet access so download the MNNIST dataset on the login node before submitting the job:

```
$ module load anaconda3/2025.12
$ conda activate /home/jdh4/.conda/envs/torch-env
$ python download_mnist.py
```

In this example, a pre-installed Conda environment by user `jdh4` is being used. After the workshop you can [create your own environment](https://researchcomputing.princeton.edu/support/knowledge-base/pytorch) and use that.

Submit the job to the Slurm scheduler:

```
$ sbatch job.slurm
```

Monitor the progress of the job:

```
$ squeue --me
```

If the command above lists your job then know that for the `ST` column (which is state) `PD` is pending and `R` is running. If the job is not listed then it either finished successfully or failed.

After the job finishes, you can inspect the output:

```
$ cat slurm-*.out
```

The bottom of the output should be:

```
...
Train Epoch: 3 [58240/60000 (97%)]	Loss: 0.023558
Train Epoch: 3 [58880/60000 (98%)]	Loss: 0.055956
Train Epoch: 3 [59520/60000 (99%)]	Loss: 0.018880

Test set: Average loss: 0.0308, Accuracy: 9901/10000 (99%)
```

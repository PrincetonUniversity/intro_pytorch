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

After the job finishes, you can inspect the output:

```
$ cat slurm-*.out
```

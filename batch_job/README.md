# Example of Running a PyTorch Job on Adroit

Connect to Adroit and obtain the files:

```
$ ssh <YourNetID>@adroit.princeton.edu
$ git clone https://github.com/PrincetonUniversity/intro_pytorch
$ cd intro_pytorch/batch_job
```

The job will run on one of the compute nodes. The compute nodes do not have internet access so download the MNNIST dataset on the login node before submitting the job:

```
$ module load anaconda3/2024.10
$ conda activate /home/jdh4/.conda/envs/torch-env
$ python download_mnist.py
```

In this example, a pre-installed Conda environment by user `jdh4` is being used. After the workshop you can [create your own environment](https://researchcomputing.princeton.edu/support/knowledge-base/pytorch) and use that.

Submit the job to the Slurm scheduler:

```
$ sbatch --reservation=pytorch job.slurm
```

Note: After the workshop remove `--reservation=pytorch` since it no longer applies.

After the job finishes, you can inspect the output:

```
$ cat slurm-*.out
```

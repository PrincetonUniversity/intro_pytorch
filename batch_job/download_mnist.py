import torchvision
import warnings
warnings.filterwarnings("ignore")

# compute nodes do not have internet access so download the data on the login node
# and then submit the job

_ = torchvision.datasets.MNIST('data', train=True, transform=None,
                               target_transform=None, download=True)

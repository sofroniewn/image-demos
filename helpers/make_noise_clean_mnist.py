from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import Dataset
from torch import randn
import numpy as np
from skimage.io import imsave

mnist_train = MNIST('../data/MNIST', download = True,
                    transform = transforms.Compose([
                        transforms.ToTensor(),
                    ]), train = True)

def add_noise(img):
    return img + randn(img.size())*0.4

class SyntheticNoiseDataset(Dataset):
    def __init__(self, data, mode='train'):
        self.mode = mode
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        img = self.data[index][0]
        return add_noise(img), img

noisy_mnist_train = SyntheticNoiseDataset(mnist_train, 'train')

size = [noisy_mnist_train[0][0][0].shape[0], noisy_mnist_train[0][0][0].shape[1]]
noisy = np.empty((len(noisy_mnist_train), size[0], size[1]))
clean = np.empty((len(noisy_mnist_train), size[0], size[1]))

for i, data in enumerate(noisy_mnist_train):
    noisy[i] = data[0][0].numpy()
    clean[i] = data[1][0].numpy()


imsave('data/mnist/noisy.tif', noisy.astype('float32'), plugin='tifffile',
       photometric='minisblack')

imsave('data/mnist/clean.tif', clean.astype('float32'), plugin='tifffile',
       photometric='minisblack')

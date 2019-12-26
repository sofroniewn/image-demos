import numpy as np
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from glob import glob
from os import mkdir

base_name = 'data/kaggle-nuclei/fixes/stage1_train/*'
datasets = glob(base_name)

for d in datasets:
    print(d)
    image_files = glob(d + '/images/*png')
    # mask_files = glob(d + '/masks/*.png')
    # mkdir(d + '/labels')

    image = imread(image_files[0])
    imsave(d + '/images/image_gray.tif', (255*rgb2gray(image)).astype('uint8'),
           plugin='tifffile', photometric='minisblack')

    # masks = np.array([imread(f) for f in mask_files])
    #
    # labels = np.zeros(image.shape[:2], dtype=np.uint32)
    # for i, m in enumerate(masks):
    #     labels[m>0] = i+1
    #
    # imsave(d + '/labels/label.tif', labels, plugin='tifffile',
    #        photometric='minisblack')

"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
from skimage.io import imread, imsave
from glob import glob
from napari import ViewerApp
from napari.util import app_context
import os
base_name = 'data/kaggle-nuclei/fixes/stage1_train/*'
datasets = glob(base_name)


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the first image
    image = imread(datasets[0] + '/images/image_gray.tif')
    image_layer = viewer.add_image(image, name='0', clim_range=(0, 255))
    image_layer.colormap = 'gray'

    # add the first labels
    if o.exists(datasets[0] + '/labels/drawn.tif'):
        labels = imread(datasets[0] + '/labels/drawn.tif')
    else:
        labels = np.zeros(image.shape, dtype=np.int)

    labels_layer = viewer.add_labels(labels, name='labels', opacity=0.5)

    def save(viewer):
        """Save the current annotations
        """
        labels = viewer[1].image
        name = int(viewer[0].name)
        imsave(datasets[0] + '/labels/drawn.tif', labels, plugin='tifffile',
               photometric='minisblack')
        msg = 'Saving ' + viewer[0].name
        print(msg)
        viewer.status = msg

    def next(viewer):
        """Save the current annotation and load the next image and annotation
        """
        save(viewer)
        name = int(viewer[0].name)
        name = name + 1
        if name == len(datasets):
            name = 0

        image = imread(datasets[name] + '/images/image_gray.tif')

        if o.exists(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer[0].image = image
        viewer[0].name = str(name)
        viewer[1].image = labels

        msg = 'Loading ' + viewer[0].name
        print(msg)
        viewer.status = msg

    def previous(viewer):
        """Save the current annotation and load the previous image and annotation
        """
        save(viewer)
        name = int(viewer[0].name)
        name = name - 1
        if name == -1:
            name = len(datasets)-1

        image = imread(datasets[name] + '/images/image_gray.tif')

        if o.exists(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer[0].image = image
        viewer[0].name = str(name)
        viewer[1].image = labels

        msg = 'Loading ' + viewer[0].name
        print(msg)
        viewer.status = msg

    def revert(viewer):
        """Loads the last saved annotation
        """
        name = int(viewer[0].name)
        if o.exists(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer[1].image = labels

        msg = 'Reverting ' + viewer[0].name
        print(msg)
        viewer.status = msg

    custom_key_bindings = {'s': save, 'r': revert, 'n': next, 'b': previous}
    viewer.key_bindings = custom_key_bindings

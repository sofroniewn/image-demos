"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
from skimage.io import imread, imsave
from glob import glob
from napari import ViewerApp
from napari.util import app_context
from os.path import isfile
import warnings

skimage_save_warning = "'%s is a low contrast image' % fname"

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning,
                            message=skimage_save_warning)

base_name = 'data/kaggle-nuclei/fixes/stage1_train/*'
datasets = sorted(glob(base_name))


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the first image
    image = imread(datasets[0] + '/images/image_gray.tif')
    image_layer = viewer.add_image(image, name='0', clim_range=(0, 255))
    image_layer.colormap = 'gray'

    # add the first labels
    if isfile(datasets[0] + '/labels/drawn.tif'):
        labels = imread(datasets[0] + '/labels/drawn.tif')
    else:
        labels = np.zeros(image.shape, dtype=np.int)

    labels_layer = viewer.add_labels(labels, name='labels', opacity=0.5)
    labels_layer.brush_size = 2
    labels_layer.n_dimensional = False


    def save(viewer):
        """Save the current annotations
        """
        labels = viewer.layers[1].image.astype(np.uint16)
        name = int(viewer.layers[0].name)
        imsave(datasets[name] + '/labels/drawn.tif', labels, plugin='tifffile',
               photometric='minisblack')
        msg = 'Saving ' + viewer.layers[0].name + ': ' + datasets[name]
        print(msg)
        viewer.status = msg

    def next(viewer):
        """Save the current annotation and load the next image and annotation
        """
        save(viewer)
        name = int(viewer.layers[0].name)
        name = name + 1
        if name == len(datasets):
            name = 0

        image = imread(datasets[name] + '/images/image_gray.tif')

        if isfile(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer.layers[0].image = image
        viewer.layers[0].name = str(name)
        viewer.layers[1].image = labels

        msg = 'Loading ' + viewer.layers[0].name
        print(msg)
        viewer.status = msg

    def previous(viewer):
        """Save the current annotation and load the previous image and annotation
        """
        save(viewer)
        name = int(viewer.layers[0].name)
        name = name - 1
        if name == -1:
            name = len(datasets)-1

        image = imread(datasets[name] + '/images/image_gray.tif')

        if isfile(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer.layers[0].image = image
        viewer.layers[0].name = str(name)
        viewer.layers[1].image = labels

        msg = 'Loading ' + viewer.layers[0].name
        print(msg)
        viewer.status = msg

    def revert(viewer):
        """Loads the last saved annotation
        """
        name = int(viewer.layers[0].name)
        if isfile(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer.layers[1].image = labels

        msg = 'Reverting ' + viewer.layers[0].name
        print(msg)
        viewer.status = msg

    def increment_label(viewer):
        """Increments current label
        """
        label = viewer.layers[1].selected_label
        viewer.layers[1].selected_label = label + 1

    def decrement_label(viewer):
        """Decrements current label
        """
        label = viewer.layers[1].selected_label
        if label > 0:
            viewer.layers[1].selected_label = label - 1

    def background_label(viewer):
        """Set current label to background
        """
        viewer.layers[1].selected_label = 0

    def max_label(viewer):
        """Sets label to max label in visible slice
        """
        label = viewer.layers[1]._image_view.max()
        viewer.layers[1].selected_label = label + 1

    custom_key_bindings = {'s': save, 'r': revert, 'n': next, 'b': previous,
                           'i': increment_label, 'm': max_label,
                           'd': decrement_label, 't': background_label}

    viewer.keybindings = custom_key_bindings

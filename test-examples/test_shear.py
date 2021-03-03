"""
Display raw and sheared
"""
import numpy as np
from skimage.io import imread
import napari
from napari.utils.transforms import shear_matrix_from_angle


import napari
import numpy as np

with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)
    layer = viewer.add_image(np.random.rand(64,64,64))

    mat = np.eye(3)
    mat[2,0] = 0.5
    print(mat)
    layer.shear = mat
    print(layer.shear, layer.rotate)  # array([-0. ,  0.4,  0. ])
    layer.shear = mat
    print(layer.shear, layer.rotate)  # array([-0.        ,  0.27586207,  0.        ])
    layer.shear = mat
    print(layer.shear, layer.rotate)  # array([-0.        ,  0.21253985,  0.        ])

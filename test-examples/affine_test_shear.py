"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
import napari


with napari.gui_qt():
    # add the image
    viewer = napari.Viewer()
    
    # test_2d = np.dstack([0.5 * np.ones((36, 36)), np.zeros((36, 36)), np.eye(36)])
    # #viewer.add_image(test_2d, shear=[-1.0])
    # viewer.add_image(test_2d, shear=[-1.0], rgb=True)

    test_3d = np.diag(np.arange(36)).reshape(36, 1, 36) * np.ones((1, 36, 1))
    viewer.add_image(test_3d, shear=[0.0, -1.0, 0.0])


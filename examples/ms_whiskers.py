"""
Displays an MRI volume
"""

import imageio
from napari import Viewer, gui_qt
import numpy as np

vid = imageio.get_reader('data-njs/ms_whiskers/IMG_6785.mov',  'ffmpeg')
mov = np.array([im for im in vid.iter_data()])

print(mov.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_image(mov, name='whiskers')

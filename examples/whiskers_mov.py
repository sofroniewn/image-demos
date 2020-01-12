"""
Displays an MRI volume
"""

import imageio
from napari import Viewer, gui_qt
import numpy as np

vid = imageio.get_reader('data-njs/whiskers/IMG_7988.mov',  'ffmpeg')
mov = np.array([im for im in vid.iter_data()])
mov = mov[35:]
mov = mov.mean(axis=-1)
print(mov.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_image(mov, name='whiskers')
    viewer.add_image(np.mean(mov, axis=0), name='mean')

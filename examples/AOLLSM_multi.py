"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
import napari
from napari.utils.transforms import shear_matrix_from_angle
from glob import glob
from dask_image.imread import imread

image_path = 'data/LLSM/AOLLSM_m4_raw/'
ch0_images = np.asarray(imread(image_path + 'ex6-2_CamB_ch0_*.tif'))[:, 1:, ::2, ::2]
ch1_images = np.asarray(imread(image_path + 'ex6-2_CamA_ch1_*.tif'))[:, 1:, ::2, ::2]
ch2_images = np.asarray(imread(image_path + 'ex6-2_CamA_ch2_*.tif'))[:, 1:, ::2, ::2]


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(ch0_images, name='488nm', colormap='bop purple', rendering='attenuated_mip', attenuation=0.01,
                     shear=shear_matrix_from_angle(31.5), scale=[1.33, 1, 1], blending='additive', contrast_limits=[250, 1000])
    viewer.add_image(ch1_images, name='560nm', colormap='bop blue', rendering='attenuated_mip', attenuation=0.01,
                     shear=shear_matrix_from_angle(31.5), scale=[1.33, 1, 1], blending='additive', contrast_limits=[900, 2350])
    viewer.add_image(ch2_images, name='642nm', colormap='bop orange', rendering='attenuated_mip', attenuation=0.01,
                     shear=shear_matrix_from_angle(31.5), scale=[1.33, 1, 1], blending='additive', contrast_limits=[750, 1700])

"""
Displays an 100GB zarr file of lattice light sheet data
"""

import napari
from dask_image.imread import imread


image_path = '/Volumes/GoogleDrive/.shortcut-targets-by-id/1_JT0w45Bnb3X3u5eUgZBaz_E101Tbedn/slice-tiff/'
ch0_images = imread(image_path + 'ch0/*.tif')
#ch1_images = np.asarray(imread(image_path + 'ch2/*.tif'))
#ch2_images = np.asarray(imread(image_path + 'ch2/*.tif'))


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(ch0_images, name='488nm', colormap='bop purple', rendering='attenuated_mip', attenuation=0.01,
                     scale=[1.33, 1, 1], blending='additive', contrast_limits=[250, 1000])
    # viewer.add_image(ch1_images, name='560nm', colormap='bop blue', rendering='attenuated_mip', attenuation=0.01,
    #                  shear=shear_matrix_from_angle(31.5), scale=[1.33, 1, 1], blending='additive', contrast_limits=[900, 2350])
    # viewer.add_image(ch2_images, name='642nm', colormap='bop orange', rendering='attenuated_mip', attenuation=0.01,
    #                  shear=shear_matrix_from_angle(31.5), scale=[1.33, 1, 1], blending='additive', contrast_limits=[750, 1700])



"""
Image pyramid of pathology slide
"""

# Import magicgui and qt functionality
from qtpy.QtWidgets import QSlider
from qtpy.QtCore import Qt
from magicgui import magicgui
import numpy as np
import dask.array as da
import napari
from stardist.models import StarDist2D


model = StarDist2D.from_pretrained('2D_versatile_he')

file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]
#segmented = [ar.map_blocks(lambda block: model.predict_instances(block[:, :, :3])[0], drop_axis=2, chunks=ar.chunksize[:-1], dtype=np.int)[:ar.shape[0], :ar.shape[1]] for ar in pyramid]
segmented = [ar.map_blocks(lambda block: model.predict_instances(block[:, :, :3])[0], drop_axis=2, chunks=ar.chunksize[:-1], dtype=np.int)[:ar.shape[0], :ar.shape[1]] for ar in pyramid]


with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()

    # add the pyramid
    viewer.add_image(pyramid, name='slide', multiscale=True)
    viewer.add_labels(segmented, name='segmentation', multiscale=True)

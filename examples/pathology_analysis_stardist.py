"""
Image pyramid of pathology slide
"""

# Import magicgui and qt functionality
from qtpy.QtWidgets import QSlider
from qtpy.QtCore import Qt
from magicgui import magicgui
from napari import layers
import numpy as np
import dask.array as da
import napari
from stardist.models import StarDist2D
from csbdeep.utils import normalize


model = StarDist2D.from_pretrained('2D_versatile_he')

file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]
#segmented = [ar.map_blocks(lambda block: model.predict_instances(block[:, :, :3])[0], drop_axis=2, chunks=ar.chunksize[:-1], dtype=np.int)[:ar.shape[0], :ar.shape[1]] for ar in pyramid]
#segmented = [ar.map_blocks(lambda block: model.predict_instances(block[:, :, :3])[0], drop_axis=2, chunks=ar.chunksize[:-1], dtype=np.int)[:ar.shape[0], :ar.shape[1]] for ar in pyramid]

image = np.asarray(pyramid[0][68_000:71_500, 123_500:127_000])
segmented = model.predict_instances(normalize(image[:, :, :3]))[0]

@magicgui(call_button="analyze")
def segmentation(input: layers.Image) -> layers.Labels:
    """Segment an image based using stardist."""

    print("Segmenting...")

    print("... Completed")  

    return segmented

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()
    viewer.add_image(image, name='H&E stained lymph node', multiscale=False)

    # instantiate the widget
    gui = segmentation.Gui()


    viewer.window.add_dock_widget(gui, area='bottom')
    
    # keep the dropdown menus in the gui in sync with the layer model
    viewer.layers.events.changed.connect(lambda x: gui.refresh_choices())

    gui.refresh_choices()

    # add the pyramid
    #viewer.add_labels(segmented, name='nuclei segmentation', multiscale=False)


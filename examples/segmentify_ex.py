import os
import napari
from segmentify import segmentation
import numpy as np


# parse input file
example_image = "data/segmentify/hpa.png"
example_labels = "data/segmentify/hpa_labels.tif"

with napari.gui_qt():
    viewer = napari.Viewer()

    # instantiate the widget
    gui = segmentation.Gui()

    # add our new widget to the napari viewer
    viewer.window.add_dock_widget(gui)

    # keep the dropdown menus in the gui in sync with the layer model
    viewer.layers.events.connect(lambda x: gui.refresh_choices())

    gui.refresh_choices()

    # load data
    viewer.open(example_image)
    viewer.open(example_labels, layer_type='labels')

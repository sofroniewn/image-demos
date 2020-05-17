from magicgui import magicgui
from napari import layers
from stardist.models import StarDist2D
import numpy as np
import napari


model = StarDist2D.from_pretrained('2D_demo')


@magicgui(call_button="execute")
def segmentation(base_image: layers.Image) -> layers.Labels:
    """Segment an image based using stardist."""

    print("Segmenting...")

    # fit and predict
    if base_image.rgb:
        data = base_image.data.mean(axis=2)
    else:
        data = base_image.data

    # normalize image based on clims
    clims = base_image.contrast_limits
    data = (data - clims[0]) / (clims[1] - clims[0])

    labels, details = model.predict_instances(data)

    print("... Completed")  

    return labels


# parse input file
example_image = "data/RxRx19a/images/VERO-1/Plate1/AA02_s2_w1.png"

with napari.gui_qt():
    viewer = napari.Viewer()

    # instantiate the widget
    gui = segmentation.Gui()

    # add our new widget to the napari viewer
    viewer.window.add_dock_widget(gui)

    # keep the dropdown menus in the gui in sync with the layer model
    viewer.layers.events.changed.connect(lambda x: gui.refresh_choices())

    gui.refresh_choices()

    # load data
    viewer.open(example_image)

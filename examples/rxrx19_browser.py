from magicgui import magicgui
from napari import layers
from stardist.models import StarDist2D
import numpy as np
import napari
import os
from glob import glob
from qtpy.QtWidgets import QListWidget
from qtpy.QtCore import Qt


def open_name(item):
    name = item.text()
    print('Loading', name, '...')
    viewer.layers.select_all()
    viewer.layers.remove_selected()
    
    cmaps = ['blue', 'magenta', 'yellow', 'red', 'green', 'cyan']
    for i in range(1, 6):
        fname = f'{base_path}{name}_w{i}.png'
        if os.path.isfile(fname):
            viewer.open(fname, colormap=cmaps[i-1], blending='additive')
    print('... done.')
    

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
base_path = 'data/RxRx19a/images/VERO-1/Plate1/'
files = sorted(glob(base_path + "*.png"))

names = [os.path.basename(f)[:7] for f in files]
unique_names, counts = np.unique(names, return_counts=True)
names = list(unique_names[counts==5])


with napari.gui_qt():
    viewer = napari.Viewer()

    # instantiate the widget
    gui = segmentation.Gui()

    list_widget = QListWidget()
    for n in names:
        list_widget.addItem(n)

    list_widget.currentItemChanged.connect(open_name)

    viewer.window.add_dock_widget([list_widget, gui], area='right')
    
    # keep the dropdown menus in the gui in sync with the layer model
    viewer.layers.events.changed.connect(lambda x: gui.refresh_choices())

    gui.refresh_choices()

    list_widget.setCurrentRow(0)

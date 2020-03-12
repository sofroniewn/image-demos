import numpy as np
import napari
from skimage import data
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
    
    
with napari.gui_qt():
    blobs_raw = data.binary_blobs(length=64, n_dim=2, volume_fraction=0.1)
    viewer = napari.view_image(blobs_raw)
    
    static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    axes = static_canvas.figure.subplots()
    axes.plot(blobs_raw.mean(axis=0))
    viewer.window.add_dock_widget(static_canvas, area='bottom', name='matplotlib figure')    

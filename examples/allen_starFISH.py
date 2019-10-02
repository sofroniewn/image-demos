"""
Displays FISH data, raw and deconvolved, with spots detected using starFISH
"""

from skimage.io import imread
import numpy as np
import pandas as pd
from napari import Viewer, gui_qt

raw_spots = pd.read_csv('data-njs/smFISH/allen_smfish_spots.csv')
spots = raw_spots.loc[:, [['x', 'y']]].values
spots[:, 1] = -spots[:, 1]

print(len(spots))

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the spots
    layer = viewer.add_points(spots)

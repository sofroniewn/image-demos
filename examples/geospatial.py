"""
Displays a xarray geodata
"""

import xarray as xr
import numpy as np
from napari import Viewer, gui_qt

band3_path = 'data/geodata/LT05_L1TP_032031_20050406_20160912_01_T1_sr_band3.tif'
band3_xr = xr.open_rasterio(band3_path, chunks={'band': 1, 'x': 1024, 'y': 1024})
evi_path = 'data/geodata/LT05_L1TP_032031_20050406_20160912_01_T1_sr_evi.tif'
evi_xr = xr.open_rasterio(evi_path, chunks={'band': 1, 'x': 1024, 'y': 1024})


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    layer_b3 = viewer.add_image(band3_xr, name='band3', clim_range=(0, 10_000), clim=(0, 2500))
    layer_evi = viewer.add_image(evi_xr, name='evi', clim_range=(0, 10_000), clim=(700, 4200))

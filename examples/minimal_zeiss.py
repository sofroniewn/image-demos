"""
Minmal czi file example
"""
import czifile as zis
import numpy as np
import napari

file_name = 'data-njs/zeiss/CellDivision_T=10_Z=15_CH=2_DCV_small.czi'
czi = zis.CziFile(file_name)
cziarray = czi.asarray()
#cziarray = np.squeeze(cziarray)
print('czi file shape', cziarray.shape)

with napari.gui_qt():
    napari.view_image(cziarray, channel_axis=2, scale=[1, 1, 3, 1, 1])

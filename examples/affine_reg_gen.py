"""
Affine registration
"""
from pathlib import Path

import napari
import numpy as np
from skimage import io, measure
from skimage.transform import AffineTransform


# Data from https://github.com/DeMarcoLab/correlateim/tree/master/data
data_path = Path('/Users/nsofroniew/GitHub/image-demos/data/affine')
worm_lm = io.imread(data_path/'worm_fluorescence-microscopy.tif')
worm_sem = io.imread(data_path/'worm_scanning-electron-microscopy.tif')

points_sem = np.array([
    [ 660.28046777,  456.24733395],
    [ 641.75456871, 1007.29992248],
    [1012.86707775,  994.13141409],
    [1440.2450317 , 1809.38172378],
    [1213.9861149 , 1840.50728905],
    [1368.41680414, 2129.01733639]])

points_lm = np.array([
    [ 592.88574219, 1269.09706845],
    [ 566.75134323,  957.20365742],
    [ 786.52713456,  969.01956018],
    [1014.96792124,  529.46797753],
    [ 883.41753718,  516.07662107],
    [ 974.00612501,  364.0453389 ]])


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(worm_lm, visible=False)
    viewer.add_image(worm_sem, opacity=0.5)
    viewer.add_points(points_sem, name="points_sem", face_color="orange")
    viewer.add_points(points_lm, name="points_lm", face_color="yellow", visible=False)

    src = points_lm
    dst = points_sem
    model = AffineTransform()
    model.estimate(src, dst)

    viewer.add_image(worm_lm, name="result", affine=model.params, blending='additive')
    viewer.add_points(model(points_lm), name="result_lm_in_sem", face_color="blue", size=20)

    viewer.reset_view()
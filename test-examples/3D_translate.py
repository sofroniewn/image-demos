import numpy as np
from skimage import data
from skimage.util import random_noise
import napari


with napari.gui_qt():
    viewer = napari.Viewer()

    blobs_raw = data.binary_blobs(length=64, n_dim=3, volume_fraction=0.1)
    # Check 2D view for all slices, 3D view, role, and transpose

    # # two arrays should be "stacked on top" of eachother in Z
    viewer.add_image(blobs_raw, colormap='blue')
    viewer.add_image(blobs_raw, translate=[64, 0, 0], blending='additive', colormap='red')
    # # World extent [[0, 0, 0], [128, 64, 64]]
    # # nsteps 128, 64, 64
    # # stepsize 1, 1, 1
    
    # # two arrays should be "stacked on top" of eachother in Z
    # viewer.add_image(blobs_raw, colormap='blue')
    # viewer.add_image(blobs_raw, translate=[-64, 0, 0], blending='additive', colormap='red')
    # # World extent [[-64, 0, 0], [64, 64, 64]]
    # # nsteps 128, 64, 64
    # # stepsize 1, 1, 1

    # two arrays should "overlap"
    # viewer.add_image(blobs_raw, colormap='blue')
    # viewer.add_image(blobs_raw[::2], scale=[2, 1, 1], blending='additive', colormap='red')
    # World extent [[0, 0, 0], [64, 64, 64]]
    # nsteps 64, 64, 64
    # stepsize 1, 1, 1

    # # two arrays should be "side by side" in X
    # viewer.add_image(blobs_raw, colormap='blue')
    # viewer.add_image(blobs_raw, translate=[0, 0, 64], blending='additive', colormap='red')
    # # World extent [[0, 0, 0], [64, 64, 128]]
    # # nsteps 64, 64, 128
    # # stepsize 1, 1, 1

    # # two arrays should be "side by side" in X
    # viewer.add_image(blobs_raw, colormap='blue')
    # viewer.add_image(blobs_raw, translate=[0, 0, -64], blending='additive', colormap='red')
    # # World extent [[0, 0, -64], [64, 64, 64]]
    # # nsteps 128, 64, 64
    # # stepsize 1, 1, 1

    # # two arrays should be "side by side" in X
    # viewer.add_image(blobs_raw, colormap='blue')
    # viewer.add_image(blobs_raw[::2], scale=[2, 1, 1], translate=[0, 0, 64], blending='additive', colormap='red')
    # # World extent [[0, 0, 0], [64, 64, 128]]
    # # nsteps 64, 64, 128
    # # stepsize 1, 1, 1

    # # two arrays should be "stacked on top" of eachother in Z
    # viewer.add_image(blobs_raw, colormap='blue')
    # viewer.add_image(blobs_raw[::2], scale=[2, 1, 1], translate=[64, 0, 0], blending='additive', colormap='red')
    # # World extent [[0, 0, 0], [128, 64, 64]]
    # # nsteps 128, 64, 64
    # # stepsize 1, 1, 1

    # # two arrays should "overlap"
    # viewer.add_image(blobs_raw[::2], scale=[2, 1, 1], colormap='blue')
    # viewer.add_image(blobs_raw[::2], scale=[2, 1, 1], blending='additive', colormap='red')
    # # World extent [[0, 0, 0], [64, 64, 64]]
    # # nsteps 32, 64, 64
    # # stepsize 2, 1, 1

    print(viewer.layers.extent.world)
    print(viewer.layers.extent.step)
    print(viewer.dims.nsteps)

    viewer.reset_view()
    for i in range(viewer.dims.nsteps[0]):
        viewer.dims.set_current_step(0, i)
    viewer.dims.set_current_step(0, 0)

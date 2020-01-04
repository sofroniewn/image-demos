"""
Displays an MRI surface timeseries
"""

# NKI resting state data from nilearn
from nilearn import datasets
from nilearn import surface
import napari
import numpy as np


nki_dataset = datasets.fetch_surf_nki_enhanced(n_subjects=1)

# Fsaverage5 surface template
fsaverage = datasets.fetch_surf_fsaverage()

# Load surface data and resting state time series from nilearn
pial_left = surface.load_surf_data(fsaverage['pial_left'])
sulc_left = surface.load_surf_data(fsaverage['sulc_left'])
timeseries = surface.load_surf_data(nki_dataset['func_left'][0]).transpose((1, 0))
timeseries = np.stack([timeseries, timeseries/2, timeseries/4, np.full(timeseries.shape, -1.5)], axis=0)
print(timeseries.shape)

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer(ndisplay=3)

    # add the mri
    viewer.add_surface((pial_left[0], pial_left[1], sulc_left), name='base')
    viewer.add_surface((pial_left[0], pial_left[1], timeseries), colormap='red', opacity=0.9, name='timeseries')

"""
Displays an MRI surface
"""

from nilearn import surface
from napari import Viewer, gui_qt
import numpy as np
import matplotlib.pyplot as plt
from vispy.color import Colormap


first = int((128*2)-np.round(255*(1.-0.90)))
second = (256-first)
colors2 = plt.cm.viridis(np.linspace(0.1, .98, first))
colors3 = plt.cm.YlOrBr(np.linspace(0.25, 1, second))
cols = np.vstack((colors2,colors3))
mymap = Colormap(cols)

base_path = 'data-njs/CBIG/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/FreeSurfer5.3/fsaverage6/'
lh_pial = surface.load_surf_mesh(base_path + 'surf/lh.pial')
lh_curv = surface.load_surf_data(base_path + 'surf/lh.curv')
lg400_atlas = surface.load_surf_data(base_path + 'label/lh.Schaefer2018_400Parcels_7Networks_order.annot')
u, idx = np.unique(lg400_atlas, return_inverse=True)
ed = np.loadtxt('data-njs/mri/LG400_Med.txt')
ed_lh = ed[:200]
X = np.insert(ed_lh, 0, 0, axis=0)
values = X[idx]


with gui_qt():
    # create an empty viewer
    viewer = Viewer(ndisplay=3)

    # add the mri
    layer = viewer.add_surface((lh_pial[0], lh_pial[1], lh_curv), name='base')
    layer = viewer.add_surface((lh_pial[0], lh_pial[1], values), name='gradient', colormap={'mymap': mymap},
                                opacity=0.8)

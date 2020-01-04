"""
Displays cryoET data
"""
import napari
from skimage.io import imread
import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as R


base_path = 'data-njs/cryo-EM/karen_1/'
membrane = imread(base_path + 'suitcase-membrane_blue.tif')
faces = pd.read_csv(base_path + 'faces.csv', header=None, keep_default_na=False).drop(8, axis=1).values
faces = np.concatenate([faces[:, [0, 1, 2]], faces[:, [4, 5, 6]]], axis=0)
coords = pd.read_csv(base_path + 'coords.csv', header=None, keep_default_na=False, sep='\ ').values
vals = np.random.random(len(coords))
loc_data = pd.read_csv(base_path + 'ATP_locations.csv').values[:, 1:]
locations = loc_data[:, :3]
orientations = loc_data[:, 3:]

locations[:, 1] = 697 - locations[:, 1]

print('positioning protein surfaces')
all_coords = []
all_faces = []
for loc, orient in zip(locations, orientations):
    all_faces.append(faces + len(all_coords)*len(coords))
    r = R.from_euler('xyz', orient, degrees=True)
    rot_coords = r.apply(coords, inverse=True)
    all_coords.append(rot_coords + loc)

all_coords = np.concatenate(all_coords, axis=0)
locations = locations[:, [2, 1, 0]]
coords = coords[:, [2, 1, 0]]
all_coords = all_coords[:, [2, 1, 0]]
all_faces = np.concatenate(all_faces, axis=0)
all_vals = np.random.random(len(all_coords))
print('surfaces ready')

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer(ndisplay=3)
    viewer.dims.embedded = True
    # add tomogram
    viewer.add_image(path=base_path + 'Suitcase_tomogram.tif', name='tomogram')
    viewer.layers[0].data = -viewer.layers[0].data
    # add labels
    #viewer.add_labels(membrane, name='membrane')

    # add protein centers
    #viewer.add_points(locations, face_color='red', edge_width=0, opacity=0.6, n_dimensional=True, name='protein centers')

    # add protein
    #viewer.add_surface((coords, faces, vals))

    # add proteins
    viewer.add_surface((all_coords, all_faces, all_vals), colormap='blue', name='proteins')

    viewer.layers['tomogram'].dims.ndisplay = 2

"""
Display a pyvista surface
"""

import pyvista as pv
from pyvista import examples
import numpy as np
import napari

# Load the surface and triangulate just in case
surf = pv.read(examples.planefile).triangulate()

# Convert the data to a simple numpy representation
# that napari understands
vertices = np.asarray(surf.points)
faces = np.asarray(surf.faces).reshape((-1, 4))[:, 1:]
normals = np.asarray(surf.point_normals)
# generate values by projecting on a "lighting vector"
values = np.dot(normals, [1, -1, 1])
print(vertices.shape, faces.shape, values.shape)
# (1335, 3) (2452, 3) (1335,)

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()

    # add the surface
    viewer.add_surface((vertices, faces, values))

    # turn on 3D rendering
    viewer.dims.ndisplay = 3
import napari
import numpy as np
from shapely.ops import cascaded_union
from sklearn.datasets import make_blobs
from shapely.geometry import Point, Polygon, MultiPolygon


with napari.gui_qt():
    v = napari.Viewer()

    @v.bind_key('f')
    def get_selected_points(v):
        union_data = cascaded_union([Polygon(i) for i in v.layers['annotation'].data])
        if isinstance(union_data, type(MultiPolygon())):
            polys = [Polygon(np.array(poly.exterior.coords)) for poly in union_data]
        else:
            polys = [Polygon(np.array(union_data.exterior.coords))]
        
        all_pts    = [Point(i) for i in X]
        mask       = np.any([[p.within(poly) for p in all_pts] for poly in polys], axis=0)
        sel_pts    = v.add_points(X[mask],face_color='red',size=0.1,name='selected')
        
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, y = make_blobs(n_samples=1000, centers=centers, cluster_std=0.6)
    all_points = v.add_points(X, size=0.05)

    v.add_shapes(name='annotation', edge_width=0, opacity=0.1)

import numpy as np
import napari
from skimage import data

image = np.random.random((128, 128))
blobs = data.binary_blobs(
    length=128, blob_size_fraction=0.05, n_dim=2, volume_fraction=0.3
)


with napari.gui_qt():
    viewer = napari.view_image(image)
    labels = viewer.add_labels(blobs)
    points = viewer.add_points(size=4)
    points.editable = False

    def mouse_drag(viewer, event):
        labels = None
        points = None
        for layer in viewer.layers:
            if type(layer).__name__ == 'Labels':
                labels = layer
            elif type(layer).__name__ == 'Points':
                points = layer
        if labels is None:
            raise ValueError('No labels layer found')
        if points is None:
            raise ValueError('No points layer found')

        # only exectute when points is active
        if viewer.active_layer == points:
            # Round coordinates
            coords = tuple(np.round(points.coordinates).astype(int))
            # Check if label > 0
            if labels.data[coords]:
                print(f'Point added at {coords}')
                points.add(coords)
            else:
                print(f'No label at {coords} so no point added')

    # Add callback to viewer
    viewer.mouse_drag_callbacks.append(mouse_drag)
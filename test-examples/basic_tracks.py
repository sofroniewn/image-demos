import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    data = np.concatenate([np.expand_dims(list(range(8)), axis=1), np.random.randint(4, size=(8, 4))], axis=1)
    print(data.shape)
    print(data)
    viewer.add_tracks(data)


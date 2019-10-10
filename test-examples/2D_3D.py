from skimage import data
import numpy as np
import napari

with napari.gui_qt():
  viewer = napari.Viewer()
  viewer.add_image(data.moon(), name='moon')
  blobs = np.stack(
      [
          data.binary_blobs(
              length=512, blob_size_fraction=0.05, n_dim=2, volume_fraction=f
          )
          for f in np.linspace(0.05, 0.5, 10)
      ],
      axis=0,
  ).astype(float)
  viewer.add_image(blobs, name='blobs', opacity=0.5, colormap='red')

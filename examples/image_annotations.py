"""
Add annotations to random blobs
"""
from skimage import data
import numpy as np
import napari


# Create image data
blobs = np.array([data.binary_blobs(length=128, volume_fraction=f, n_dim=2) for f in np.linspace(0.1, 0.9, 30)])
image_class = np.zeros(len(blobs), dtype=int)

# Create annotation layer
border_width = 3
border = [[[-border_width, -border_width],
           [border_width + blobs.shape[1], border_width + blobs.shape[2]]]]
border_cols = ['white', 'red', 'green', 'blue']


with napari.gui_qt():
    # add the images
    viewer = napari.view_image(blobs, name='blobs', metadata={'class': image_class})

    # add the borders
    viewer.add_shapes(border, shape_type='rectangle',
                      face_color=[0, 0, 0, 0], edge_color='white',
                      edge_width=border_width*2, opacity=0.75, name='annotation')
    viewer.layers['annotation']._value = (None, None)
    viewer.layers['annotation'].events.highlight()
    viewer.reset_view()

    @viewer.bind_key('0')
    def set_0(viewer):
        """Set annotation
        """
        key = 0
        shapes = viewer.layers['annotation']
        image_class = viewer.layers['blobs'].metadata['class']
        index = viewer.dims.indices[0]
        image_class[index] = key
        shapes._data_view.update_edge_color(0, border_cols[key])
        shapes.events.edge_color()
        viewer.status = str(key)

    @viewer.bind_key('1')
    def set_1(viewer):
        """Set annotation
        """
        key = 1
        shapes = viewer.layers['annotation']
        image_class = viewer.layers['blobs'].metadata['class']
        index = viewer.dims.indices[0]
        image_class[index] = key
        shapes._data_view.update_edge_color(0, border_cols[key])
        shapes.events.edge_color()
        viewer.status = str(key)

    @viewer.bind_key('2')
    def set_2(viewer):
        """Set annotation
        """
        key = 2
        shapes = viewer.layers['annotation']
        image_class = viewer.layers['blobs'].metadata['class']
        index = viewer.dims.indices[0]
        image_class[index] = key
        shapes._data_view.update_edge_color(0, border_cols[key])
        shapes.events.edge_color()
        viewer.status = str(key)

    @viewer.bind_key('3')
    def set_3(viewer):
        """Set annotation
        """
        key = 3
        shapes = viewer.layers['annotation']
        image_class = viewer.layers['blobs'].metadata['class']
        index = viewer.dims.indices[0]
        image_class[index] = key
        shapes._data_view.update_edge_color(0, border_cols[key])
        shapes.events.edge_color()
        viewer.status = str(key)

    def recolor_box(event):
        index = viewer.dims.indices[0]
        shapes = viewer.layers['annotation']
        image_class = viewer.layers['blobs'].metadata['class']
        key = image_class[index]
        shapes._data_view.update_edge_color(0, border_cols[key])
        shapes.events.edge_color()

    viewer.dims.events.axis.connect(recolor_box)

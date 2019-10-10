from skimage import data
import napari


with napari.gui_qt():
    viewer = napari.view_image(data.moon(), name='moon')
    viewer.layers['moon'].contrast_limits=(100, 175)

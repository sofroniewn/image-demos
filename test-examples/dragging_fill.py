import napari
from skimage import data, segmentation

astro = data.astronaut()
segmented = segmentation.slic(
    astro, compactness=20, sigma=1, start_label=1
)

with napari.gui_qt():
    v = napari.Viewer()
    imglayer = v.add_image(astro)
    seglayer = v.add_labels(segmented)
    seglayer.mode = 'fill'

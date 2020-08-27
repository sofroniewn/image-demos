from skimage import data, color
import napari

astro = data.astronaut()
gray_astro = color.rgb2gray(astro[::4, ::4])

with napari.gui_qt():
    viewer = napari.view_image(astro, rgb=True)
    viewer.add_image(
        gray_astro,
        scale=[4, 4],
        opacity=0.7,
    )
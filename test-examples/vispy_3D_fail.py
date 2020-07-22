"""
Display a 2D Image visual then remove and display 3D Volume visual
"""
import numpy as np
from vispy import app, scene, io

# Create raw image and volume data
image_data = np.random.random((500, 500))
volume_data = np.random.random((100, 500, 500))

# Create canvas and view
canvas = scene.SceneCanvas(keys='interactive', size=(600, 600), show=True)
view = canvas.central_widget.add_view()

# Set panzoom camera
view.camera = scene.cameras.PanZoomCamera()

# Show and remove image
image_vis = scene.visuals.Image(image_data)
image_vis.parent = view.scene

image_vis2 = scene.visuals.Image(image_data)
image_vis2.parent = view.scene

# Implement key presses
@canvas.events.key_press.connect
def on_key_press(event):
    print(event.text)
    if event.text == 'x':

        image_vis2.parent = None
        volume_vis2 = scene.visuals.Volume(volume_data)
        volume_vis2.parent = view.scene

        image_vis.parent = None
        volume_vis = scene.visuals.Volume(volume_data)
        volume_vis.parent = view.scene

        # Set archball camera
        view.camera = scene.cameras.ArcballCamera(fov=60)

# Run example
app.run()

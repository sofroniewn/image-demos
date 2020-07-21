"""
Display a 2D Image visual then remove and display 3D Volume visual
"""
import numpy as np
from vispy import app, scene, io

# Create raw image and volume data
image_data = np.random.random((100, 100))
volume_data = np.random.random((100, 100, 100))

# Create canvas and view
canvas = scene.SceneCanvas(keys='interactive', size=(600, 600), show=True)
view = canvas.central_widget.add_view()

# Create cameras
cam1 = scene.cameras.PanZoomCamera(parent=view.scene)
cam2 = scene.cameras.ArcballCamera(parent=view.scene, fov=60)

# Show and remove image
view.camera = cam1  # Select PanZoomCamera
image_vis = scene.visuals.Image(image_data, parent=view.scene)
image_vis.parent = None

# Show volume
view.camera = cam2  # Select ArcballCamera
volume_vis = scene.visuals.Volume(volume_data, parent=view.scene)

# Run example
app.run()
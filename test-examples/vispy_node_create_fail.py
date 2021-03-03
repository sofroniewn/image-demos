"""
Create a node in a draw loop
"""
from vispy import app, scene
from vispy.scene.node import Node
app.use_app('pyqt5')

# Create canvas and view
canvas = scene.SceneCanvas(keys='interactive', size=(600, 600), show=True)
view = canvas.central_widget.add_view()
view.camera = scene.cameras.PanZoomCamera()

node_index = 0
def on_draw(event):
    global node_index
    print(f"VispyCamera.on_draw: {node_index}")
    Node()
    node_index += 1

canvas.connect(on_draw)

# Run example
app.run()

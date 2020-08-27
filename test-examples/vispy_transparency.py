import os
import PySide2
from pathlib import Path

os.environ['QT_PLUGIN_PATH'] = str(
    Path(PySide2.__file__).parent / 'Qt' / 'plugins'
)

from vispy.app import use_app
app = use_app('pyside2')


from vispy.scene import SceneCanvas
from vispy.scene.visuals import Polygon

canvas = SceneCanvas()
v = canvas.central_widget.add_view()
v.bgcolor = 'gray'
v.camera = 'panzoom'
cx, cy = (0.5, 0.5)
halfx, halfy = (0.1, 0.1)
poly_coords = [(cx - halfx, cy - halfy),
               (cx + halfx, cy - halfy),
               (cx + halfx, cy + halfy),
               (cx - halfx, cy + halfy)]
poly = Polygon(poly_coords, color=(1.0, 0.0, 0.0, 0.5), border_color=(1.0, 1.0, 1.0, 0.2),
               border_width=3,  parent=v.scene)
canvas.show()
app.run()
import napari
import numpy as np

# with napari.gui_qt():
#     viewer = napari.Viewer()
#     image = np.random.rand(1000,1000)
#     points = np.random.rand(100, 2) * 1000
#     shapes = [np.random.rand(10,2) * 1000 for x in range(10)]
    
#     viewer.add_image(image)
#     viewer.add_shapes(shapes, shape_type='polygon')
#     viewer.add_points(points)

#     # remove and re-add image    
#     viewer.layers.remove('image')
#     viewer.add_image(image, name='image')
    
#     # remove non-image data
#     viewer.layers.remove('shapes')
#     viewer.layers.remove('points')
#     # add it back
#     viewer.add_shapes(shapes, shape_type='polygon')
#     viewer.add_points(points)
#    # and mysteriously, shapes is not visible


with napari.gui_qt():
    viewer = napari.Viewer()
    vis = viewer.window.qt_viewer.layer_to_visual
    image = np.random.rand(10,10)
    
    viewer.add_image(image, colormap='red', name='red')
    print([vis[x].order for x in viewer.layers])
    viewer.add_image(image, colormap='green', name='green')
    print([vis[x].order for x in viewer.layers])
    viewer.add_image(image, colormap='blue', name='blue')
    print([vis[x].order for x in viewer.layers])


    # remove and re-add image    
    viewer.layers.remove('red')
    viewer.add_image(image, colormap='red', name='red')
    print([vis[x].order for x in viewer.layers])
    
    # remove non-image data
    viewer.layers.remove('green')
    viewer.layers.remove('blue')
    print([vis[x].order for x in viewer.layers])
    # add it back
    viewer.add_image(image, colormap='green', name='green')
    viewer.add_image(image, colormap='blue', name='blue')
    viewer.layers['blue'].visible = False
    print([vis[x].order for x in viewer.layers])
   # and mysteriously green is not visible
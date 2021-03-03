import napari

points = [[100, 100], [200, 200], [333, 111]]

with napari.gui_qt():

    viewer = napari.view_points(points)
    points_layer = viewer.layers[0]

    print('initial face colors:')
    print(points_layer.face_color)

    # select a point and update the color
    points_layer.selected_data = [0]
    points_layer.current_face_color = 'red'

    print('new current_face_color:')
    print(points_layer._face.current_color)
    print('new face_colors:')
    print(points_layer.face_color)
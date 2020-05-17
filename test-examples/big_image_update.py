import numpy as np
import napari
import time

with napari.gui_qt():
    # create the viewer with an image
    data = np.random.random((2, 10240, 10240))
    viewer = napari.Viewer()
    layer = viewer.add_image(data[1], is_multiscale=False)

    def layer_update(*, update_period, num_updates):
        # number of times to update
        t = time.time()
        for k in range(num_updates):
            layer.data = data[k%2]
            #layer.events.set_data()
            #layer.data = data[k%2]
            # a = time.time()
            # layer.data.all() != data[k%2].all()
            # print('asdf', time.time()-a)
            # 
            # # check that data layer is properly assigned and not blocked?
            # while layer._data_view.all() != data[k%2].all():
            #     layer._data_view = data[k%2]
            print(round(1/(time.time()-t), 2))
            t = time.time()

    viewer.update(layer_update, update_period=0.0, num_updates=10)

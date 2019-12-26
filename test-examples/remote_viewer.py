import napari
import asyncio


address = 'tcp://127.0.0.1:52729'
with napari.gui_qt():
    viewer = napari.Viewer(address=address)
    #viewer.title = 'wwww'
    viewer.remote.connect()

    # loop = asyncio.get_event_loop()
    # print(loop)
    # loop.run_until_complete(viewer.remote.title.sub())

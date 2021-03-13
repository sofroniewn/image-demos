"""
Connect napari to webcam
"""

import time
import cv2
import napari
from napari.qt import thread_worker


def on_yield(image):
    if image is None:
        return

    if 'webcam' in [layer.name for layer in viewer.layers]:
        viewer.layers['webcam'].data = image
    else:
        viewer.add_image(image, name='webcam')


@thread_worker(connect={'yielded': on_yield})
def watch_webcam(video_capture):
    """Watch the webcam for incoming frames"""
    while True:
        if not video_capture.isOpened():
            print('No frame available')
            time.sleep(1)
            yield None

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # invert frame
        frame = frame[:, ::-1, :].mean(axis=2)
        yield frame

        # Add a slight sleep so as not to get overwhelmed by frames
        time.sleep(0.01)


# Create viewer
viewer = napari.Viewer()

# Start video capture and worker
video_capture = cv2.VideoCapture(0)
worker = watch_webcam(video_capture)

# Run napari
napari.run()

# When everything is done, release the capture
video_capture.release()

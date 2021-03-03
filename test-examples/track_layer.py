import napari
import numpy as np


def _circle(r, theta):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y

def _sphere(r, theta, psi):
    x = r*np.sin(theta) + r*np.cos(psi)
    y = r*np.sin(theta) + r*np.sin(psi)
    z = r*np.cos(theta)
    return x, y, z


def tracks_2d(num_tracks = 10):
    """ create 2d+t track data """
    tracks, properties = [], []

    for i in range(num_tracks):

        track = np.zeros((100,3), dtype=np.float32)
        track[:,0] = np.arange(track.shape[0])

        r = 50*np.random.random()
        phase = np.mod(track[:,0]*0.1 + np.random.random()*np.pi, 2*np.pi)
        x, y = _circle(r, phase)

        track[:,1] = 50. + x
        track[:,2] = 50. + y

        tracks.append(track)
        properties.append({'time': track[:,0],
                           'theta': phase.tolist(),
                           'radius': r})

    return tracks, properties


def tracks_3d(num_tracks = 10):
    """ create 3d+t track data """
    tracks, properties = [], []

    for i in range(num_tracks):

        track = np.zeros((100,4), dtype=np.float32)
        track[:,0] = np.arange(track.shape[0])

        r = 50*np.random.random()
        theta = np.mod(track[:,0]*0.1 + np.random.random()*np.pi, 2*np.pi)
        psi = np.mod(track[:,0]*0.1 + np.random.random()*np.pi, 2*np.pi)
        x, y, z = _sphere(r, theta, psi)

        track[:,1] = 50. + x
        track[:,2] = 50. + y
        track[:,3] = 50. + z

        tracks.append(track)

        properties.append({'time': track[:,0],
                           'theta': theta,
                           'psi': psi,
                           'radius': r})

    return tracks, properties


# tracks, properties = tracks_2d(num_tracks=100)
tracks, properties = tracks_3d(num_tracks=100)

with napari.gui_qt():
    viewer = napari.Viewer()
    # viewer.add_tracks(data=tracks, name='test')
    viewer.add_tracks(data=tracks, properties=properties, name='test')